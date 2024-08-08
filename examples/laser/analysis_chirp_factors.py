#! /usr/bin/env python3

# Copyright 2022
#
# This file is part of HiPACE++.
#
# Authors: Xingjian Hui
# License: BSD-3-Clause-LBNL


import matplotlib.pyplot as plt
import matplotlib
import argparse
import numpy as np
import scipy.constants as scc
import scipy
from openpmd_viewer.addons import LpaDiagnostics

do_plot = False

parser = argparse.ArgumentParser(description='Compare laser propagation in vacuum with theory')
parser.add_argument('--output-dir',
                    dest='output_dir',
                    default='diags/hdf5',
                    help='Path to the directory containing output files')
args = parser.parse_args()



ts1 = LpaDiagnostics(args.output_dir)

#                   calculate phi2\beta\zeta
laser_module1=np.abs(Ar)
z_diff = np.diff(m.z)
y_diff = np.diff(m.y)
phi_envelop=np.array(np.arctan2(Ar.imag, Ar.real))
#unwrap phi_envelop
phi_envelop = np.unwrap(phi_envelop, axis=0)
#calculate local freq
z_diff = np.diff(m.z)
pphi_pz = (np.diff(phi_envelop, axis=0)).T / (z_diff/scc.c)
#temp chirp (phi2)
pphi_pz2 = ((np.diff(pphi_pz, axis=1)) / (z_diff[:len(z_diff)-1])/scc.c).T
#spatio chirp (zeta)
pphi_pzpy = ((np.diff(pphi_pz, axis=0)).T / (y_diff))
#weight average
temp_chirp = 0
sum = 0
nu = 0
for i in range(len(m.z)-2):
    for j in range(len(m.x)-2):
        temp_chirp = temp_chirp+pphi_pz2[i,j] * laser_module1[i,j]
        nu = nu + pphi_pzpy[i,j] * laser_module1[i,j]
        sum = sum + laser_module1[i,j]
x = temp_chirp * scc.c**2 / sum
a = 4 * x
b = -4
c = tau**4 x
phi2 = np.max([(-b-np.sqrt(b**2-4*a*c)) / (2*a),(-b+np.sqrt(b**2-4*a*c)) / (2*a)])
