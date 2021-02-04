def volume(x):
    if ( x > 0 and isinstance(x ,(int,float))):
        return x * x * x
    else: return 0

def average(list):
    if len(list) > 0:
        result = sum(list) / len(list)
        return result
    else: return 0

def fullname(x,y):
    if(isinstance(x,str) and isinstance(y,str)):
        z = x + " " + y
        return z
    else: return 0