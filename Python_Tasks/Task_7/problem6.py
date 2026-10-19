
# Problem 6: Pangrams
# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem

import string

s = input().lower()

if set(string.ascii_lowercase).issubset(set(s)):
    print("pangram")
else:
    print("not pangram")
