# idea: you can either do nothing, merge 2 or split 2

import sys
input = sys.stdin.readline

def n_transformations():
    s = input().strip()
    mergable = 0
    splittable = 0
    for i in range(1, len(s) - 1):
        if s[i] == s[i - 1] == s[i + 1]:
            splittable = 1
        if s[i] != s[i - 1] == s[i + 1]:
            mergable = 1
    return 1 + splittable + mergable

t = int(input())
out = []
for _ in range(t):
    out.append(str(n_transformations()))

print("\n".join(out))