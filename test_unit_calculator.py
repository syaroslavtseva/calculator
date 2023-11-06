#from calculator import operation_addition
import calculator
calculator.module_argparce(['--operation', 'addition'], ['--number1','278.1'], ['--number2', '972.45'])

#test def operation_addition(number1, number2):(++float),(+-),(--),0
def test_operation_addition():
   # calculator.args.operation = 'addition'
    #calculator.args.number1 = 278.1
    #calculator.args.number2 = 972.45
    assert operation_addition(12, 34) == 46
test_operation_addition()





#test def operation_substraction(number1, number2): (++float),(+-),(--),0
#test def operation_multiplication(number1, number2): (++float),(+-),(--), 0
#test def operation_division(number1, number2): (++float),(+-),(--), 0
#test def operand_checking(number1, number2):(n1>1000), (n1<-1000), (n1>1000), (n1<-1000)(n1>1000,n2<-1000)