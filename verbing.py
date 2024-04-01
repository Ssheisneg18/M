def verbing(string):
    if len(string)>= 3:
        if string.endswith("ing"):
                verb1 = string+"ly"
                return verb1
        
        else:
           verb = string + "ing"
           return verb 
    if len(string)<3:
        return string
    
string=input("enter a string:")
print(verbing(string))