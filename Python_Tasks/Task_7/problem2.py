
# Problem 2: The Captain's Room
# HackerRank: https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == '__main__':
    k = int(input())
    room_numbers = list(map(int, input().split()))

    unique_rooms = set(room_numbers)
    captain_room = (sum(unique_rooms) * k - sum(room_numbers)) // (k - 1)

    print(captain_room)
