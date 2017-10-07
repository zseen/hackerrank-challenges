#!/bin/python3

import sys


sys.stdin = open('climbingTheLeaderboard_input.txt')
n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here

def rank(scores, alice,n):
    sorted(scores)
    scoresUniqueForRank = []
    for i in range(0,n):
        if scores[i-1] != scores[i]:
            scoresUniqueForRank.append(scores[i])

    for item in alice:
        scoresUniqueForRank.append(item)
        y = sorted(scoresUniqueForRank, key=int)
        y.reverse()
        x = y.index(item)
        print(x+1)



rank(scores, alice,n)