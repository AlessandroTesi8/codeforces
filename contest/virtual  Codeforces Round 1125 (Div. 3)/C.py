import sys
from collections import Counter
input = sys.stdin.readline

def pairs():
    # guardi i seguenti della lista di hash sum e poi fai la combinazione - n conflitti
    l = int(input())
    arr = list(int(n) for n in input().split())
    sums = [arr[i] + arr[i + 2] - arr[i + 4] for i in range(l - 4)]
    hash_sums = Counter()
    res = 0
    conflicts = 0
    for i in range(len(sums)):
        hash_sums[sums[i]] += 1
        if i > 1:
            conflicts += sums[i] == sums[i - 2]
        if i > 3:
            conflicts += sums[i] == sums[i - 4]

    for same_love in hash_sums.values():
        res += (same_love * (same_love - 1) // 2)
    return res - conflicts



t = int(input())
out = []
for _ in range(t):
    out.append(str(pairs()))

print("\n".join(out))