import sys
import math
input = sys.stdin.readline

def solution():
    l = int(input())
    arr = map(int, input().split())
    hash_phases = {}
    res = 0
    squares_sum = lambda n : sum(int(d) ** 2 for d in str(n))

    for _ in range(l):
        n = next(arr)
        evolution = []
        seen = set()

        while n not in seen:
            evolution.append(n)
            seen.add(n)
            n = squares_sum(n)

        cycle = evolution[evolution.index(n):]
        phase = len(evolution) % len(cycle)
        count = hash_phases.get(cycle[-phase], 0)
        hash_phases[cycle[-phase]] = count + 1
    for v in hash_phases.values():
        res += math.comb(v, 2)
    return res
        



t = int(input())
out = []
for _ in range(t):
    out.append(str(solution()))
print('\n'.join(out))