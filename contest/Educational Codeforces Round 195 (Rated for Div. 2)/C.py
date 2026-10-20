# idea: make an array of modulo k's, then use a sliding window, while passing 
# from left you add the modulo to a counter, when going to right you add to the res
# the counter corresponding value
import sys
from collections import defaultdict
input = sys.stdin.readline

def n_subarrays():
    l, k = input().strip().split()
    l, k = int(l), int(k)
    arr = [int(n) for n in input().strip().split()]
    arr[0] = arr[0] % k
    counter = [1] + [0] * (k - 1)
    for i in range(1, l):
        arr[i] = (arr[i - 1] + arr[i] ) % k
    res = 0
    for i in range(k, l):
        res += counter[arr[i]]
        counter[arr[i - k]] += 1
    return res


t = int(input())
out = []
for _ in range(t):
    out.append(str(n_subarrays()))
print('\n'.join(out))