
# Problem 3: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

if __name__ == '__main__':
    s = input().strip()
    original = "SOS"
    changed = 0

    for i, char in enumerate(s):
        if char != original[i % 3]:
            changed += 1

    print(changed)
