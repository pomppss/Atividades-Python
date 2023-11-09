produto1 = int(input("Digite o preço do produto: "))
produto2 = int(input("Digite o preço do produto: "))
produto3 = int(input("Digite o preço do produto: "))

if produto1 < produto2 and produto1 < produto3:
    print("O pruduto mais barato custa", produto1)
elif produto2 < produto1 and produto2 < produto3:
    print("O pruduto mais barato custa ", produto2)
elif produto3 < produto2 and produto3 < produto1:
    print("O pruduto mais barato custa ", produto3)