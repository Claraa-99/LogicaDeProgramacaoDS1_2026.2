"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
quant= 0
soma = 0
for i in range(6):
    num = int(input("Digite um número: "))
    if num > 0:
        quant = quant + 1
        soma = soma + num
    else:
        quant = quant +0

    media = soma / quant

print(f"""A quantidade de números positivos é de: {quant} 
e a média é de : {media}""")