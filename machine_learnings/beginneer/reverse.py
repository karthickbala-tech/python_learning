#reverse astring(eg.'hello'-> 'olleh')
a=str(input("Enter a string:"))
rev=[]
i=len(a)-1
while i>=0:
    rev.append(a[i])
    i-=1
print("".join(rev))
    
a = list(input("Enter a string:"))
start = 0
end = len(a) - 1

while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1

print("".join(a))