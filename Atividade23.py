while True:
    nome = input("Digite seu nome(mais que tres caracteres): ")
    if len(nome) <= 3:
        print("É necessario mais de tres caracteres, digite novamente")
    else:
        break

while True:
    idade = int(input("Digite sua idade(idade entre 0 e 150): "))
    if 0 <= idade <= 150:
        break
    else:
        print("Idade invalida, digite novamente")

while True:
    salario = int(input("Digite seu salario: "))
    if salario <= 0:
        print("Digite um salario maior que zero")
    else:
        break

while True:
    estado_civil = input("Digite seu estado civil -- 's', 'c', 'v' ou 'd': ").lower()
    if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
        break
    else:
        print("valor invalido, digite novamente!")

while True:
    sexo = input("digite sua sexualidade -- 'f'- feminino e 'm'-masculino: ").lower()
    if sexo == "f" or sexo == "m":
        break
    else:
        print("valor invalido, digite novamente")

print(f"nome: {nome}\n idade: {idade}\n salario: {salario}\n estado civil: {estado_civil}\n sexo: {sexo}")