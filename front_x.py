def front_x(list1):
    x=[]
    words=[]
    for i in list1:
        if i.startswith("x"):
            x.append(i)
        else:
            words.append(i)
            
    result = x + words
    return result
    
    
    
list1=input("please enter the words:")
print(front_x(list1))