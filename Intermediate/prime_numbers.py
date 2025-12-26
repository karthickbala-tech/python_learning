#Find all prime numbers between 1 and 100
'''n=2
primes=[]
while len(primes) < 100:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        primes.append(n)
    n += 1

print(primes)
'''
k=[]
for i in range(2,101):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime==True:
        k.append(i)
print(k)
            