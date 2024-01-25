def printcommand(x): 
    with open("isprimecompiled.py", 'a') as f: 
        f.write("i = eval(input(\"Please input the number you want to test \"))\n") 
        for i in range(x): 
            f.write(f"if i == {i}: \n")  
            f.write(f"\tprint(\"{i} is a {getcompo1(i)}\")\n") 
            if (i % 10000 == 0): 
                print(f"{i}/{x}") 
        f.write(f"input() ") 
            
def isprime(x): 
    if ( x == 1 or x == 0 ): 
        return "Not a prime number nor a compound number "
    for i in range(2, (int)(x ** 0.5 * 2)): 
        if (x % i == 0): 
            return "Compound number " 
    return "Prime number " 

def allprime(x): 
    prime = [2] 
    for i in range(2, x): 
        index = 0 
        prime.append(i) 
        while (prime[index] < (int)(i ** 0.5)): 
            if i % prime[index] == 0: 
                prime.remove(i) 
                break 
            index = index + 1 
    print(prime) 

def getcompo1(x): 
    if ( x == 1 or x == 0 ): 
        return "Not a prime number nor a compound number "
    for i in range(2, (int)(x ** 0.5 * 2)): 
        if (x % i == 0): 
            return getcompo2(x) 
    return "Prime number " 

def getcompo2(x): 
    compo = "compound number " 
    for i in range (1, (int)(x ** 0.5 * 2)): 
        if ( x % i == 0 ): 
            compo += f"= {i} * {(int)(x/i)} " 
    return compo 

for i in range(100): 
    print(f"{i} is a {isprime(i)}") 
    input() 

printcommand(10000) 

'''
allprime(300000) 
for i in range(300000): 
    isprime(i) 
print("finish")  
''' 
