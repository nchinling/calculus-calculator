# Derivatives and Integral Calculator

This is a simple calculator for computing derivatives and integrals. It uses SymPy, a Python library for symbolic computation. It can be run either from the command line or through a web interface. The web interface is implemented using Flask.

## Usage

### Flask (Web Interface)

1. **Install Flask:** If you haven't installed Flask, you can do so using the following command:

    ```bash
    pip install flask
    ```

2. **Run the Calculator:**
    - Navigate to the project directory in your terminal.
    - Run the following command to start the Flask application:

        ```bash
        flask run
        ```

    - Open your web browser and go to `http://127.0.0.1:5000/`.
    - Use the provided web form to input the function with respect to 'x', and the calculator will display the result on the webpage.

### Command Line

1. **Run the Calculator:**
    - Open a terminal.
    - Navigate to the project directory.
    - Run the following command:

        ```bash
        python calculus-calculator.py
        ```

2. **Input Instructions:**
    - You will be prompted to choose between computing derivatives and integrals.
    - Follow the on-screen instructions to input the function (with respect to 'x').
    - The calculator will display the result in the terminal.

## Notes

- Ensure you have Python installed on your system.

