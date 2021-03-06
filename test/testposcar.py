#!/usr/bin/python
import sys
import io
import os
import logging
import numpy as np
testdir = os.path.dirname(__file__)
srcdir = '../parsevasp'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
import poscar

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Testing')

poscar = poscar.Poscar(file_path = testdir + "/POSCAR")

poscar.modify("unitcell", np.array([[2.0, 0.0, 0.0],
                                 [0.0, 2.0, 0.0],
                                 [0.0, 0.0, 2.0]]))
poscar.delete_site(7)

poscar.write(file_path = testdir + "/POSCARMOD")
