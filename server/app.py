#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(num) for num in range(parameter)) + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1 = float(num1)
    num2 = float(num2)
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero", 400
        result = num1 / num2
        return str(result)  
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    
    if result.is_integer():
        return str(int(result))
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
