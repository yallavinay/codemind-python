l=int(input())
u=int(input())
for i in range(l,u+1):
    q=i
    c=0
    tc=0
    while q!=0:
        c=c+1
        r=q%10
        if r!=0 and i%r==0:
            tc=tc+1
        q=q//10
    if c==tc:
        print(i,end=" ")
       