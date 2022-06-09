n=int(input())
temp=n
x=n
count=0
while temp>0:
    temp=temp//10
    count=count+1
sum=0
while x>0:
    r=x%10
    sum=sum+r**count
    x=x//10
    count=count-1
if sum==n:
    print("True")
else:
    print("False")