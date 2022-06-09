n=int(input())
temp=n
a=0
while temp>0:
    r=temp%10
    temp=temp//10
    if r>a:
        a=r
print(a)