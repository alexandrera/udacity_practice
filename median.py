def medianHard(a,b,c):
    if a > b: 
        if a < c: 
            if b < a:
                return a
            else:
                return b
        else:
            return c
    else:
        if b > c:
            if a > c:
                return a
            else:
                return c
        else:
            return b
        
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def medianEasy(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger (b,c)
    if big == b:
        return bigger (a,c)
    else:
        return bigger (a,b)
            
print(medianHard(1,2,3))
print(medianEasy(2,3,1))
