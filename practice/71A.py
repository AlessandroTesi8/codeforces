import sys
input = sys.stdin.readline

def too_long():
    w = input().strip()
    l = len(w)
    return w if l <= 10 else w[0] + str(l - 2) + w[-1]

t = int(input())
out = []
for _ in range(t):
    out.append(too_long())

print("\n".join(out))