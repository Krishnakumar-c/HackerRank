#!/bin/python3

import sys


N = int(input().strip())
if N % 2 != 0:
    print("Weird")
elif(N%2 == 0 and N in range(1,5)):
    print("Not Weird")
elif(N%2 ==0 and N in range(5,20)):
    print("Weird")
elif(N%2 == 0 and N > 20):
    print("Not Weird")
