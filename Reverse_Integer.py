n=int(input())
s=0
flag=0
if(n<0):
    flag=1
    n=n*-1

while(n!=0):
    r=n%10
    s=s*10+r
    n//=10
if(flag==1):
    print(s*-1)
else:
    print(s)
        

