prime = int(input("Give me a number:")) 
count =0
for i in range(1,prime+1):
    if(prime%i==0):
        count+=1 
if(count==2):
    print("YES, It's a prime number")
else:
    print("NO, It's not")