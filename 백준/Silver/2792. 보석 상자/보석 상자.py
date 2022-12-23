import sys
import math

input = sys.stdin.readline
N, M = map(int, input().split())
gems = [int(input()) for _ in range(M)]


def validate(n):
    if not n:
        return False
    count = sum(math.ceil(i / n) for i in gems)
    return count <= N


jump = max(gems)
result = jump + 1

while True:
    if jump == 0:
        break
    if validate(result - jump):
        result -= jump
    else:
        jump //= 2

print(result)
