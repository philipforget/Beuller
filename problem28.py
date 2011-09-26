import sys

__problem__ = """
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?

1.3.5.7.9...13...17...21...25 // .....31.....37.....43
"""


class Main():
    def __init__(self):
        rows = int(sys.argv[1])
        total, current = 1, 1
        for i in range(rows / 2):
            for j in range(4):
                current += 2 * (i+1)
                total += current

        print total


if __name__ == '__main__':
    Main()
