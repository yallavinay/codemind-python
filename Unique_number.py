n=int(input())
l=[]
flag=0
while(n!=0):
    r=n%10
    if r not in l:
        l.append(r)
    else:
        flag = 1
    n //= 10
if flag==1:
    print("Not Unique Number")
else:
    print("Unique Number")
