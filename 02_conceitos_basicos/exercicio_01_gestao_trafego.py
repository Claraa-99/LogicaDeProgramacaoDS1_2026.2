"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_campanha = float(input("Qual o valor investido?"))
cliques = int(input("Quantos cliques teve?"))
custo_por_clique = valor_campanha / cliques
print(f"O CPC (Custo POr Clique) é de R$ {custo_por_clique: .2f}")
