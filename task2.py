def addition(x,y):
    return x + y;
def substraction(x,y):
    return x - y;
def multiplication(x,y):
    return x * y;
def division(x,y):
    if (x != 0):
        return x / y
    else:
        return "please give valid number!"
def modulus(x,y):
    return x % y
def exponentiation(x,y):
    return x ** y
def floor (x,y):
    if (x != 0):
        return x // y
    else:
        return "please give valid number!"
#taking inputs from the user
num1 = int(input("Enter number for first input:"))
num2 = int(input("Enter number for second input:"))
operation = input("please give arithmetic operator(+,-,*,/,**,%,//): ")
#execution of arithmetic operator
if( operation == "+"):
    result = addition(num1,num2)
elif( operation == "-"):
    result = substraction(num1,num2)
elif( operation == "*"):
    result = multiplication(num1,num2)
elif( operation == "/"):
    result = divison(num1,num2)
elif( operation == "%"):
    result = modulus(num1,num2)
elif( operation == "**"):
    result = exponentiation(num1,num2)
elif( operation == "//"):
    result = floor(num1,num2)
else:
    result = "please give valid operator"
print(result)




    



    
