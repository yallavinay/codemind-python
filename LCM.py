a,b=map(int,input().split())
if a>b:
    max=a
else:
    max=b
while(1):
    if(max%a==0 and max%b==0):
        print(max)
        break
    max=max+1