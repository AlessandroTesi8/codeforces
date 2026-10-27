# idea:
# take the smallest value missing up to arr[:- k ]
# so for example if arr[-k] il len 3, we should bring in the smallest
# value less than 3. if 0, 1, 2 are present we return -1.


import sys
input = sys.stdin.readline

def swap():
    l, k = input().strip().split()
    l, k = int(l), int(k)
    arr = [int(n) for n in input().split()]
    n_present = [0] * (l - k + 1)
    to_swap_with = None
    for i, n in enumerate(arr[ : l - k + 1]):
        if n < len(n_present):
            n_present[n] = 1
        else:
            if to_swap_with is None:
                to_swap_with = i
    if all(n for n in n_present): return -1

    v = None
    for i in range(len(n_present)):
        if not n_present[i]:
            v = i
            break
    swap_idx = arr.index(v) 
    return f'{to_swap_with + 1} {swap_idx + 1}'
    
t = int(input())
out = []
for _ in range(t):
    out.append(str(swap()))

print("\n".join(out))