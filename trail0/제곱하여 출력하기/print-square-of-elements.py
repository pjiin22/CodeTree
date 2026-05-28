N = int(input())
num = list(map(int, input().split()))

for i in range(N):
    print(num[i]**2, end = " ")