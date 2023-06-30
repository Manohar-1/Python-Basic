given = "PyNaTive"
lower_letters="" 
upper_letters=""
for i in given:
    if(i.islower()):
        lower_letters+=i
    else:
        upper_letters+=i


print(lower_letters+upper_letters)