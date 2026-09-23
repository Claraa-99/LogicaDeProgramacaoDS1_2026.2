"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
idade = int(input(f"Qual a sua idade? "))

if idade <12:
    valor_final = 100 - (100 * 0.5)
    print(f"O bilhete é Infantil! ")
    print(f"O valor a pagar é de R${valor_final: .2f} ")

elif idade >= 60 :
    valor_final = 100 - 100
    print(f"O bilhete é Melhor Idade! ")
    print(f"O valor a pagar é de {valor_final: .2f} ")
else:
    valor_final = 100 -0
    print(f"O valor a pagar é de {valor_final: .2f} ")
