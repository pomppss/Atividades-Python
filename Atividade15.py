nota1 = int(input("Digite a nota do aluno: "))
nota2 = int(input("Digite a nota do aluno: "))

media = int((nota1 + nota2)/2)

if media >= 7 and media <= 9:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")