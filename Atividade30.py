while True:
    number1 = int(input("Digite um numero: "))
    if number1 == str:
        ("digite um valor valido")
    else:
        break
while True:
    number2 = int(input("Digite outro numero: "))
    if number2 == str:
        ("digite um valor valido")
    else:
        break

if number1 < number2:
    number1 += 1
    while number1 < number2:
        print(number1, end=" ")
        number1 += 1
elif number2 < number1:
    number2 += 1
    while number2 < number1:
        print(number2, end=" ")
        number2 += 1