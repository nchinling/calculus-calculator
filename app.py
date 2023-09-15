from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)
app.debug = True


x = sp.symbols('x')


def calculate_derivative(expression):
    derivative = sp.diff(expression, x)
    return derivative


def calculate_integral(expression):
    integral = sp.integrate(expression, x)
    return integral


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        expression_str = request.form['expression']
        operation = request.form['operation']

        try:
            expression = sp.sympify(expression_str)

            if operation == 'derivative':
                result = str(calculate_derivative(expression))
                print("Derivative Result:", result)
            elif operation == 'integral':
                result = str(calculate_integral(expression))
        except (sp.SympifyError, ValueError):
            result = "Invalid input. Please enter a valid mathematical expression."

    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
