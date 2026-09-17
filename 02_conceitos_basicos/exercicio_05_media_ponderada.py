"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota01 = float(input("Qual a nota 01? "))
nota02 = float(input("Qual a nota 02? "))
nota03 = float(input("Qual a nota 03? "))
nota_1 = nota01 * 2
nota_2 = nota02 * 3
nota_3 = nota03 * 5
media = (nota_3 + nota_2 + nota_1) / 3
print(f"Olá, sua média é {media: .2f} ")

