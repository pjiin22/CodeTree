A,B = input().split()

if len(A) == len(B):
    print("same")
else:
    if len(A) > len(B):
        print(A, len(A), end = " ")
    else:
        print(B, len(B), end = " ")