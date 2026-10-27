import sys
input = sys.stdin.readline

def n_op():
    l, r= input().strip().split()
    l, r = int(l), int(r)
    x = 0
    return x
    
t = int(input())
out = []
for _ in range(t):
    out.append(str(n_op()))

print("\n".join(out))