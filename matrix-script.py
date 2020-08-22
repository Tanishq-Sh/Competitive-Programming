#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

com = str()
for p in range(m):
    for q in range(n):
        com = com + matrix[q][p]

try:
    x = re.search("[a-zA-Z0-9]", com)
    y = re.search("[a-zA-Z0-9]", com[::-1])

    beg = com[:x.start()]
    end = com[len(com) - y.start() - 1 :]
    mid = com[x.start() : len(com) - y.start()]

    mid = re.sub("[!@#$%&]", ' ', mid)
    mid = ' '.join(mid.split())
    print(beg+mid+end)

except:
    print(com)

