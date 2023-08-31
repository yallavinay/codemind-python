a,b,t,f=map(int,input().split())
s=0
for i in range(a,b+1):
    if i%t==0 and i%f!=0:
        s=s+i
print(s)