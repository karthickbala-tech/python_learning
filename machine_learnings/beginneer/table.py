#print the multiplication table of a given number
mul=int(input("enter a multiplication number:"))
num=int(input("enter end serial number"))
for i in range(1,num+1):
    print(f"{i} * {mul} = {i*mul}")
