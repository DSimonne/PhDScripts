#!C:\ProgramData\Anaconda3\python.exe
# -*- coding: utf-8 -*-

# PyNX - Python tools for Nano-structures Crystallography
#   (c) 2016-present : ESRF-European Synchrotron Radiation Facility
#       authors:
#         Vincent Favre-Nicolin, favre@esrf.fr

from __future__ import division

import sys
from pynx.ptycho.runner import PtychoRunnerException, helptext_generic
from pynx.ptycho.runner.simulation import PtychoRunnerSimul, PtychoRunnerScanSimul, helptext_beamline, params
from pynx.mpi import MPI

help_text = helptext_generic + helptext_beamline

if __name__ == '__main__':
    try:
        if 'profiling' in sys.argv:
            import cProfile

            r = 0
            if MPI is not None:
                r = MPI.COMM_WORLD.Get_rank()
            cProfile.run('PtychoRunnerSimul(sys.argv, params, PtychoRunnerScanSimul).process_scans()',
                         'profiling-%02d.txt' % r)
        else:
            w = PtychoRunnerSimul(sys.argv, params, PtychoRunnerScanSimul)
            w.process_scans()
    except PtychoRunnerException as ex:
        print(help_text)
        print('\n\n Caught exception: %s    \n' % (str(ex)))
        sys.exit(1)
