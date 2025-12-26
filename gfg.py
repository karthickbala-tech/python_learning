'''n=1223
print(str(n)[-1])
if str(n)== str(n)[::-1]:
    print(True)
else:
    print(False)'''
    
    
'''def floorSqrt(n): 
    if n==0 or n==1:
        return n
    for i in range ((n//2)+1):
        if i*i>n:
            return i-1
        elif i*i==n:
            return i
print(floorSqrt(3))'''

"""n=int(input("Enter a number:"))            
count=0
for i in range(1,n):
    if n%i==0:
        count+=i
if count==n:
    print(True)
else:
    print(False)"""

'''arr= [3,2,9]
if len(arr)< 3:
    print("-1")
print(max(arr))
#print(min(arr),max(arr))'''

'''arr =[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr.sort(reverse=False)
print(arr)'''

'''a= [1,1,1,1,1,1, 2, 5, 4, 0]
b = [2, 4, 5, 1,1,1,1,1,0, 1]
a1=list(set(a))
b1=list(set(b))
print(a1,b1)'''

'''a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
n=counter(a)
print(n)'''

'''arr = [2, 3, 2, 3, 5]
target=4
if len(arr)<=1:
	print(False)
 
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        k=arr[i]+arr[j]
	    if k ==target:
		    print(True)
print(False)'''

'''arr = [2, 3, 2, 3, 5]
print(set(arr))'''

'''a = [1, 2, 3, 2, 1] 
b = [3, 2, 2, 3, 3, 2]
c=set(a.__add__(b))
print(c)'''

'''a = [89, 24, 75, 11, 23]
b = [89, 2, 4]
seen=set()
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j] :
            seen.add(a[i])
print(len(seen)) '''

'''a= [2, 3, 6, 7, 9]
b= [1, 4, 8, 10]
k = 5   
l=list(set(a.__add__(b)))
print(l[k-1])   '''

'''arr =[10, 5, 2, 7, 1, -10]
k=15
n=len(arr)
seen=0
result=0
for i in range(n):            
    seen+=arr[i]
    if seen == k:
        result=i+1
print(result)'''

'''nums = [2,2,1,1,1,2,2]
seen=set()
dup=set()
for i in nums:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)
print(dup)'''

'''arr= [2, 3, -8, 7, -1, 2, 3]
s=0
for i in arr: 
    s+=i
    
   
print(s)'''

'''arr= [10, 10, 10]
n=len(arr)
count=0
for i in range(n):
    for j in range(i+i,n):
        if arr[i]>arr[j]:
            count+=1
print(count)'''


'''def search_matrix(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                return True
    return False

arr = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

print(search_matrix(arr, target))
#print(arr[0][1])'''

intervals = [[1,3],[2,6],[8,10],[15,18]]
'''a= len(intervals)
seen=[0,0,0,0]
for i in range(a):
    if intervals[i][1] < intervals[i][0]:
        seen[i]= [intervals[i][0], intervals[i][1]]
    else:
        seen[i]=intervals[i]
print(seen)'''
        
'''intervals.sort()
print(intervals)'''

'''arr= [-2, 6, -3, -10, 0, 2]
if not arr:
    print("0")
    
max_product=current_max=current_min=arr[0]
    
for i in range(1,len(arr)):
    num=arr[i]

    if num<0:
        current_max,current_min=current_min,current_max
    current_max= max(num,current_max*num)
    current_min= min(num,current_min*num)

    max_product=max(current_max,max_product)
print(max_product) '''  

'''nums = [3,2,1]
def cal1():
    nums[-1],nums[-2]=nums[-2],nums[-1]
def cal2():
    nums[-1],nums[-3]=nums[-3],nums[-1]
    cal1()
def cal3():
    nums[-2],nums[-3]=nums[-3],nums[-2]
    cal1()
def cal4():
    nums.reverse()
if nums[-1] > nums[-2] :        
    cal1()
elif nums[-1] < nums[-2] and nums[-1]>nums[-3]:
    cal2()
elif nums[-1]<=nums[-2] and  nums[-2]>=nums[-3]:
    cal3()
elif nums[-1]<nums[-2]<nums[-3]:
    cal4()
print(nums)'''

'''nums = [1,3,2]
n = len(nums)
i = n - 2

while i >= 0 and nums[i] >= nums[i + 1]:
    i -= 1

if i >= 0:
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]

left, right = i + 1, n - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
    print(nums)     
 
n=len(nums) #3
i=n-2 #1

while i>=0 and nums[i]>=nums[i+1]:
    i-=1

if i>=0:
    j=n-1
    while nums[j]<=nums[i]:
        j-=1
    nums[i],nums[j]=nums[j],nums[i]
    

left,right=i+1,n-1
while left<right:
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1
print(nums)'''

'''n=10
count=0
seen=[]
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        seen.append(i)
    count=0       
print(seen)'''

'''n=35
if n<2:
    print([])
prime= [True]*(n+1)
prime[0]=prime[1]=False

for i in range(2,n+1):
    if prime[i]:
        for j in range(i*2,n+1,i):
            prime[j]=False
result=[]
for i in range(2,n+ 1):
    if prime[i]==True:
        result.append(i)
print(result)'''

'''matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
found=False
for i in range(len(matrix)):
    if matrix[i][-1]>=target>=matrix[i][0]:
        for j in range(len(matrix[i])):
            if target==matrix[i][j]:
                found=True
                break
    if found:
        break
print(found)''' 

'''mat= [[0, 1, 2], [3, 4, 5], [6, 7, 8]]  
n= len(mat)
for i in range(n):
    for j in range(i+1,n):
        mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
for j in range(n):
    for i in range(n//2):
        mat[i][j],mat[n-1-i][j]=mat[n-1-i][j],mat[i][j]
print(mat)'''

