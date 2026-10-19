
# Problem 17: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for i in range(1, len(s)):
        first = int(s[:i])
        current = first
        result = str(current)

        while len(result) < len(s):
            current += 1
            result += str(current)

        if result == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        s = input().strip()
        separateNumbers(s)
