def calculator():
    print("\n--- SMART CALCULATOR ---")

    while True:
        print("\nChoose an option")
        print("1. Basic Calculator")
        print("2. Age Calculator")
        print("3. Percentage Calculator")
        print("4. BMI Calculator")
        print("5. Unit Converter")
        print("6. Discount Calculator")
        print("7. Electricity Bill")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            basic_calculator()

        elif choice == "2":
            age_calculator()

        elif choice == "3":
            percentage_calculator()

        elif choice == "4":
            bmi_calculator()

        elif choice == "5":
            unit_converter()

        elif choice == "6":
            discount_calculator()

        elif choice == "7":
            electricity_bill()

        elif choice == "8":
            print("Thank you!")
            break

        else:
            print("Invalid Choice!")


def basic_calculator():
    print("\n--- Basic Calculator ---")

    num1 = float(input("Enter First Number: "))
    operator = input("Enter Operator (+ - * / % // **): ")
    num2 = float(input("Enter Second Number: "))

    if operator == "+":
        print("Answer =", num1 + num2)

    elif operator == "-":
        print("Answer =", num1 - num2)

    elif operator == "*":
        print("Answer =", num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print("Answer =", num1 / num2)
        else:
            print("Cannot divide by zero")

    elif operator == "%":
        print("Answer =", num1 % num2)

    elif operator == "//":
        print("Answer =", num1 // num2)

    elif operator == "**":
        print("Answer =", num1 ** num2)

    else:
        print("Invalid Operator")


def age_calculator():
    print("\n--- Age Calculator ---")

    birth_year = int(input("Enter Birth Year: "))
    current_year = int(input("Enter Current Year: "))

    age = current_year - birth_year

    print("Your Age is", age, "years")


def percentage_calculator():
    print("\n--- Percentage Calculator ---")

    total = 0

    for i in range(1, 6):
        marks = float(input(f"Enter Marks of Subject {i}: "))
        total += marks

    percentage = total / 5

    print("Total =", total)
    print("Percentage =", percentage)

    if percentage >= 40:
        print("Result : PASS")
    else:
        print("Result : FAIL")


def bmi_calculator():
    print("\n--- BMI Calculator ---")

    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (m): "))

    bmi = weight / (height ** 2)

    print("BMI =", round(bmi, 2))

    if bmi < 18.5:
        print("Underweight")

    elif bmi < 25:
        print("Normal")

    elif bmi < 30:
        print("Overweight")

    else:
        print("Obese")


def unit_converter():
    print("\n--- Unit Converter ---")

    print("1. KM to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. KG to Pounds")
    print("4. Inches to CM")

    choice = input("Choose: ")

    if choice == "1":
        km = float(input("Enter KM: "))
        print("Miles =", km * 0.621371)

    elif choice == "2":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit =", (c * 9/5) + 32)

    elif choice == "3":
        kg = float(input("Enter KG: "))
        print("Pounds =", kg * 2.20462)

    elif choice == "4":
        inch = float(input("Enter Inches: "))
        print("CM =", inch * 2.54)

    else:
        print("Invalid Choice")


def discount_calculator():
    print("\n--- Discount Calculator ---")

    price = float(input("Enter Price: "))
    discount = float(input("Enter Discount %: "))

    discount_amount = (price * discount) / 100
    final_price = price - discount_amount

    print("Discount =", discount_amount)
    print("Final Price =", final_price)


def electricity_bill():
    print("\n--- Electricity Bill ---")

    units = int(input("Enter Units: "))

    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    print("Total Bill = ₹", bill)


calculator()  