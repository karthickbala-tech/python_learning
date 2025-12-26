List=[5,6,3,67,3,5,1]
last=len(List)
i=0
while i<last:
    j=0
    while j<last-1:
        if List[j]>List[j+1]:
            temp=List[j]
            List[j]=List[j+1]
            List[j+1]=temp
        j+=1
    i+=1
print(List)

List = [5, 6, 3, 67, 3, 5, 1]
last = len(List) 

for i in range(last):
    swapped = False
    for j in range(last - i - 1):
        if List[j] > List[j + 1]:
            List[j], List[j + 1] = List[j + 1], List[j]
            swapped = True
    if not swapped:
        break
print(List)