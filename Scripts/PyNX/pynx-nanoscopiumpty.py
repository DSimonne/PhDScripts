#!C:\ProgramData\Anaconda3\python.exe
# -*- coding: utf-8 -*-

# PyNX - Python tools for Nano-structures Crystallography
#   (c) 2016-present : ESRF-European Synchrotron Radiation Facility
#       authors:
#         Vincent Favre-Nicolin, favre@esrf.fr

from __future__ import division

import sys
from pynx.ptycho.runner import PtychoRunnerException, helptext_generic
from pynx.ptycho.runner.nanoscopium import PtychoRunnerNanoscopium, PtychoRunnerScanNanoscopium, helptext_beamline, \
    params

help_text = helptext_generic + helptext_beamline

if __name__ == '__main__':
    try:
        w = PtychoRunnerNanoscopium(sys.argv, params, PtychoRunnerScanNanoscopium)
        w.process_scans()
    except PtychoRunnerException as ex:
        print(help_text)
        print('\n\n Caught exception: %s    \n' % (str(ex)))
        sys.exit(1)
