n=int(input())
s=0
k=0
for i in range(1,n+1):
    s=s+(i*i)
for i in range(1,n+1):
    k=k+i
l=k**2
d=l-s
print(d)