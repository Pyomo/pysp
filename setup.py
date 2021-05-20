#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright 2017 National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

"""
Script to generate the installer for pysp.
"""

import sys
import os

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as README:
        # Strip all leading badges up to, but not including the COIN-OR
        # badge so that they do not appear in the PyPI description
        while True:
            line = README.readline()
            if 'COIN-OR' in line:
                break
            if line.strip() and '[![' not in line:
                break
        return line + README.read()

def get_version():
    # Source pyomo/version/info.py to get the version number
    _verInfo = dict(globals())
    _verFile = os.path.join(os.path.dirname(__file__), 'pysp', 'version.py')
    with open(_verFile) as _FILE:
        exec(_FILE.read(), _verInfo)
    return _verInfo['__version__']

from setuptools import setup, find_packages

def run_setup():
   setup(name='PySP',
      #
      # Note: the release number is set in pyomo/version/info.py
      #
      version=get_version(),
      maintainer='Pyomo Developer Team',
      maintainer_email='pyomo-developers@googlegroups.com',
      url='https://github.com/Pyomo/pysp',
      license='BSD',
      platforms=["any"],
      description='PySP: Stochastic programming in Python',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      keywords=['optimization'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules' ],
      python_requires='>=3.6',
      install_requires=[
          'Pyomo>=6.0',
          'PyUtilib>=6.0.0',
          'ply',
          'six>=1.4',
      ],
      packages=find_packages(exclude=("scripts",)),
      entry_points="""
        [console_scripts]
        runbenders=pysp.benders:Benders_main
        evaluate_xhat=pysp.evaluate_xhat:EvaluateXhat_main
        runph=pysp.phinit:PH_main
        runef=pysp.ef_writer_script:main
        phsolverserver=pysp.phsolverserver:main
        scenariotreeserver=pysp.scenariotree.server_pyro:main
        computeconf=pysp.computeconf:main
        pyro_mip_server = pysp.pyro.pyro_mip_server:main
        pyomo_ns = pysp.pyro.pyro_commands:pyomo_ns
        pyomo_nsc = pysp.pyro.pyro_commands:pyomo_nsc
        kill_pyro_mip_servers = pysp.pyro.pyro_commands:kill_pyro_mip_servers
        launch_pyro_mip_servers = pysp.pyro.pyro_commands:launch_pyro_mip_servers
      """
      )

run_setup()
