n=int(input())
add=0
while n>0:
    r=n%10
    add=add+r
    n=n//10
    if add>9 and n==0:
        n=add
        add=0
print(add)