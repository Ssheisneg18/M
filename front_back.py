def front_back( a , b):
    i = len(str1)/2 # برای پیدا کردن اندیس عنصر میانی 
    if len(str1)%2 == 0:# اگر طول زوج بود
        front = str1[:int(i)]
        back = str1[int(i):]
    else:# اگر طول فرد بود
        front = str1[:int(i)+1]
        back = str1[int(i)+1: ]
    fa = front
    ba = back
        
    j = len(str2)/2
    if len(str2)%2 == 0:
        front1 = str2[:int(j)]
        back1 = str2[int(j):]
    else:
        front1 = str2[:int(j)+1]
        back1 = str2[int(j)+1: ]
            
    fb=front1
    bb = back1
    
    result = fa + fb + ba +bb
    return result
str1=input("enter the first str:")
str2 = input("enther the second str:")
print(front_back(str1 ,str2))