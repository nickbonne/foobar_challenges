#!/usr/bin/env python 
from itertools import permutations

'''
Find largest number divisible by 3 possible using list of 
integers as function arg.

ex) [1,2,3,4,5,6,7,8,9]

answer = 987654321

987654321 / 3  = 329218107

'''

def answer(l):

    l = sorted(l, reverse=True)
    num = ''.join(map(str,l))

    if int(num) % 3 == 0:
        return num

    if l == [3]:
        return 3

    for i in range(len(l), 1, -1):
        try: 
            return max([int(''.join(e)) for e in [list(x) for x in permutations(num, i)] if int(''.join(e)) % 3 == 0])
        except Exception:
            pass

    return 0

