#
# Copyright 2018 Ettus Research, a National Instruments Company
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""
Gain table constants for Rhodium
"""

###############################################################################
# Constants
###############################################################################

# Rhodium has two configurable gain elements
# DSA1 - 0-30, attenuation
# DSA2 - 0-30, attenuation
# Gain table values are written as [DSA1, DSA2]
# This is stored as a gain table, so index 0 is the lowest available power
# These default gain tables have 61 indices

RX_LOWBAND_GAIN_TABLE = [
    [30, 30],
    [29, 30],
    [28, 30],
    [27, 30],
    [26, 30],
    [25, 30],
    [24, 30],
    [23, 30],
    [22, 30],
    [21, 30],
    [20, 30],
    [19, 30],
    [18, 30],
    [17, 30],
    [16, 30],
    [15, 30],
    [14, 30],
    [13, 30],
    [12, 30],
    [11, 30],
    [10, 30],
    [ 9, 30],
    [ 9, 29],
    [ 8, 29],
    [ 8, 28],
    [ 7, 28],
    [ 7, 27],
    [ 6, 27],
    [ 6, 26],
    [ 5, 26],
    [ 5, 25],
    [ 5, 24],
    [ 5, 23],
    [ 5, 22],
    [ 5, 21],
    [ 5, 20],
    [ 5, 19],
    [ 5, 18],
    [ 5, 17],
    [ 5, 16],
    [ 5, 15],
    [ 4, 15],
    [ 4, 14],
    [ 3, 14],
    [ 3, 13],
    [ 2, 13],
    [ 2, 12],
    [ 1, 12],
    [ 1, 11],
    [ 0, 11],
    [ 0, 10],
    [ 0,  9],
    [ 0,  8],
    [ 0,  7],
    [ 0,  6],
    [ 0,  5],
    [ 0,  4],
    [ 0,  3],
    [ 0,  2],
    [ 0,  1],
    [ 0,  0]]

RX_HIGHBAND_GAIN_TABLE = [
    [30, 30],
    [29, 30],
    [28, 30],
    [27, 30],
    [26, 30],
    [25, 30],
    [24, 30],
    [23, 30],
    [22, 30],
    [21, 30],
    [20, 30],
    [19, 30],
    [18, 30],
    [17, 30],
    [16, 30],
    [15, 30],
    [14, 30],
    [13, 30],
    [12, 30],
    [11, 30],
    [10, 30],
    [ 9, 30],
    [ 8, 30],
    [ 7, 30],
    [ 7, 29],
    [ 6, 29],
    [ 5, 29],
    [ 5, 28],
    [ 4, 28],
    [ 3, 28],
    [ 3, 27],
    [ 2, 27],
    [ 2, 26],
    [ 2, 25],
    [ 1, 25],
    [ 1, 24],
    [ 1, 23],
    [ 0, 23],
    [ 0, 22],
    [ 0, 21],
    [ 0, 20],
    [ 0, 19],
    [ 0, 18],
    [ 0, 17],
    [ 0, 16],
    [ 0, 15],
    [ 0, 14],
    [ 0, 13],
    [ 0, 12],
    [ 0, 11],
    [ 0, 10],
    [ 0,  9],
    [ 0,  8],
    [ 0,  7],
    [ 0,  6],
    [ 0,  5],
    [ 0,  4],
    [ 0,  3],
    [ 0,  2],
    [ 0,  1],
    [ 0,  0]]

TX_LOWBAND_GAIN_TABLE = [
    [30, 30],
    [29, 30],
    [29, 29],
    [28, 29],
    [28, 28],
    [27, 28],
    [27, 27],
    [26, 27],
    [26, 26],
    [25, 26],
    [25, 25],
    [24, 25],
    [24, 24],
    [23, 24],
    [23, 23],
    [22, 23],
    [22, 22],
    [21, 22],
    [21, 21],
    [20, 21],
    [20, 20],
    [19, 20],
    [19, 19],
    [18, 19],
    [18, 18],
    [17, 18],
    [17, 17],
    [16, 17],
    [16, 16],
    [15, 16],
    [15, 15],
    [14, 15],
    [14, 14],
    [13, 14],
    [13, 13],
    [12, 13],
    [12, 12],
    [11, 12],
    [11, 11],
    [10, 11],
    [10, 10],
    [ 9, 10],
    [ 9,  9],
    [ 8,  9],
    [ 8,  8],
    [ 7,  8],
    [ 7,  7],
    [ 6,  7],
    [ 6,  6],
    [ 5,  6],
    [ 5,  5],
    [ 4,  5],
    [ 4,  4],
    [ 3,  4],
    [ 3,  3],
    [ 2,  3],
    [ 2,  2],
    [ 1,  2],
    [ 1,  1],
    [ 0,  1],
    [ 0,  0]]

TX_HIGHBAND_GAIN_TABLE = [
    [30, 30],
    [29, 30],
    [29, 29],
    [28, 29],
    [28, 28],
    [27, 28],
    [27, 27],
    [26, 27],
    [26, 26],
    [25, 26],
    [25, 25],
    [24, 25],
    [24, 24],
    [23, 24],
    [23, 23],
    [22, 23],
    [22, 22],
    [21, 22],
    [21, 21],
    [20, 21],
    [20, 20],
    [19, 20],
    [19, 19],
    [18, 19],
    [18, 18],
    [17, 18],
    [17, 17],
    [16, 17],
    [16, 16],
    [15, 16],
    [15, 15],
    [14, 15],
    [14, 14],
    [13, 14],
    [13, 13],
    [12, 13],
    [12, 12],
    [11, 12],
    [11, 11],
    [10, 11],
    [10, 10],
    [ 9, 10],
    [ 9,  9],
    [ 8,  9],
    [ 8,  8],
    [ 7,  8],
    [ 7,  7],
    [ 6,  7],
    [ 6,  6],
    [ 5,  6],
    [ 5,  5],
    [ 4,  5],
    [ 4,  4],
    [ 3,  4],
    [ 3,  3],
    [ 2,  3],
    [ 2,  2],
    [ 1,  2],
    [ 1,  1],
    [ 0,  1],
    [ 0,  0]]
