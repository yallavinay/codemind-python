n=int(input())
h=(n//3600)
m=(n-(3600*h))//60
s=(n-(3600*h)-(m*60))
print(f"H:M:S-{h}:{m}:{s}")