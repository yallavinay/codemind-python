n=int(input())
flag=0
while(n!=0):
    if n%2==0:
        n//=2
    elif n%3==0:
        n//=3
    elif n%5==0:
        n//=5
    else:
      flag=1
      break
if flag==1 and n==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")