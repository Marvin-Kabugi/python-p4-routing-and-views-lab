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
    numbers = '\n'.join(str(number) for number in range(parameter))
    return numbers + '\n'
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    match operation:
        case "+":
            return str(num1 + num2)
        case "-":
            return str(num1 - num2)
        case "*":
            return str(num1 * num2)
        case "div":
            return str(num1 / num2)
        case "%":
            return str(num1 % num2)
        case _:
            return 'invalid operator'    
        
if __name__ == '__main__':
    app.run(port=5555, debug=True)
