import time 
import random

def exam_number(): 
    x = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000','1001', '1010', '1011', '1100', '1101', '1110', '1111']
        #مجموعه اعداد باینری 
    
    
    sh = time.time()#زمان شروع 
    time1 = 20  #مهلت بازی
    t = 0 #متغیر برای شمارش تعداد سوال پرسیده شده
    correct = 0
    incorrect=0
    while True:#به صورت متوالی تا وقتی تایم تموم نشده سوال میپرسه 
        if time.time() - sh > time1 :# میخواستم while time.sleep(20) اما کار نمیکرد مجبور شدم تایمی که برنامه ران میشه رو با تایم سیستم مقایسه کنم و اگر تایم تموم شده باشه از برنامه خارج میشه
            print("finish")
            break
        
        binary = random.choice(x)#یه عدد باینری رندوم انتخاب میکنیم 
        t += 1#هر بار به تعداد یدونه اضافه میکنیم
        print(binary)
        
        num =int(input("decimal: ")) 
        decimal = 0 
        tavan  = 0
        for i in reversed(binary):
            #نمیدونم چرا تابع اماده برای تبدیل باینری به دسیمال کار نکرد:/
            decimal += int(i) * 2 **(tavan)
            tavan +=1
        if num == decimal:
            correct+=1 
            print("correct")
        else:
            incorrect +=1
            print("incorrect!")
            
    print("\ncorrect:", correct , "\nincorrect:",incorrect, "\ntotal:", t)
    
        
        
    

exam_number()


