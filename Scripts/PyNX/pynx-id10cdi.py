#!C:\ProgramData\Anaconda3\python.exe
# -*- coding: utf-8 -*-

# PyNX - Python tools for Nano-structures Crystallography
#   (c) 2017-present : ESRF-European Synchrotron Radiation Facility
#       authors:
#         Vincent Favre-Nicolin, favre@esrf.fr

from __future__ import division

import sys
from pynx.cdi.runner import helptext_generic, CDIRunnerException
from pynx.cdi.runner.id10 import CDIRunnerID10, CDIRunnerScanID10, helptext_beamline, params


help_text = helptext_generic + helptext_beamline


if __name__ == '__main__':
    try:
        w = CDIRunnerID10(sys.argv, params, CDIRunnerScanID10)
        w.process_scans()
    except CDIRunnerException as ex:
        print(help_text)
        print('\n\n Caught exception: %s    \n' % (str(ex)))
        sys.exit(1)

