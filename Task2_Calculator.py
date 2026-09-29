# CODSOFT INTERNSHIP
# TASK 2 - CALCULATOR

print("==============================")
print("       SIMPLE CALCULATOR")
print("==============================")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter your choice (1/2/3/4): ")

if choice == "1":
    result = num1 + num2
    print("\nResult =", result)

elif choice == "2":
    result = num1 - num2
    print("\nResult =", result)

elif choice == "3":
    result = num1 * num2
    print("\nResult =", result)

elif choice == "4":
    if num2 == 0:
        print("\nError: Cannot divide by zero.")
    else:
        result = num1 / num2
        print("\nResult =", result)

else:
    print("\nInvalid choice. Please select 1, 2, 3, or 4.")

print("\nThank you for using the calculator!")
