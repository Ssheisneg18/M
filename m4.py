import random
def calculate_magic_number():
    num1=int(input("enter the first num:"))
    num2=int(input("the second number:"))
    x = random.randrange(num1 , num2 +1)
    # در این قسمت عدد دوم باید یکی بیشتر شود چون در حالت عادی خودش در بازه نخواهد بود و برای قرارگیری ان باید یکی به ان اضافه کنیم 
    print("the magic number:",x)
    
calculate_magic_number()