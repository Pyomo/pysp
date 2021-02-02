#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright 2017 National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

from os.path import dirname, abspath

import sys
import pyutilib.dev.runtests

def runPySPTests(argv=None):
    if argv is None:
        argv = sys.argv

    basedir=dirname(dirname(dirname(abspath(__file__))))
    targets=['pysp']
    return pyutilib.dev.runtests.run(targets, basedir, argv)

if __name__ == '__main__':
    sys.exit(runPySPTests())
