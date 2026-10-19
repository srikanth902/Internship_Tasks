
# Problem 8: Gemstones
# HackerRank: https://www.hackerrank.com/challenges/gem-stones/problem

if __name__ == '__main__':
    n = int(input())
    common = set(input().strip())

    for _ in range(n - 1):
        common = common.intersection(set(input().strip()))

    print(len(common))
