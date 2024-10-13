n1 = int(input("Enter first number: "))
action = input("Enter action: +,-,*,/")
n2 = int(input("Enter second number: "))

if action == "+":
    print(n1+n2)
elif action == "-":
    print(n1-n2)
elif action == "*":
    print(n1*n2)
elif action == "/":
    if n2 != 0:
        print(n1/n2)
    else:
        print("Error:impossible to solve ")
else:
    print("Enter correct action")