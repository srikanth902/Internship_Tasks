
# Problem 7: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/py-alphabet-rangoli/problem

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alpha[size - 1:size - i - 1:-1]
        right = alpha[size - i:size]
        row = '-'.join(left + right)
        lines.append(row.center(4 * size - 3, '-'))

    rangoli = lines[::-1] + lines[1:]
    return '\n'.join(rangoli)


if __name__ == '__main__':
    n = int(input())
    print(print_rangoli(n))
