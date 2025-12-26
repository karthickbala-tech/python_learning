#Generate the first 10 Fibonacci numbers
n=10
a=0
b=1
print(a)
for i in range(n-1):
    print(b)
    c=a+b
    a=b
    b=c
    