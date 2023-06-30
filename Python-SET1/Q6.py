string =input("Hello User, Please give me a string:")

count =0
for i in string:
    if(i=='a' or i== 'A' or i=='e' or i=='E' or i=='o' or i=='O' or i=='i' or i=='I' or i=='U' or i=='u'):
        count+=1


print("The vowel count is:" + str(count))