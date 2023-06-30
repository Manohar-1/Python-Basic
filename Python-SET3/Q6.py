from collections import deque


def addToQueue(q1,q2,element):
    while(len(q1)!=0):
        q2.append(q1.popleft())

    q1.append(element) 

    while(len(q2)!=0):
        q1.append(q2.popleft())


def removeFromQueue(q1):
    if(len(q1)==0):
        return "None"
    
    return q1.popleft()


q1 = deque() 
q2 = deque() 

addToQueue(q1,q2,1);
addToQueue(q1,q2,2);
addToQueue(q1,q2,3);
addToQueue(q1,q2,4);
addToQueue(q1,q2,5);

print(removeFromQueue(q1))
print(removeFromQueue(q1))


addToQueue(q1,q2,6)
print(removeFromQueue(q1))
print(removeFromQueue(q1))
print(removeFromQueue(q1))