A, B, C = map(int,input().split())

if A<B and C<B:
    if A < C:
        print(f"{C}")
    else:
        print(f"{A}")
elif A<B and B< C:
    print(f"{B}")
elif C<B and B<A:
    print(f"{B}")
else:
    if A<C:
        print(f"{A}")
    else:
        print(f"{C}")
