import numpy as np
import matplotlib.pyplot as plt


def binned_lightcurve(meta, bjdtdb, i):
    plt.figure(4300 + i, figsize=(8, 6))
    plt.clf()
    plt.suptitle(f"Bandpass {i}: %.3f - %.3f" % (meta.wave_low[i], meta.wave_hi[i]))
    ax = plt.subplot(111)
    mjd = np.floor(bjdtdb[0])
    # Normalized light curve
    norm_lcdata = meta.lcdata[i] / meta.lcdata[i, -1]
    norm_lcerr = meta.lcerr[i] / meta.lcdata[i, -1]
    plt.errorbar(bjdtdb - mjd, norm_lcdata, norm_lcerr, fmt='o', color=f'C{i}', mec='w')
    plt.text(0.05, 0.1, "MAD = " + str(np.round(1e6 * np.median(np.abs(np.ediff1d(norm_lcdata))))) + " ppm",
             transform=ax.transAxes, color='k')
    plt.ylabel('Normalized Flux')
    plt.xlabel(f'Time [MJD + {mjd}]')

    plt.subplots_adjust(left=0.10, right=0.95, bottom=0.10, top=0.90, hspace=0.20, wspace=0.3)
    plt.savefig(meta.outputdir + 'figs/Fig' + str(4300 + i) + '-' + meta.eventlabel + '-1D_LC.png')
    plt.close()

def drift1d(meta):
    plt.figure(4101, figsize=(8,4))
    plt.clf()
    plt.plot(np.arange(meta.nx)[np.where(meta.driftmask)], meta.drift1d[np.where(meta.driftmask)], '.')
    # plt.subplot(211)
    # for j in range(istart,ev.n_reads-1):
    #     plt.plot(ev.drift2D[:,j,1],'.')
    # plt.ylabel('Spectrum Drift Along y')
    # plt.subplot(212)
    # for j in range(istart,ev.n_reads-1):
    #     plt.plot(ev.drift2D[:,j,0]+ev.drift[:,j],'.')
    plt.ylabel('Spectrum Drift Along x')
    plt.xlabel('Frame Number')
    plt.tight_layout()
    plt.savefig(meta.outputdir + 'figs/Fig4101-Drift.png')
    plt.close()

def cc_spec(meta, ref_spec, fit_spec, nx, n):
    plt.figure(4500)
    plt.clf()
    plt.title(f'Cross Correlation - Spectrum {n}')
    plt.plot(range(nx), ref_spec, '-', label='Reference Spectrum')
    plt.plot(range(meta.drift_range,nx-meta.drift_range), fit_spec, '-', label='Current Spectrum')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig(meta.outputdir + f'figs/Fig4500-{n}-CC_Spec')
    plt.close()

def cc_vals(meta, vals, n):
    plt.figure(4501)
    plt.clf()
    plt.title(f'Cross Correlation - Values {n}')
    plt.plot(range(-meta.drift_range,meta.drift_range+1), vals, '.')
    plt.tight_layout()
    plt.savefig(meta.outputdir + f'figs/Fig4501-{n}-CC_Vals')
    plt.close()
