#関数を戻り値として返す
def get_operator(operator):
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def division(x, y):
        return x / y
    def multiply(x, y):
        return x * y
    
    if operator == '+':
        return add
    elif operator == '-':
        return subtract
    elif operator == '/':
        return division
    elif operator == '*':
        return multiply
    else:
        return None

operation = get_operator('/')
result = operation(10, 2)
print(result)