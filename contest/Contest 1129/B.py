import sys
input = sys.stdin.readline

def max_seq():
    l = input().strip()
    l = int(l)
    arr = [int(n) for n in input().split()]
    return l * any(n < l for n in arr)
    
t = int(input())
out = []
for _ in range(t):
    out.append(str(max_seq()))

print("\n".join(out))