#Обработка аргументов командной строки
import argparse
import sys

def module_argparce():
    parser = argparse.ArgumentParser(description = 'Проект \"Калькулятор\" ')
    parser.add_argument('-o', '--operation', dest = 'operation', metavar = 'Operation', type = str, required = True, help = 'Выберите операцию (Введите addition (+), substraction (-), multiplication (*) или division (/) ). Указывается в формате: -o=x')
    parser.add_argument('-n1', '--number1', dest = 'number1', metavar = 'Number 1', type = float, required = True, help = 'Первое число. Указывается в формате: -n1=x')
    parser.add_argument('-n2', '--number2', dest='number2', metavar = 'Number 2', type = float, required = True, help = 'Второе число. Указывается в формате: -n2=x')
    a = parser.parse_args()
    return(a.operation, a.number1, a.number2)
operation, number1, number2 = module_argparce()

#Определение функций для арифметических действий
def operation_addition(number1, number2):
    return(number1 + number2)
def operation_substraction(number1, number2):
    return(number1 - number2)
def operation_multiplication(number1, number2):
    return(number1 * number2)
def operation_division(number1, number2):
    if number2 == 0:
        return('Делить на ноль нельзя')
    else:
        return(number1 / number2)

#Проверка аргументов
def operand_checking(number1, number2):
    if number1<-1000 or number1>1000:
        return('Введите значение n1 от -1000 до 1000')
    elif number2<-1000 or number2>1000:
        return('Введите значение n2 от -1000 до 1000')
    else:
        return('')

result = operand_checking(number1, number2)
if result != '':
    print(result)
    sys.exit(0)

operation_result = 0
if operation.lower() == 'addition':
    operation_result = operation_addition(number1, number2)
elif operation.lower() == 'substraction':
    operation_result = operation_substraction(number1, number2)
elif operation.lower() == 'multiplication':
    operation_result = operation_multiplication(number1, number2)
elif operation.lower() == 'division':
    operation_result = operation_division(number1, number2)
else: operation_result = 'Неверная операция (Введите addition (+), substraction (-), multiplication (*) или division(/))'
print(operation_result)