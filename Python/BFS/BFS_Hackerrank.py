#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
def bfs(n, m, edges, s):









if __name__ == '__main__':
    sys.stdin = open('BFS_Hackerrank_input.txt')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        edges = []
        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))
        s = int(input())
        result = bfs(n, m, edges, s)
        print(result)

