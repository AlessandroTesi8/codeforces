import sys
input = sys.stdin.readline

def n_sandwitches():
    a, b = (input().strip()).split()
    a, b = int(a), int(b)
    if b >= a: 
        return -1
    return min(b, a - b)

t = int(input())
out = []
for _ in range(t):
    out.append(str(n_sandwitches()))

print("\n".join(out))