#!/bin/python3

import math
import os
import random
import re
import sys


def max_and(n, k):
    print(f"n: {n} k: {k}")
    # if math.log(k, 2) - math.floor(math.log(k, 2)) == 0:
    #     # k is even pow of 2
    if k == 2:
        if n == 2:
            return 0
        return 1
    #     else:
    #         a = k
    #         b = a - 1
    #         return(max(a & b, (a - 1) & (b - 1)))
    # else:
    #     a = max(k + 1, n)
    #     b = a - 2
    #     return(a & b)
    res = k & (k - 1)
    # original (off by 1 error in range function d'oh):
    # for a in range(k - 2, n - 1):
    #     for b in range(a + 1, n):
    # fix after local debugging:
    for a in range(k - 2, n):
        for b in range(a + 1, n + 1):
            # for a in range(k - 20, n):
            #     for b in range(a + 1, n + 1):
            c = a & b
            print(f"a:{a} b:{b} c:{c}")
            if c > res and c < k:
                res = c

    return(res)


if __name__ == '__main__':
    nk = [sys.argv[1], sys.argv[2]]

    n = int(nk[0])

    k = int(nk[1])
    print(max_and(n, k))
    print(f"n: {n} k: {k}")
