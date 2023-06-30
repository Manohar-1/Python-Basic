# file = open("new_file.txt","a") 
file = open("new_file.txt","r")

content = file.read() 

words = content.split(); 
print(len(words))

file.close()