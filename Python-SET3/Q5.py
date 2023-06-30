def swap(i,j,arr):
    temp = arr[i]
    arr[i] = arr[j] 
    arr[j] = temp
import math

arr = [64, 25, 12, 22, 11] 

for i in range(0,len(arr)):
    min = math.inf
    index=-1
    for j in range(i,len(arr)):
        if(arr[j]<min):
            min=arr[j]
            index=j 
    if(index!=-1):
        swap(i,index,arr)


print(arr) 


