#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    return sum(p // 2 for p in set(ar.count(i) for i in ar))
    #return sum(p // 2 for p in set(ar.count(i) for i in ar))
    #return sum(set(ar.count(i) // 2 for i in ar))


if __name__ == '__main__':
    #print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
    print(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))
