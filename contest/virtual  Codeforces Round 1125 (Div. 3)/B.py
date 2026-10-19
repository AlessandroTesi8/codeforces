import sys
input = sys.stdin.readline

def not_printed():
    n = int(input())
    commands = input()
    printed = set()
    stack = []
    for i, command in enumerate(commands, start = 1):
        if command == '1':
            stack.append(i)
        elif command == '2':
            if stack:
                printed.add(stack.pop())
            else:
                printed.add(i)
        else:
            printed.add(i)

    not_printed_set = set(range(1, n + 1)) - printed
    res = []
    for v in not_printed_set:
        res.append(str(v))
    return str(len(not_printed_set)) + '\n' + ' '.join(res)



t = int(input())
out = []
for _ in range(t):
    out.append(str(not_printed()))

print("\n".join(out))