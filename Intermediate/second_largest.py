#Find the second largest number in a list.
l=[32,45,53,23,56,25,10]
last=len(l)
i=0
while i<last:
    j=0
    while j<(last-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
        j+=1
    i+=1
    
print(l[1])