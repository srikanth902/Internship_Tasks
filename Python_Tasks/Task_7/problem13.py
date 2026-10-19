
# Problem 13: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-the-valid-string/problem

from collections import Counter

s = input().strip()
counts = list(Counter(s).values())
freq = Counter(counts)

if len(freq) == 1:
    print("YES")

elif len(freq) == 2:
    (f1, n1), (f2, n2) = freq.items()

    if (f1 == 1 and n1 == 1) or (f2 == 1 and n2 == 1):
        print("YES")

    elif abs(f1 - f2) == 1 and (
        (f1 > f2 and n1 == 1) or
        (f2 > f1 and n2 == 1)
    ):
        print("YES")

    else:
        print("NO")

else:
    print("NO")
