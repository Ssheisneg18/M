# من برای تابع اخر که قرار بود یه کد استخراج بشه همه توابع رو اوردم اینجا و یه سری تغیرات دادم که قبل از اجرای تابع unclock_vauleچاپ نشن 




import keyword
def dec1(text):
    """ برای پیدا کردن کلمه کلیدی توی متنمون """
    keyword1 = [ ]#یه لیست خالی درست میکنیم 
    for word in keyword.kwlist:
        if word in text:
            keyword1.append(word)#هر کلمه کلیدی که توی منن باشه به لیست foundkeyword منتقل میشه
    return keyword1
    

#مطمئن نیستم که باید متن رو از کابرد گرفت یا از اول تو یه متغیر قرار داد
text= "ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables...quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversar...blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati..."
dec = dec1(text)
#print(dec) 
#بعد از بررسی تمام کلمات کلیدی انهایی که در متن بودن ریترن میشن و اینجا پیرینت میشن 
#___________________________________
def solve_puzzles():
    """تابعی برای چک کردن و پیدا کردن مقادیرtrue or false 
    و سپس برگرداندن ان ها"""
        
        
    #تمام مقادیر رو تبدیل به یه لیست کردم که به عنوان ورودی تابع باشه ولی چون در نهایت باید خروجی همه ی توابع رو داشته باشیم اوردمش توی خود تابع که با متغیر های دیگه قاطی نشه
    puzzle = ['ali',
        '1233',
        0,
        "",
        [],
        {},
        'False',
        '0',
        'None',
        None,
        -1,
        [1, 2, 3],
        {'key': 'value'},
        True,
        ' ',
        '[]',
        '[1, 2, 3]',
        '{}',
        "{'a': 1}",
        True,
        'ali',
        '1234',
        1,
        0.1,
        -0.1,
        True,
        ' ',
        '[]',
        '[1, 2, 3]',
        '{}',
        "{'a': 1}",
        True,
        'ali',
        '1234',
        1,
        0.1,
        -0.1]
    
    x = []#یه لیست خالی درست کردم که بتونم بعدا ورودی هایی که ویژگی مورد نظر رو داشتن توی لیست اضافه و چاپ کنم
    for i in puzzle:
        i = bool(i)
        x.append(i)
    return x
        

solve =solve_puzzles()
#print(solve)
#___________________________________

import random
def calculate_magic_number():
    num1=int(input("enter the first num:"))
    num2=int(input("the second number:"))
    x = random.randrange(num1 , num2 +1)
    # در این قسمت عدد دوم باید یکی بیشتر شود چون در حالت عادی خودش در بازه نخواهد بود و برای قرارگیری ان باید یکی به ان اضافه کنیم 
    print(x)
    

#___________________________________
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
                             return username
    

#print(usernam)
#___________________________________
def unclock_vaule(j):
    for i in j:
        x = i[0][0]
        return x





print(unclock_vaule(dec))
print(unclock_vaule(str(solve)))
magic = calculate_magic_number()
print(unclock_vaule(str(magic)))
usernam = check_pass()
print(unclock_vaule(usernam))
