#!/bin/python

import math
import os
import random
import re
import sys

#Given an integer, 3, perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of 6 to 20, print Weird
#If  is even and greater than 20, print Not Weird

if __name__ == '__main__':
    n = int(raw_input().strip())
if n % 2 != 0:
     print('Weird')
elif n % 2 == 0 and n < 6:
    print('Not Weird')
elif n % 2 == 0 and n < 21:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')