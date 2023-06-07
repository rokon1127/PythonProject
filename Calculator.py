print("=================Simple Calculator====================================")


first_number =int(input("Enter Your Number: "))
second_number =int(input("Enter Another Number: "))
operation =input("Enter Operation: ")

user_input01 = first_number

user_input02 = second_number
op = operation

if op=="+":
    print("Add: ", user_input01+user_input02 )

elif op=="-":
    print("SUB: ", user_input01-user_input02 )

elif op=="*":
    print("Mul: ", user_input01*user_input02 )

elif op=="/":
    print("Div: ", user_input01/user_input02 )

print("======================ThankYou=========================")