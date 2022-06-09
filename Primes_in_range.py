def prime(n):
    if n==1:
        return False
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return False
    else:
        return True
x=int(input())
y=int(input())
c=0
for j in range(x,y+1):
    if prime(j):
               c=c+1
print(c)