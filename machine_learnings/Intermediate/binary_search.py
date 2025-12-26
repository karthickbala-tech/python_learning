# Implement binary search on a sorted list.
num = list(map(int, input("Enter numbers separated by space: ").split()))

search = int(input("Enter a searching number: "))

num = sorted(num)
first = 0
last = len(num) - 1
find = False

while first <= last:
    mid = (first + last) // 2
    if num[mid] < search:
        first = mid + 1
    elif num[mid] > search:
        last = mid - 1
    else:
        find = True
        break
        
if find:
    print("search number is found")
else:
    print("search is not found")
