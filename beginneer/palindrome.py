a=input("enter anything:")
rev=''
length=len(a)-1
while length>=0:
    rev+=a[length]
    length-=1
if a== rev:
    print("palindrome")
else:
    print('not palindrome')
#time complexit o(n*n)
#space complexity o(n)
#modified version 
a= input('type anything')
start=0
last=len(a)-1
palindrome=True
while start<last:
    if a[start] != a[last]:
        palindrome=False
        break
    start+=1
    last-=1
if palindrome==True:
    print("palindrome")
else:
    print(" not a palindrame")
#time:o(n)
#space:o(1)
