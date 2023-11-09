while True:
    nota = int(input("digite uma nota de 0 a 10: "))

    if 0 <= nota <= 10:
        break 
    else:
        print("Valor invalido")

print("nota valida")