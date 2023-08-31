a,b,c=map(int,input().split())
if a>c and b>c:
    print(a+b)
elif b>a and c>a:
    print(b+c)
else:
    print(c+a)