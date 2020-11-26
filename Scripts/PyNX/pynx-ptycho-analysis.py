#!C:\ProgramData\Anaconda3\python.exe
# -*- coding: utf-8 -*-

# PyNX - Python tools for Nano-structures Crystallography
#   (c) 2016-present : ESRF-European Synchrotron Radiation Facility
#       authors:
#         Vincent Favre-Nicolin, favre@esrf.fr
from __future__ import division

import sys
import time
import numpy as np
import h5py as h5
from pylab import  gcf, savefig, show, clf
from pynx.utils.math import ortho_modes
from pynx.version import get_git_version
_pynx_version = get_git_version()
from pynx.ptycho.analysis import probe_propagate, modes


params={'propagate': False, 'z-range': (-500e-6,500e-6,600), 'modes': False, 'wavelength': 12.3984e-10/8,
        'pixelsize': None, 'zdet':None, 'prefix': None, 'saveplot': False}

helptext="""
pynx-analyseprobe: Script to analyse a probe from a ptychographic analysis

Example:
    pynx-ptycho-analysis.py Run0001-04.cxi propagate z-range=-2e-3,500e-6,500 modes saveplot

command-line arguments:
    path/to/Run.npz or path/to/Run.cxi: path to .cxi or .npz file with the probe to analyse.
        [mandatory]

    propagate: if used, the probe will be propagated to find the focus and a standard plot
        will be issued

    z-range=-2e-3,500e-6,500: the range as (zmin, zmax, nbz) for the propagation 
        [default=(-500e-6,500e-6,600)], in meters

    modes: if used, the modes will be calculated for the probe, and a plot with statistics
        will be issued [ignored if probe is 2D (no modes)]

    saveplot: if used, plots are saved rather than showed on screen. If not set, and not using
        ipython, the plot must be closed to proceed or exit.

    prefix=scan67/Run654: if used, will be used as prefix to save the plots 
        (e.g. 'scan67/Run654-probe-z.png', 'scan67/Run654-probe-modes.png')
        [default: use the probe name prefix]
"""

if __name__ == '__main__':
    probe = None
    for arg in sys.argv:
        if arg == 'help':
            print(helptext)
        elif arg in ['propagate', 'modes', 'saveplot']:
            params[arg] = True
        else:
            s = arg.find('=')
            if s > 0 and s < (len(arg) - 1):
                k = arg[:s].lower()
                v = arg[s + 1:]
                print(k, v)
                if k == 'z-range':
                    params[k] = eval(v)
                elif k in ['wavelength', 'pixelsize', 'zdet']:
                    params[k] = float(v)
            elif arg.find('.cxi') > 0:
                h = h5.File(arg, 'r')
                # Find last entry in file
                i = 1
                while True:
                    if 'entry_%d' % i not in h:
                        break
                    i += 1
                entry = h['entry_%d' % (i - 1)]
                probe = entry['probe/data'][()]
                if params['pixelsize'] is None:
                    params['pixelsize'] = (entry['probe/x_pixel_size'][()] + entry['probe/y_pixel_size'][()]) / 2
                if params['wavelength'] is None:
                    if 'instrument_1/beam_1/incident_wavelength' in entry:
                       params['wavelength'] = entry['instrument_1/beam_1/incident_wavelength']
                    else:
                        nrj = None
                        if 'instrument_1/beam_1/incident_energy' in entry:
                            nrj = entry['instrument_1/beam_1/incident_energy'] / 1.60218e-16
                        elif 'instrument_1/source_1/energy' in entry:
                            # Old CXI with energy stored as source (ring) energy
                            nrj = entry['instrument_1/source_1/energy'] / 1.60218e-16
                        if nrj is not None:
                            params['wavelength'] = 12.3984e-10 / nrj
                params['prefix'] = arg[:-4]

            elif arg.find('.npz') >0:
                tmp = np.load(arg)
                probe = tmp['probe']
                if "pixelsize" in tmp.keys():
                    if np.isscalar(tmp['pixelsize']):
                        params['pixelsize'] = float(tmp['pixelsize'])
                    else:
                        params['pixelsize'] = np.array(tmp['pixelsize']).mean()
                else:
                    if params['zdet'] is not None and params['wavelength'] is not None:
                        params['pixelsize'] = params['wavelength'] * params['zdet'] / 55e-6 / probe.shape[-1]
                        print("No pixel size given, assuming detector pixel size was 55 microns => pixel size= %5.1fnm"%(params['pixelsize']*1e9))
                    else:
                        assert params['pixelsize'] is not None
                params['prefix'] = arg[:-4]
    if probe is None:
        print('ERROR: no probe data file was supplied !\n')
        print(helptext)

    if params['propagate'] is False and params['modes'] is False:
        print("\nERROR: neither keyword 'propagate' or 'modes' is given !\n")
        print(helptext)

    if params['modes'] and (probe.ndim == 2 or (probe.ndim == 3 and probe.shape[0] == 1)):
        print("\nERROR: keyword 'modes' is given, but probe has only one mode !\n")
        print(helptext)

    if probe.ndim == 3:
        if probe.shape[0] > 1:
            # Orthogonalize modes
            probe = ortho_modes(probe)
            if params['modes']:
                print("\n", "#" * 100, "\n#", "\n#         Calculating probe modes: ", params['prefix'], "\n#\n", "#" * 100)
                modes(probe, params['pixelsize'])
                if params['saveplot']:
                    n = params['prefix'] + '-probe-modes.png'
                    dy = (6 + 1) / 72 / gcf().get_size_inches()[1]
                    gcf().text(dy/5, dy/2, "PyNX v%s, finished at %s" % (_pynx_version, time.strftime("%Y/%m/%d %H:%M:%S")),
                             fontsize=6, horizontalalignment='left', stretch='condensed')
                    print("Saving probe modes plot to: "+n)
                    savefig(n)
                    clf()
                else:
                    show()
        probe = probe[0]
    if params['propagate']:
        print("\n", "#" * 100, "\n#", "\n#         Propagating probe: ", params['prefix'], "\n#\n","#" * 100 )
        p, vdz, izmax, fig = probe_propagate(probe, params['z-range'], params['pixelsize'], params['wavelength'])
        if params['saveplot']:
            n = params['prefix'] + '-probe-z.png'
            dy = (6 + 1) / 72 / gcf().get_size_inches()[1]
            fig.text(dy/5, dy/2, "PyNX v%s, finished at %s" % (_pynx_version, time.strftime("%Y/%m/%d %H:%M:%S")),
                       fontsize=6, horizontalalignment='left', stretch='condensed')
            print("Saving propagated probe plot to: "+n)
            savefig(n)
        else:
            show()
