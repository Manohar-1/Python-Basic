list = [0,1] 

start = 2; 

how_many = int(input("Length of fibonacci sequnce you want:")) 

times = how_many - start 

for i in range(0,times):
    list.append(list[start-1]+list[start-2]) 
    start+=1
print(list)