n=int(input())
s=0
q=n
while(q!=0):
    r=q%10
    s=s*10+r
    q //=10
if(s==n):
    print("Palindrome")
else:
    print("Not Palindrome")