n=int(input())
a,b=0,1
cnt=0
for i in range(1,n+1):
    c=a+b
    if c==n:
        cnt=cnt+1
        break
    a=b
    b=c
if cnt==0:
    print("False")
else:
    print("True")