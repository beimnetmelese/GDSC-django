def basic_operations(num1, num2):
    try:
        sum = num1 + num2
        substruct = num1 - num2
        divide = num1 / num2
        multipliy = num1 * num2
        operations = {
            "sum": sum,
            "substruct": substruct,
            "divide": divide,
            "multiply": multipliy
            }
        return operations
    except ZeroDivisionError:
        print("you can't divide integers by zero")
    
def power_operation(base, exponent, **kwargs):
    try:
        power = 1
        for num in range(exponent):
            power = power * base
        if "modulo" in kwargs:
            power = power % kwargs["modulo"]
        return power
    except ZeroDivisionError:
        print("you can't divide integers by zero")

def apply_operations(operations_lists):
    return list(map(lambda operator: operator[0](*operator[1]), operations_lists))
def apply(operation_list):
    result = []
    for i in range(len(operation_list)):
        result.append(list(map(operation_list[i][0],operation_list[i][1])))
    return result

operation = [(lambda x,y: x + y, (3,4)), (lambda x,y: x * y, (2,5))]
print(apply(operation))

    


