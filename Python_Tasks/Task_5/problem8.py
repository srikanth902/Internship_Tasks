
# Problem 8: Set .add()
# HackerRank:
# https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == '__main__':
    n = int(input())
    country_stamps = set()

    for _ in range(n):
        country = input().strip()
        country_stamps.add(country)

    print(len(country_stamps))
