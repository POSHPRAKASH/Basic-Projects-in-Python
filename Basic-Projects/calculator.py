print ('Welcome to the Basic Calculator')
while 1 :
    print('What would you like to do ???')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Power')
    print('6. Remainder')
    print('7. Exit')
    choice = int(input("Enter Your Choice:"))

    if choice == 1 :
        num1 = int(input("Enter your Number 1:"))
        num2 = int(input("Enter your Number 2:"))
        print('Output:', num1+num2 )
    elif choice == 2 :
        num1 = int(input("Enter your Number 1:"))
        num2 = int(input("Enter your Number 2:"))
        print('Output:', num1-num2 )
    elif choice == 3 :
        num1 = int(input("Enter your Number 1:"))
        num2 = int(input("Enter your Number 2:"))
        print('Output:', num1*num2 )
    elif choice == 4 :
        num1 = int(input("Enter your Number 1:"))
        num2 = int(input("Enter your Number 2:"))
        print('Output:', num1/num2 )
    elif choice == 5 :
        num1 = int(input("Enter your Number 1:"))
        num2 = int(input("Enter your Number 2:"))
        print('Output:', num1**num2 )
    elif choice == 6 :
        num1 = int(input("Enter your Number 1:"))
        num2 = int(input("Enter your Number 2:"))
        print('Output:', num1%num2 )
    elif choice == 7 :
        print('Exiting....')
        break