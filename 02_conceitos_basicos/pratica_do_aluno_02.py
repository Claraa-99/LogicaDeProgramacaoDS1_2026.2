# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

valor_da_conta = float(input("digite o valor da conta:"))
quant_pessoas = int(input("digite o numero de pessoas:"))

valor_por_pessoa = valor_da_conta / quant_pessoas
print(f"Olá, cada pessoa irá pagar {valor_por_pessoa: .2f}")
