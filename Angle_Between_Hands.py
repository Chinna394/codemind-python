n=input()
n=n.split(":")
n[0]=int(n[0])
n[1]=int(n[1])
h=(n[0]*30)+(n[1]/2)
m=(n[1]*6)
c=abs(h-m)
d=abs(360-c)
if c<d:
    print(c)
else:
    print(d)