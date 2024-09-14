from flask import Flask, request, render_template, jsonify
import math

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Example: Addition API
@app.route('/add', methods=['POST'])
def add():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 + num2
    return jsonify(result=result)

# Example: Factorial API
@app.route('/factorial', methods=['POST'])
def factorial():
    number = int(request.form['number'])
    result = math.factorial(number)
    return jsonify(result=result)
# problem - 5 Modulus 
@app.route("/modulus",method=["POST"])

def modulo():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    result = number1 % number2
    return jsonify(result=result)

<<<<<<< HEAD
@app.route('/multiply', methods=['POST'])
def multiply():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 * num2
    return jsonify(result=result)    

=======
def sqrt():
    num = int(input("Enter a Number: "))
    if num<0:
        return "not possible"
    return math.sqrt(num)

>>>>>>> 9a744ae9c9d3956fc4fea9a84438d67d128be768
# You can add more routes for each math function
# for example, multiplication, square roots, etc.

if __name__ == '__main__':
    app.run(debug=True)
