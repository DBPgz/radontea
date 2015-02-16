#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Tests backprojection algorithm
"""
from __future__ import division, print_function

import numpy as np
import os
import sys
import time

from os.path import abspath, dirname, split

# Add parent directory to beginning of path variable
sys.path = [split(dirname(abspath(__file__)))[0]] + sys.path

import radontea
import radontea._Back_2D


def test_2d_backproject():
    myname = sys._getframe().f_code.co_name
    print("running ", myname)
    A = 5
    N = 13
    sino = np.arange(A*N).reshape(A,N) * np.pi
    angles = np.linspace(0,1,A)

    r = radontea.backproject(sino, angles)
    r2 = radontea._Back_2D.backproject(sino, angles)
    
    assert np.allclose(r, r2)
    assert np.allclose(r, results[myname])



results = dict()

results["test_2d_backproject"] = np.array(
[[ -0.38163035,  -0.12756273,   1.36873504,   4.43580189,
          8.08483758,  12.5331383 ,   6.86857254,   6.13056917,
          5.99404236,   5.72190782,   5.52527457,   6.15789564,
          9.43791146],
       [ -0.38163035,  -0.12756273,   6.55385956,  19.70441487,
          9.52733694,   6.46875773,   6.08709878,   5.56142245,
          5.19483189,   5.22795925,   5.7913267 ,   6.42905174,
          9.03617184],
       [ -0.38163035,   2.40433224,  18.86634163,   6.65049122,
          6.61327344,   5.97315513,   5.1575124 ,   4.92143689,
          5.09521127,   5.32707419,   5.75115509,   6.38360725,   9.9083797 ],
       [ 10.07445481,  19.44359465,   6.55125528,   6.89868894,
          5.65185827,   4.75213605,   4.91526098,   4.96731359,
          5.01964465,   5.24425014,   5.99506687,   6.89734303,
         10.75461418],
       [  9.97165547,   9.15363547,   6.68313561,   5.56277541,
          4.60627259,   4.95242333,   4.69222424,   4.73058477,
          5.12110416,   5.57526618,   6.39084185,   7.30261396,
         12.46175691],
       [  9.9303314 ,   6.36670231,   5.55203803,   4.59031943,
          4.93896018,   4.50664514,   4.57858757,   5.01664035,
          5.30683619,   5.76507346,   6.81759686,   8.16935719,
         14.78858458],
       [  8.76319561,   5.45725719,   4.96697534,   4.61808969,
          4.48857161,   4.39788663,   5.13063774,   4.87186923,
          5.61402123,   6.26199508,   7.72233302,   9.05747554,  18.820353  ],
       [  6.56936328,   5.03774515,   4.54138811,   4.43024073,
          4.51000354,   4.80159562,   4.83752545,   5.31459691,
          6.40925494,   6.56608629,   8.8800113 ,  10.73165193,
         18.70282158],
       [  5.4019207 ,   4.5998015 ,   4.48081533,   4.54080049,
          4.61189354,   4.78229891,   5.2674646 ,   6.12157548,
          6.31483054,   8.2109428 ,  10.61787265,  15.64150529,
         17.77018455],
       [  4.72682337,   4.5899158 ,   4.43492362,   4.49216778,
          4.80727134,   5.34127816,   5.81922704,   6.19952904,
          7.95477993,  10.28938934,  10.82445222,  30.76972908,
         17.01830421],
       [  4.48343715,   4.40355544,   4.51672977,   4.88809456,
          5.19415102,   5.58530237,   6.43036246,   8.02937286,
          9.5458969 ,  10.40224025,  27.90572872,   6.63586   ,
          3.43044183],
       [  4.00171272,   4.79633417,   4.88236268,   5.08041578,
          5.61546077,   6.6777742 ,   7.90866578,   9.03887483,
         13.68124401,  27.839641  ,  12.09517981,   0.77444562,
          3.43044183],
       [  4.70564855,   4.89906491,   4.87789035,   5.99288054,
          6.89906542,   7.7208359 ,   9.26652703,  17.15003713,
         12.28371379,   8.02933814,   4.08724772,   0.77444562,
          3.43044183]]
)


if __name__ == "__main__":
    test_2d_backproject()
