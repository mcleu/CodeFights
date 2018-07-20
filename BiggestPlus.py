# Given a matrix of integers, your task is to find the biggest plus (+) shape formed by adjacent equal numbers.
# More formally, the size of the plus is based on the distance from its centre to its shortest arm.
# For example, the plus formed by the 2's below would have a size of 1, even though one of its arms extends further.
# [[1,0,2,3],
#  [2,2,2,2],
#  [4,3,2,5]]
# Specifically, we would like to find the coordinates of the center of the biggest plus (row index and column index).
# If there is more than one biggest plus, return the coordinates with the smallest row index;
# if there is more than one biggest plus with the same row indices, return the coordinates with the smallest column index.
# 
# Input / Output
# [execution time limit] 4 seconds (py3)
# [input] array.array.integer arr
# A rectangular matrix of whole numbers
# Guaranteed constraints:
# 1 ≤ arr.length ≤ 500,
# 1 ≤ arr[i].length ≤ 500,
# 0 ≤ arr[i][j] ≤ 10.
# [output] array.integer
# A 2-element array consisting of the row index and column index of the center of the biggest plus made up of equal numbers.

import numpy as np

def biggestplus(A):
    wx,wy = 0,0
    cm = 0
    NA = np.array(A)
    [nx, ny] = np.shape(NA)
    for x in range(1,nx-1):
        for y in range(1,ny-1):
            m = sizeplus(NA,x,y,nx,ny)
            if m > cm:
                cm = m
                wx,wy = x,y
    return wx,wy

def sizeplus(A, x, y, nx, ny):
    B = A[x,y]
    s = 0
    try: 
        for nn in range(len(A)) :
            m = s+1
            L = get(A,x-m,y,nx,ny)
            R = get(A,x+m,y,nx,ny)
            U = get(A,x,y-m,nx,ny)
            D = get(A,x,y+m,nx,ny)
            if (B==L==R==U==D):
                s += 1
                continue
            else:
                break
    except:
        pass
    return s

def get(A,x,y,nx,ny):
    if (x<0) or (y<0) or (x>=nx) or (y>=ny):
        raise IndexError()
    else:
        return A[x,y]
