# TODO: Implemente o menu utilizando match-case ou elif

print(f"""
Opção 1: Consultar livro
Opção 2: Realizar empréstimo
Opção 3: Devolver livro
""")
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))



match opcao:
    case 1:
        print("Consultar livro.")
    case 2:
        print("Realizar empréstimo.")
    case 3:
        print("Devolver livro.")
    case _:
        print("Opção indísponivel!")