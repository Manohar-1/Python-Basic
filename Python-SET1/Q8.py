num = int(input("give me a number:")) 

product =1 
for i in range(1,num+1):
    product *=i;

print("The factorial of " + str(num) + " is "+ str(product))