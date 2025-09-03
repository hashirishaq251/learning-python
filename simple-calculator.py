#© 2025 hashirishaq251
import sys
print("=====-----=====-----Welcome to the simple calculator program designed by M.M.Hashir-----=====-----=====")
def sum():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"The sum of {a} and {b} is {a + b}")
def multiply():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"The product of {a} and {b} is {a * b}")
def divide():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    if b != 0:
        print(f"The division of {a} by {b} is {a / b}")
    else:
        print("Error: Division by zero is not allowed.")  
def subtract():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"The difference when {b} is subtracted from {a} is {a - b}")
def ag():
    again = input("Do you want to try again? (y/n): ")
    if again == 'y':
        main()
    elif again == 'n':
        print("Goodbye!")
        sys.exit(0)
def main():
    a = input("Enter a for additon, s for subtraction, m for multiplication, d for division: ")
    if a == 'a':
        sum()
        ag()
    elif a == 'm':
        multiply()
        ag()
    elif a == 'd':
        divide()
        ag()
    elif a == 's':
        subtract()
        ag()
    else:
        print("Invalid input")
        again = input("Do you want to try again? (y/n): ")
        if again == 'y':
            main()
        elif again == 'n':
            print("Goodbye!")
            sys.exit(0)
main()    
        




       