#!/usr/bin/python
import sys
import io
import os
import logging
import numpy as np
testdir = os.path.dirname(__file__)
srcdir = '../parsevasp'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
import kpoints

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Testing')

kpoints = kpoints.Kpoints(file_path = testdir + "/KPOINTSEXP")

kpoints.modify("tetra", [[7, 2, 3, 4, 5]])

kpoints.write(file_path = testdir + "/KPOINTSEXPMOD")
