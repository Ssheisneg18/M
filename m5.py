import string
def check_pass():
    result =[]
    users = [('alex', 'Ab1674d:'), ('bomm', 'abc13()'), ('python', 'sec91:)')] #یوزرنیم و پسورد را خودم دادم و فقط یکی از ان ها شرایط لازم را دارد 
    let =string.ascii_uppercase
    let1= string.ascii_lowercase
    a =string.punctuation
    n ="1234567890"
    #برای چک کردن پسورد ها نیاز به تمام حروف بزرگ و کوچیک و علائم نگارشی و اعداد هستیم
    #تک تک پسورد هارو چک میکنیم میشد با استفاده ها index هم این کار را کرد
    for username ,password in users:
        if len(password)>7:
            if password.find(let): 
                 if password.find(let1):
                     if password.find(a):
                         if password.find(n):
                             result.append(username)
                             print(result)
    
check_pass()
