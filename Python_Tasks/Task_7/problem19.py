
# Problem 19: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

if __name__ == '__main__':
    s = input().strip()
    n = int(input())

    weights = set()
    previous = ''
    current = 0

    for char in s:
        if char == previous:
            current += ord(char) - ord('a') + 1
        else:
            current = ord(char) - ord('a') + 1
            previous = char

        weights.add(current)

    for _ in range(n):
        x = int(input())
        print("Yes" if x in weights else "No")
