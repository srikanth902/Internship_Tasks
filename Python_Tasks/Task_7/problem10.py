
# Problem 10: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()

words = 1 + sum(1 for char in s if char.isupper())

print(words)
