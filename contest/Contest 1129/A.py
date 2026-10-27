import sys
input = sys.stdin.readline

def mex():
    l, max_size = input().strip().split()
    l, max_size = int(l), int(max_size)
    arr = [int(n) for n in input().split()]
    arr.sort()
    min_find  = i = max_size - 1
    i = min_find
    curr = 0
    while i < l:
        if arr[i] > curr:
            return curr
        elif arr[i] < curr:
            i += 1
        elif arr[i] == curr:
            curr += 1
            i += 1
            min_find += max_size
            i = max(i, min_find)
    return curr
    
t = int(input())
out = []
for _ in range(t):
    out.append(str(mex()))

print("\n".join(out))