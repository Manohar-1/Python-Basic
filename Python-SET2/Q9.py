sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"] 

my_dict = {} 

for i in keys:
    my_dict[i] = sample_dict[i] 

print(my_dict)