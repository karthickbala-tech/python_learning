#Create a simplecalculator using functions (add, subtract, multiply, divide).
def add(m,n):
    print(a+b)
def sub(m,n):
    print(a-b)
def mul(m,n):
    print(a*b)
def div(m,n):
    print(a//b)
print("enter numbers:")
a=int(input())
b=int(input())
print("enter peration:(add,sub,mul,div)")
c=str(input())
if c == 'add':
    add(a,b)
elif c== 'sub':
    sub(a,b)
elif c== 'div':
    div(a,b)
elif c== 'mul':
    mul(a,b)