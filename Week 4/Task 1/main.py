from math_operations import apply_operations, power_operation, basic_operations
result_basic = basic_operations(10,5)
print(f'Basic operations result: {result_basic}')
result_power = power_operation(2,3)
print(f'Power operation result: {result_power}')
result_power_modulo = power_operation(2,3, modulo = 5)
print(f'Power operation with modulo: {result_power_modulo}')
operation = [(lambda x,y: x + y, (3,4)), (lambda x,y: x * y, (2,5))]
result_apply = apply_operations(operation)
print(f"Apply operation result: {result_apply}")
