import sys
input = sys.stdin.readline

def find_point():
    # simple sol, move R step to right
    x, y, r = map(int, input().split())
    return x + r, y

t = int(input())
out = []
for _ in range(t):
    x, y = find_point()
    out.append(f'{x} {y}')

print("\n".join(out))