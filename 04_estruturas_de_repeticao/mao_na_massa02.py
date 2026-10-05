soma = 0

num_usu = int(input(f"Digite um número: "))
while num_usu != 0:
    soma =num_usu+soma
    num_usu =  int(input(f"Digite um número: "))
    continue

print(f"Somando os números...")
print(f"A soma dos números digitados é {soma}!")
