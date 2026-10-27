# !!! not working
import sys
from functools import cache
input = sys.stdin.readline

def f():
    n, x = input().strip().split()
    n, x = int(n), int(x)
    arr = [int(n) for n in input().split()]
    d = []
    for i in range(0, n - 1):
        d.append(arr[i + 1] - arr[i])

    l_b = 1
    u_b = max(d)
    max_moves =  x
    
    @cache
    def feasible(i: int, k: int, prev: bool) -> int: # fai il passo avanti solamente se costa meno di fare +1 e po +2
        moves = 0
        if i >= len(d): 
            return 0
        if i == len(d) - 1 :
            return ((d[i] - 1) // k) 
        if not prev: 
            moves += ((d[i] - 1) // k) + feasible(i + 1, k, True)
        else:
            moves += min(((d[i] - 1) // k + 1) + feasible(i + 1, k, True), feasible(i + 1, k, False))
        return moves

    #. between 0 and 1 is mandatory
    #print(f'arr: {arr}, d {d}, max moves: {max_moves}')
    while l_b < u_b: # u_b must remain feasible
        k = (u_b + l_b) // 2
        moves = feasible(0, k, False)
        print(f'k: {k}, moves: {moves}')
        if moves > max_moves:
            l_b = k + 1
        else:
            u_b = k
    return u_b
    
t = int(input())
out = []
for _ in range(t):
    out.append(str(f()))

print("\n".join(out))