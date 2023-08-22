def isnumeric(s):
    s=s.strip()
    try:
        s=float(s)
        return True
    except:
        return False 
n=input("Enetr a value ")
print(isnumeric(n))
