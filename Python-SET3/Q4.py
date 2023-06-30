word = "madam" 

left = 0 
right = len(word)-1 

while(left<right):
    if(word[left]==word[right]):
        left+=1
        right-=1
        continue
    else:
        break;

if(left>=right):
    print(word+" is palindrome")
else:
    print(word+" is not palindrome")