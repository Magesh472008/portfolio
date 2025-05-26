x= int(input("Enter a number:"))
y= int(input("Enter a number:"))
choose=(input("Enter operator:"))
def add(x,y):
    return x+y
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y  

if choose == "+":
   print("return:",add(x,y))
elif choose == "-":
    print("return:",subtract(x,y))
elif choose == "*":
    print("return:",multiply(x,y))
elif choose == "/":
    print("return:",divide(x,y))
else:
    print("Invalid")