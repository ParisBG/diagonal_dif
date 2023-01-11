#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 07:57:12 2022
@author: parisbg

Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""
import numpy as np
    
#Determine size of 2d array
#Traverse the array summing necessary diagonal values
#pattern for diagonal_for would be start at arr[0][0] then m + 1 and n + 1 each iteration
#pattern for diagonal_bac would be start at arr[0][0] then m + 1 and n - 1 each iteration
#Running sum for each diagonal
#Subtract both diagonal sums
#return absolute value of result abs(my_num)

arr = np.array( [[1, 2, 3, 4], [5, 5, 6, 7], [1, 2, 3, 9], [8, 4, 5, 6]] )
diagonal_for = 0
diagonal_bac = 0
m,n = len(arr),len(arr[0])
#print('Rows =', m, 'Cols=', n)
for i in range(m):
    diagonal_for += arr[i][i]
    diagonal_bac += arr[i][(m-1)-i]

print( abs(diagonal_for - diagonal_bac) )




'''
2x2
diagonal1 = arr[0][0] + arr[1][1]
diagonal2 = arr[0][1] + arr[1][0]
1 2 
3 4 

3x3
diagonal1 = arr[0][0] + arr[1][1] + arr[2][2]
diagonal2 = arr[0][2] + arr[1][1] + arr[2][0]
1 2 3
4 5 6
9 8 9  

4x4
diagonal1 = arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3]
diagonal2 = arr[0][3] + arr[1][2] + arr[2][1] + arr[2][0]
1 2 3 4
1 2 3 4
5 6 7 8
9 1 2 3
4 5 6 7

'''