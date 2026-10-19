
# Problem 18: String Construction
# HackerRank: https://www.hackerrank.com/challenges/string-construction/problem

if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        s = input().strip()
        print(len(set(s)))
