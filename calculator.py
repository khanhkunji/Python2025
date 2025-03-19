#Calculator basic operations
def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b != 0:
        return a/b
    else:
        return "Division by zero is not allowed"
    
def calculator():
    print("""\tCALCULATOR
          1. Add\n
          2. Subtract\n
          3. Multiply\n
          4. Divide\n
          5. Exit\n""")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 5:
                break
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if choice == 1:
                print(f"Result: {sum(num1,num2)}")
            elif choice == 2:
                print(f"Result: {sub(num1,num2)}")
            elif choice == 3:
                print(f"Result: {mul(num1,num2)}")
            elif choice == 4:
                print(f"Result: {div(num1,num2)}")
            else:
                print("Invalid choice")
        except ValueError:
            print("You must enter a number")

if __name__ == "__main__":
    calculator()