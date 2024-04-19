num1=int(input("Enter the Number 1 :"))
num2=int(input("Enter the Number 2 :"))

operator=input("Enter The Operator : ")

if operator=='+':
    print(num1+num2)
elif operator=='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(num1/num2)
elif operator=='%':
    print(num1%num2)
else:
    print('Invalid Operator')    

