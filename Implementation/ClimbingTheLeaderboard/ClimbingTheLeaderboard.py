#!/bin/python3

import sys


def getRank(scores, aliceScores):
    aliceRank = []
    scoresUniqueList = sorted(set(scores))
    scoresIndex = 0

    for item in aliceScores:
        while scoresIndex < len(scoresUniqueList) and scoresUniqueList[scoresIndex] <= item:
            scoresIndex += 1
        aliceRank.append(len(scoresUniqueList) - scoresIndex + 1)

    return aliceRank


def main():
    sys.stdin = open('ClimbingTheLeaderboard_input.txt')
    n = int(input().strip())
    scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
    m = int(input().strip())
    alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
    alicePosition = getRank(scores,alice)
    print(*alicePosition, sep='\n')

if __name__ == "__main__":
    main()
