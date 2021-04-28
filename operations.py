import re

def solution(bruh):
    iput = str(bruh)
    if errcheck(iput) == 0:
        pass

    else:
        return errcheck(iput)

def errcheck(inp):
    t2 = re.search('[x+\-÷]$',inp)
    if t2 != None:
        return "Incomplete operation!"

    t1 = re.search('[A-Za-z]$',inp)
    if t1 != None:
        return "Operation cant end with an alphabet!"
    
    