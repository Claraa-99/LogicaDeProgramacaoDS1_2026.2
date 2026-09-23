"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
codigo_opcao = int(input(f"Escolha um opção (entre 01 e 05): "))
quantidade = int(input(f"Qual a quantidade consumida? "))
match codigo_opcao:
    case 1: 
        valor_final = 4.0 * quantidade
        print(f"O valor a pagar é de {valor_final: .2f}")

    case 2:
        valor_final= 4.5 * quantidade
        print(f"O valor a pagar é de {valor_final: .2f}")

    case 3:
        valor_final= 5.0 * quantidade
        print(f"O valor a pagar é de {valor_final: .2f}")

    case 4:
        valor_final = 2.0 * quantidade  
        print(f"O valor a pagar é de {valor_final: .2f}")

    case 5:
        valor_final = 1.5 * quantidade
        print(f"O valor a pagar é de {valor_final: .2f}")

    case _:
        print("Opção indisponível!")