while True:
    nome = input("Digite o nome do usuario: ")
    senha = input("Digite sua senha: ")

    if senha != nome:
        print("Cadastro valido")
    else:
        print("A senha não pode ser a mesma do usuario")