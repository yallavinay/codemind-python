n=int(input())
q=(n*n)
s=0
while q!=0:
    r=q%10
    s=s+r
    q=q//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")