N, M = map(int, input().split())

# Please write your code here.

while True:
    print(N)
    N //= M

    if N ==0:
        break