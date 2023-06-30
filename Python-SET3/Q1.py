tuple_list = [("John", 25), ("Jane", 30)]
string=""
for i in tuple_list:
    string += i[0] + " is "+ str(i[1]) + " years old."
print(string)