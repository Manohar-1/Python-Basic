arr = [2,4,5,7,11]
target = 9 
ans=[]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(i!=j and arr[i]+arr[j]==target):
            ans.append([arr[i],arr[j]])
print(ans)

