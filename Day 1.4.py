def ispalindrome(n):
    return n==n[::-1]
n=input("Enter the integer ")
s=ispalindrome(n)
if n.isalpha():
    print("Enter only numbers")
elif s:
    print("True")
else:
    print("False")
    
