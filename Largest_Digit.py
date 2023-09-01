n=int(input())
l=0
while(n!=0):
    r=n%10
    l=max(r,l)
    n=n//10
print(l)