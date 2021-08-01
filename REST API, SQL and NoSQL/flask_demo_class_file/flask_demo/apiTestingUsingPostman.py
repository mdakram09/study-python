from flask import Flask, request

app = Flask(__name__)

@app.route("/postmanpost", methods=['POST'])
def math_operation():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])

        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
    return result


@app.route("/postmanget", methods=['GET'])
def math_operation_get():

    operation=request.args.get('operation')
    num1=int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))

    if(operation=='add'):
        r=num1+num2
        result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
    if (operation == 'subtract'):
        r = num1 - num2
        result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'multiply'):
        r = num1 * num2
        result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'divide'):
        r = num1 / num2
        result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
    return result


if __name__ == '__main__':
    # app.run(debug=True, port=8000)
    app.run(debug=True)