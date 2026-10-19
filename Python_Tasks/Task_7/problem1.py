
# Problem 1: Set .symmetric_difference() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    set_n = set(map(int, input().split()))

    m = int(input())
    set_m = set(map(int, input().split()))

    result = set_n.symmetric_difference(set_m)
    print(len(result))
