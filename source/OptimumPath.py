import sys

sys.stdin = open('input.txt', 'r')


T = int(input())

for test_case in range(1, T + 1):
    company = list(map(int, input.split()))
    home = list(map(int, input.split()))

    customer = [list(map(int, input.split()))] for _ in range(N)
