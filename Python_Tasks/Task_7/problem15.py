
# Problem 15: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

s = input().strip()
odd = sum(count % 2 for count in Counter(s).values())

if odd <= 1:
    print("YES")
else:
    print("NO")
