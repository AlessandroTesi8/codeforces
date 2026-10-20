# Main idea:
# borders left and top are reachable, all points are reachable if its right one or top one 
# is reachable, if you find a non reachable point return False
# you can simply traverse the matrix and keep a set of reachable, but since you are traversing
# you can simply keep only one row, making time O(m n) space O(m + n)
# m and n dimensions are swapped wrt problem description

import sys
input = sys.stdin.readline

def reproducible():
    m, n = map(int, input().split())
    # build the matrix
    matrix = []
    for _ in range(m):
        r = input()
        matrix.append([int(v) for v in r.strip()])
    correct_col = [1] * n
    for i in range(m):
        correct_row = True
        for j in range(n):
            if matrix[i][j]:
                if not(correct_row or correct_col[j]):
                    return False
            else:
                correct_row = False
                correct_col[j] = 0
    return True


t = int(input())
out = []
for _ in range(t):
    out.append('Yes' if reproducible() else 'No')
print('\n'.join(out))