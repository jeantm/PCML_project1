# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    # Initialization variables
    poly = np.zeros(shape=(len(x),degree+1))
    
    # for set of date
    for m in range(0,len(x)):
        for j in range(0,degree+1):
            poly[m,j] = np.power(x[m],j)
    
    return poly