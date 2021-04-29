import re

ops = ["x","^","+","-","÷"]

def front(x):
    z = ""
    for i in range(len(x)+1):
        try:
            elem = x[-1*(i+1)]
        except IndexError:
            return z

        if elem not in ops:
          
            z = elem + z
        else:
            
            return z

def reverse_string(str2):  
    str1 = ""
    for i in str2:  
        str1 = i + str1  
    return str1


def back(x):
    z = ""
    for i in range(len(x)+1):
        try:
            elem = x[i]
        except IndexError:
            return reverse_string(z)
 
        if elem not in ops:
            z = elem + z

        else:
            return reverse_string(z)

def powersolve(j):
    s = j

    while "^" in s:
        
        i = s.find("^")
        a = s[:i]
        b = s[i+1:]
        t1 = front(a)
        t2 = back(b)
        
        power = float(t1)**float(t2)
       
        torep = t1 + "^" + t2
        s = s.replace(torep,str(power))

    return s

def dividesolve(j):
    s = j

    while "÷" in s:
        
        i = s.find("÷")
        a = s[:i]
        b = s[i+1:]
        t1 = front(a)
        t2 = back(b)
        
        power = float(t1)/float(t2)
       
        torep = t1 + "÷" + t2
        s = s.replace(torep,str(power))

    return s

def multsolve(j):
    s = j

    while "x" in s:
        
        i = s.find("x")
        a = s[:i]
        b = s[i+1:]
        t1 = front(a)
        t2 = back(b)
        
        power = float(t1)*float(t2)
       
        torep = t1 + "x" + t2
        s = s.replace(torep,str(power))

    return s

def addsolve(j):
    s = j

    while "+" in s:
        
        i = s.find("+")
        a = s[:i]
        b = s[i+1:]
        t1 = front(a)
        t2 = back(b)
        
        power = float(t1)+float(t2)
       
        torep = t1 + "+" + t2
        s = s.replace(torep,str(power))

    return s

def subtractsolve(j):
    s = j


    while "-" in s:
        
        i = s.find("-")
        a = s[:i]
        b = s[i+1:]
        t1 = front(a)
        t2 = back(b)
        
        power = float(t1)-float(t2)
       
        torep = t1 + "-" + t2
        s = s.replace(torep,str(power))

    return s

def solution(bruh):
    iput = str(bruh)
    if errcheck(iput) == 0:
        if re.search('[x+\-÷\^]', iput) is None:
            return iput
        else:
            x = subtractsolve(addsolve(multsolve(dividesolve(powersolve(iput)))))
            return x  

    else:
        return errcheck(iput)

def errcheck(inp):
    t2 = re.search('[x+\-÷\^]$',inp)
    if t2 != None:
        return "Incomplete operation!"

    t4 = re.search('^[x+\-÷\^]', inp)
    if t4 != None:
        return "Can't begin with an operator"

    t1 = re.search('[A-Za-z]$',inp)
    if t1 != None:
        return "Operation can't end with an alphabet!"
    
    return 0
