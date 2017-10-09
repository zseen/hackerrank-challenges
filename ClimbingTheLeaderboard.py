#!/bin/python3

import sys




def rank(scores, alice):
    sorted(scores)
    scoresUniqueForRank = set(scores)

    aliceRank = []

    for item in alice:
        scoresUniqueForRank.add(item)
        newScores = sorted(scoresUniqueForRank, key=int)
        newScores.reverse()
        position = newScores.index(item)
        aliceRank.append(position+1)

    return aliceRank


def main():
    sys.stdin = open('climbingTheLeaderboard_input.txt')
    n = int(input().strip())
    scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
    m = int(input().strip())
    alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
    alicePosition = rank(scores,alice)
    print(*alicePosition,sep='\n')

if __name__ == "__main__":
    main()
