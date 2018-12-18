while True:
    print("Options:")
    print("Enter '+' to add two numbers")
    print("Enter '-' to subtract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    print("Enter 'quit' to quit the program")
    user_input = input(": ")

    if user_input == 'quit':
        break

    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))   
    
    if user_input == "+":
        result = str(num1+num2)
        print(str(num1) + " + " + str(num2) + " = " + result)
    elif user_input == "-":
        result = str(num1-num2)
        print(str(num1) + " - " + str(num2) + " = " + result)
    elif user_input == "*":
        result = str(num1*num2)
        print(str(num1) + " * " + str(num2) + " = " + result)
    elif user_input == "/":
        result = str(num1/num2)
        print(str(num1) + " / " + str(num2) + " = " + result)
    else:
        print("Unknown input")
    