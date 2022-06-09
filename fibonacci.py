def fib(c):
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,c):
        d=a+b
        a=b
        b=d
        print(d,end=" ")
n=int(input())
fib(n)
    