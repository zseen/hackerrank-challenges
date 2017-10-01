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
    print(scores)
    scoresUniqueForRank = []
    for i in range(0,n):
        if scores[i-1] != scores[i]:
            scoresUniqueForRank.append(scores[i])
    print(scoresUniqueForRank)
    print(alice)

    for item in alice:
        for i in range(0,n):
            scoresUniqueForRank.insert(scoresUniqueForRank[i+1], item)
            print(scoresUniqueForRank)

rank(scores, alice,n)