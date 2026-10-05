"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
a = float(input(f"Qual o valor de A? "))
b = float(input(f"Qual o valor de B? "))
c = float (input(f"Qual o valor de C? "))

if a == 0:
    print(f"Impossivel calcular!")
else:
    delta = (b **2) - ((4 *a) * c )
    if delta < 0:
        print(f"Impossivel calcular! ")
    else:
        r1 = ((-b + delta **0.5)/2*a)
        r2= ((-b + delta **0.5)/2*a)
        print(f"As raízes são {r1: .5f}, {r2: .5f}")