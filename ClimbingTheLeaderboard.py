#!/bin/python3

import sys


def getRank(scores, alice):
    
    scoresUniqueForRank = set(scores)

    aliceRank = []

    for item in alice:
        scoresUniqueForRank.add(item)
        newScores = sorted(scoresUniqueForRank, key=int)
        newScores.reverse()
        position = newScores.index(item)
        aliceRank.append(position+1)
        scoresUniqueForRank.remove(item)

    return aliceRank


def main():
    sys.stdin = open('climbingTheLeaderboard_input.txt')
    n = int(input().strip())
    scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
    m = int(input().strip())
    alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
    alicePosition = getRank(scores,alice)
    print(*alicePosition, sep='\n')

if __name__ == "__main__":
    main()
