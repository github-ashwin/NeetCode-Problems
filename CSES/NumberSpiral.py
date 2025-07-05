import sys

input = sys.stdin.readline

t = int(input().strip())
output = []
for _ in range(t):
    y,x = map(int,input().strip().split())
    n = max(x,y)
    if n % 2 == 0:
        if y == n:
            ans = n * n - x + 1
            output.append(ans)
        else:
            ans = (n - 1) * (n - 1) + y
            output.append(ans)
    else:
        if x == n:
            ans = n * n - y + 1
            output.append(ans)
        else:
            ans = (n - 1) * (n - 1) + x
            output.append(ans)

for i in range(t):
    print(output[i])

    