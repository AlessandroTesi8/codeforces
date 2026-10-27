# must find same frogs in columns and rows
import sys
input = sys.stdin.readline

def min_k():
    l = input().strip()
    l = int(l)
    first_row = input().strip()
    second_row = input().strip()
    return (first_row.count('f') + second_row.count('f')) & 1
    
t = int(input())
out = []
for _ in range(t):
    out.append(str(min_k()))

print("\n".join(out))