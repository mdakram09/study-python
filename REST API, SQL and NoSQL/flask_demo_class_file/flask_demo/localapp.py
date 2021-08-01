

def math_operation(num1, num2, operation):
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



output = math_operation(5, 6, 'add')
print(output)