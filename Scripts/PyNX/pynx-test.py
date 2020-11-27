#!C:\ProgramData\Anaconda3\python.exe
# -*- coding: utf-8 -*-

# PyNX - Python tools for Nano-structures Crystallography
#   (c) 2018-present : ESRF-European Synchrotron Radiation Facility
#       authors:
#         Vincent Favre-Nicolin, favre@esrf.fr

import sys
import io
import unittest
from pynx.test import *

help_text = """
pynx-test: script to run PyNX unit tests

Example:
    pynx-test: will run all tests

command-line arguments can be used to specify specific tests to be run (by default: all):
    processing_unit: run processing_unit tests
    cdi: run CDI API tests
    cdi_runner: run CDI runner scripts test
    opencl: only perform tests using OpenCL - this excludes CUDA tests
    cuda: only perform tests using CUDA - this excludes OpenCL tests
    live_plot: include live plotting tests

Other options:
    mailto=name@esrf.fr : will mail test results to given address, using localhost
    mailto_fail=name@esrf.fr : will mail test results to given address, using localhost, only if tests fail

"""


def run_tests():
    test_suite = unittest.TestSuite()
    mailto = None
    mail_no_error = True
    for arg in sys.argv:
        if 'pynx-test.py' in arg:
            continue
        elif arg.lower() == 'help':
            print(help_text)
        elif arg.lower() == 'opencl':
            continue
        elif arg.lower() == 'cuda':
            continue
        elif 'mailto_fail' in arg.lower():
            mailto = arg.split('mailto_fail=')[-1]
            mail_no_error = False
            print("Will mail results to %s if there are errors" % mailto)
        elif 'mailto' in arg.lower():
            mailto = arg.split('mailto=')[-1]
            print("Will mail results to %s" % mailto)
        else:
            try:
                test_suite.addTests(eval("%s_suite()" % arg))
            except:
                print("Could not find the following unittest suite: %s_suite" % arg)

    if test_suite.countTestCases() == 0:
        # No specific suite was specified from the command line, so use the general one
        test_suite = suite()

    res = unittest.TextTestRunner(verbosity=2, descriptions=False).run(test_suite)

    info = "Running:\n"
    for arg in sys.argv:
        info += arg + " "
    info += "\n"

    nb_err_fail = len(res.errors) + len(res.failures)
    if len(res.errors):
        info += "\nERRORS:\n\n"
        for t, s in res.errors:
            tid = t.id()
            tid1 = tid.split('.')[-1]
            tid0 = tid.split('.' + tid1)[0]
            info += '%s (%s):\n' % (tid1, tid0) + s
    if len(res.failures):
        info += "\nFAILURES:\n\n"
        for t, s in res.failures:
            tid = t.id()
            tid1 = tid.split('.')[-1]
            tid0 = tid.split('.' + tid1)[0]
            info += '%s (%s):\n\n' % (tid1, tid0) + s + '\n\n'

    if mailto is not None and ((nb_err_fail > 0) or mail_no_error):
        import smtplib
        from email.message import EmailMessage

        msg = EmailMessage()
        msg['From'] = 'favre@esrf.fr'
        msg['to'] = mailto
        msg['Subject'] = 'PyNX test results [nb_fail=%d nb_error=%d]' % (len(res.failures), len(res.errors))

        msg.set_content(info)

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
        print("Sent message with subject: %s" % msg['Subject'])

    sys.exit(int(nb_err_fail > 0))


if __name__ == '__main__':
    run_tests()