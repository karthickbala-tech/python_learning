#Find all prime numbers between 1 and 100
n=2
prime=[]
while len(prime)<100:
    count=0
    for i in range (1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        prime.append(n)
    n+=1
print(prime)
    
