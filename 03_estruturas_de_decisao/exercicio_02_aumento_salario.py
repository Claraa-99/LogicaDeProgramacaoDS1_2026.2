"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario = float(input(f"Qual o seu salário? "))
if salario <= 400: 
    percentual = 1.5
elif salario <= 800:
   percentual = 1.2
elif salario <= 1200:
    percentual = 1.0
elif salario <= 2000:
    percentual = 0.07
else :
    percentual= 0.04

reajuste = salario * percentual
novo_salario = reajuste + salario

print(f"O novo salário é de {novo_salario}!")
print(f"O valor do reajuste é de {reajuste}!")
print(f"O percentual é de {percentual * 10}%!")