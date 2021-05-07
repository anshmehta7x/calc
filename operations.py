import re
import math
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

        if re.search("^[\-].*[0-9]$", s) is not None:
            return s


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

def trigsolve(mainstr,func,inverse,mode):
    if "π" in mainstr:
        nopi = mainstr.replace("π","")
        piremoved = float(nopi) * math.pi

    else:
        piremoved = float(mainstr)

    if inverse == False:
        if mode == True:
            rads = math.radians(piremoved)
        else:
            rads = piremoved

        if func == "sin":
            
            return round(math.sin(rads),4)
        
        elif func == "cos":
            return round(math.cos(rads),4)

        elif func == "tan":
            if math.tan(rads) > 10000000:
                return "undefined"
            else:
                return round(math.tan(rads),4)
        
        elif func == "csc":
            return round(1/math.sin(rads),4)
        
        elif func == "sec":
            return round(1/math.cos(rads),4)

        elif func == "cot":
            try:
                1/math.tan(rads)
            except ZeroDivisionError:
                return "undefined"
            if 1/math.tan(rads) > 10000000:
                return "undefined"
            else:
                return round(math.tan(rads),4)
    
    elif inverse == True:

        if func == "sin":
            x = math.asin(piremoved)
            if mode == True:
                return round(math.degrees(x),4)
            else:
                return round(x,4)

        elif func == "cos":
            x = math.acos(piremoved)
            if mode == True:
                return round(math.degrees(x),4)
            else:
                return round(x,4)

            

        elif func == "tan":
            x = math.atan(piremoved)
            if mode == True:
                return round(math.degrees(x),4)
            else:
                return round(x,4)


        elif func == "csc":
            x = math.asin(1/piremoved)
            if mode == True:
                return round(math.degrees(x),4)
            else:
                return round(x,4)

        elif func == "sec":
            x = math.acos(1/piremoved)
            if mode == True:
                return round(math.degrees(x),4)
            else:
                return round(x,4)


        elif func == "cot":
            x = math.atan(1/piremoved)
            if mode == True:
                return round(math.degrees(x),4)
            else:
                return round(x,4)

def trigerrcheck(mainstr,func,inverse,mode):

    t1 = re.search('[a-zA-Z]', str(mainstr))
    if t1 is not None:
        return "Can't have letters!"
    
    t2 = re.findall('\.',mainstr)
    if len(t2) > 1:
        return "Too many dots"

    t3 = re.findall("[π]", mainstr)
    if len(t3) > 1:
        return "Can only have one π"
    
    return trigsolve(mainstr,func,inverse,mode)

def logsolve(inpval, base):
    if "e" in inpval:
        if inpval == "e":
            i = math.e
        else:
            x = inpval.replace("e","")
            i = float(x) * math.e
    
    else:
        i = float(inpval)
    
    if "e" in base:
        if base == "e":
            b = math.e
        else:
            y = base.replace("e","")
            b = float(y) * math.e
    
    else:
        b = float(base)
    
    return math.log(i,b)

def q(a,b,c):
    try:
        A = float(a)
        B = float(b)
        C = float(c)

    except TypeError or ValueError:
        return "Enter numbers only!"
    
    print(validity(A,B,C))
    if validity(A,B,C) == "sus":
        return "Equation does not have real roots"

    else: 
        r = validity(A,B,C)
        root1 = round(((-1*B)+(r**0.5))/(2*A),4)
        root2 = round(((-1*B)-(r**0.5))/(2*A),4)
        r1 = str(-1*root1)
        if root1 > 0:
            r1 = r1
        else:
            r1 = "+"+r1
        r2 = str(-1*root2)
        if root2 > 0:
            r2 = r2
        else:
            r2 = "+"+r2
        
        z = "(x{})(x{})".format(r1,r2)
        mainstr = "root 1: {} \nroot 2: {} \n{}".format(str(root1),str(root2),z)
        return mainstr
    
def validity(a,b,c):
    disc = (b**2)-4*a*c
    print(disc)
    if disc == 0.0:
        return disc
    else:
        if disc >= float(0):
            return disc
        else:
            return "sus"
