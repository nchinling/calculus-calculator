# Derivative and Integral Calculator

## Overview

The Derivative and Integral Calculator is a simple tool that allows users to calculate the derivative or integral of a mathematical expression in terms of the variable 'x'. The calculator provides both a command-line interface and a web interface using Flask.

## Features

- **Calculate Derivative**: Obtain the derivative of a given mathematical expression.
- **Calculate Integral**: Compute the integral of a given mathematical expression.
- **Web Interface**: Access the calculator through a web browser for user-friendly interaction.

## Command-Line Interface

To use the calculator from the command line:

1. Run the `calculus-calculator.py` script.
2. Select the desired operation (derivative or integral).
3. Enter a mathematical expression in terms of 'x'.
4. View the result.

## Web Interface

To use the calculator through the web interface:

1. Run the `app.py` script using `flask run`
2. Open your web browser and go to `http://127.0.0.1:5000/`.
3. Enter a mathematical expression in the provided form.
4. Check the desired operation (derivative, integral, or both).
5. Click the "Calculate" button.
6. View the result on the web page.

## Technologies Used

- **Python**: Core language for calculator logic.
- **SymPy**: Library for symbolic mathematics in Python.
- **Flask**: Web framework for the web interface.
- **Bootstrap**: Front-end framework for styling.

## How to Run Locally

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the command-line calculator with `python calculus-calculator.py`.
4. Run the web interface with `flask run`.
5. Access the web interface in your browser at `http://127.0.0.1:5000/`.

## Acknowledgments

- The calculator uses SymPy for symbolic mathematics.
- The web interface is built with Flask and Bootstrap.

Feel free to explore the calculator, contribute to its development, or customize it to suit your needs.
