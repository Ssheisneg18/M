def not_bad(string):
    bad = string.find("bad")
    #index کلمات خواسته شده را در جمله پیدا میکنیم 
    not1 =string.find("not")
    if bad > not1:
        #باید کلمه ی بد بعد از کلمه ی نات باشه 
        string = string.replace(string[not1:bad+3],"good")
        #کلمه ی خوب را با هر کلمه ایی بین نات و بد است جایگزین میکنیم
        # bad+3 به این دلیل هست که خود bad مروبوط به اندیس شروع کلمه هست و برای پاک کردن کل کلمه باید طول کلمه را بهش اضافه کنیم 
        return string
        
string=input("enther a sentence:")
print(not_bad(string))