'''mat = [[1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]]
count=[]
for i in mat:
    count.append(i.count(1))
a=min(count)
for idx,val in enumerate(count):
    if val ==a:
        print(idx+1)
        break'''
'''for j in count:
    if a==0:
        print('1')
        break
    elif a==j:
        print(j)
        break'''
        
'''mat=[[1,2,3],[4,5,6],[7,8,9]]
k=8
km= k % 3
if km ==1:
    mat[0][0],mat[0][1],mat[0][2]=mat[0][1],mat[0][2],mat[0][0]
    mat[1][0],mat[1][1],mat[1][2]=mat[1][1],mat[1][2],mat[1][0]
    mat[2][0],mat[2][1],mat[2][2]=mat[2][1],mat[2][2],mat[2][0]
elif km ==2:
    mat[0][0],mat[0][1],mat[0][2]=mat[0][2],mat[0][0],mat[0][1]
    mat[1][0],mat[1][1],mat[1][2]=mat[1][2],mat[1][0],mat[1][1]
    mat[2][0],mat[2][1],mat[2][2]=mat[2][2],mat[2][0],mat[2][1]
elif km==3:
    return mat
return mat'''
        
'''matrix = [[1,1,1],[1,0,1],[1,1,1]]
k=len(matrix)
for i in matrix:
    for j in matrix:
        if matrix[i][j]==0:
            matrix[i][0]=0
            matrix[0][j]=0
n=10 
k= (n*(n+1)//2 -1)%3
print(k)'''            
             
'''mat= [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
n=len(mat)
result=[] 
print(n)'''           
            
'''arr = [1, 2, 8, 10, 10, 12, 19] 
x = 11
floor=-1
for i in range(len(arr)):
    if arr[i]<=x:
        floor=i
return floor
    print(i)'''
        
'''arr= [1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 5
f=-1
l=-1

for i in range(len(arr)):
    if arr[i]==x and i!=arr[i-1]:
        f=i
    elif arr[i]==x and i!=arr[i+1]:
        l=i
result=[f,l]
    
print(result)'''

'''nums = [3,0,1]
sort=sorted(nums)
if sort[0]!=0:
    print(0)
for i in range(len(nums)):
    if i!=sort[i]:
        print(i)
    elif i==sort[-1]:
        print(sort[-1]+1)'''

'''n = 10
n1=str(n)
print(int(n1[::-1]))'''

'''n=4
i=1
arr=[]
if i==n:
    arr.append(i)
while i<=n:
	mid=n//2
    if mid %2 ==0:
        pass
    elif mid %2 !=0:
        
print(arr)'''

'''arr=[1, 2, 3, 4, 5]
a=sorted(arr)
n=len(arr)
for i in range(n):
    if arr[0]!=a[0]:
        if a[0]==arr[i+1]:
            return i+1
            break
if a==arr:
    return 0'''

'''print(int(eval(input("enter"))))'''

'''n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=" ")
    for k in range(i+1):
        print('*',end=" ")
    for l in range(i):
        print('*',end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print(' ',end=" ")
    for k in range(i+1):
        print('*',end=" ")
    for l in range(i):
        print('*',end=" ")
    print()'''
    
    
'''n = 5  

# Upper half
for i in range(n):
    print('  ' * (n - i - 1), end='')     # Leading spaces
    print('* ' * (2 * i + 1))             # Stars (odd count)

# Lower half
for i in range(n - 2, -1, -1):
    print('  ' * (n - i - 1), end='')     # Leading spaces
    print('* ' * (2 * i + 1))             # Stars (odd count)
'''
    
    
'''arr =[1]
first=0
last=len(arr)-1
while first<last:
    mid=(first+last)//2
    if arr[first]<arr[mid]<arr[last]:
        first+=1
        last-=1
    if arr[mid]>arr[last]:
        mid+=1
    if arr[mid]<arr[first]:
        mid-=1
    if arr[mid-1]<arr[last] or arr[mid]>arr[first]:
        print(True)
        break
    print(False)'''

'''N=3
mat = [[0, 0, 1], 
              [0, 1, 1], 
              [0, 0, 0]]
print(len(mat))'''

'''arr=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target=1
result=False
i=0
j=len(arr[0])-1
while i<len(arr) and j>=0:
    if arr[i][j]==target:
        result=True
        break
    elif arr[i][j]>target:
        j-=1
        
    else:
        i+=1
print(result)'''

'''n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''
   
'''n=str(input())
f=0
l=len(n)-1
while f<l:
    if int(n[f])!=int(n[l]):
        int(n[f])=int(n[l])
        f+=1
        l-=1
    elif int(n[f+1])!=int(n[l+1]):
        n[f]+=1
        n[f]=n[l]
print(n)'''

'''stalls =[1, 2, 4, 8, 9]
k = 3
stalls.sort()
for i in range(len(stalls)-1):
    if stalls[i]<k<stalls[i+1]:
        print(i)
        break'''

'''for i in range(5):
    for j in range(4):
        if j==0 or i+j==3:
            print("*",end="")
    print()'''

'''n=input()
l=len(n)
k=0

for i in n:
    b=1
    for j in range(1,int(i)+1):
        b*=j
    k+=b  
    
if k==int(n):
    print(n,"is a strong number")
else:
    print(n,"is a not strong number")'''
    
    
'''mat= [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
n=len(mat)
a=0
b=0
        '''
'''a= [3, 5, 6, 12, 15,90]
b= [8, 4, 7, 10, 9]
a=a+b
a=sorted(a)
e=len(a)//2
if len(a)%2==0:
    f=(a[e]+a[e-1])/2
    print(f)
else:
    print(a[e])'''
