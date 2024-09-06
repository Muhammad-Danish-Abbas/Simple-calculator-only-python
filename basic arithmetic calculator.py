# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    # Check if the denominator is not zero to avoid division by zero
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main function to display the options and get user input
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is one of the four options
        if choice in ['1', '2', '3', '4']:
            try:
                # Input the two numbers from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handle invalid input for numbers
                print("Invalid input. Please enter numeric values.")
                continue

            # Perform the operation based on user's choice
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        else:
            # Handle invalid choices
            print("Invalid input. Please select a valid option.")

        # Ask the user if they want to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

# Call the calculator function to start the program
calculator()
