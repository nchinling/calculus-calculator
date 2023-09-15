import sympy as sp

x = sp.symbols('x')


def calculate_derivative(expression):
    derivative = sp.diff(expression, x)
    return derivative


def calculate_integral(expression):
    integral = sp.integrate(expression, x)
    return integral


def main():
    print("\nWelcome to the Derivative and Integral Calculator!\n")

    while True:
        print("Select an option:")
        print("1. Calculate Derivative")
        print("2. Calculate Integral")
        print("3. Quit\n")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            expression_str = input(
                "Enter a mathematical expression in terms of x: ")

            try:
                expression = sp.sympify(expression_str)

                derivative = calculate_derivative(expression)
                print(f"Derivative: {derivative}\n")

            except (sp.SympifyError, ValueError):
                print("Invalid input. Please enter a valid mathematical expression.")

        elif choice == '2':
            expression_str = input(
                "Enter a mathematical expression in terms of x: ")

            try:
                expression = sp.sympify(expression_str)

                integral = calculate_integral(expression)
                print(f"Integral: {integral}\n")

            except (sp.SympifyError, ValueError):
                print("Invalid input. Please enter a valid mathematical expression.")

        elif choice == '3':
            print("Goodbye!\n")
            break

        else:
            print("Invalid choice. Please select a valid option (1/2/3).")


if __name__ == "__main__":
    main()
