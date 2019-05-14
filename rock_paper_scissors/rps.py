#!/usr/bin/python

import sys

possible_plays = ["Rock", "Paper", "Scissors"]
combination = []
result = []


def rock_paper_scissors(n):
    if n == 0:
        return result
    else:
        for i in range(len(possible_plays)):
            for j in range(len(possible_plays)):
                combination = [possible_plays[i] + ", " + possible_plays[j]]
                result.append(combination)

    return result


print(rock_paper_scissors(1))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
