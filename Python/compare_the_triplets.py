#!/bin/python3

import sys

def solve(a,b):
    A = B =0
    for x in range(3):
        if a[x] > b[x]:
            A = A + 1
        elif a[x] < b [x]:
            B = B + 1
    result = str(A) + ' ' + str(B)
    return(result)

a0, a1, a2 = input().strip().split(' ')
a = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b = [int(b0), int(b1), int(b2)]
result = solve(a,b)
print(result)