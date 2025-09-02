print('''
+ Add
- Subtract
* Multiply
/ Divide
''')

num1= int(input("Enter your value1:-  "))
num2= int(input("Enter your value2:-  "))
opr = input("Enter the operator(+,-,*,/):  ")

if opr == "+":
    print(num1+num2)
elif opr == "-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
else:
    print("Invalid operator")

