number1 = int(input("Digite um valor: "))
number2 = int(input("Digite um valor: "))
number3 = int(input("Digite um valor: "))

if number1 > number2 and number1 > number3:
    print(number1)
elif number2 > number1 and number2 > number3:
    print(number2)
elif number3 > number2 and number3 > number1:
    print(number3)