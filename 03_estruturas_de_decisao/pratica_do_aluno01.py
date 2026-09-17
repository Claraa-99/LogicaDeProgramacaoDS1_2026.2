media_aluno = float(input("Qual a media do aluno? "))
frequencia = int(input("Qual a média percentual? "))

media_final = media_aluno >= 6.0
frequencia_final = frequencia >=75

resultado = media_final and frequencia_final
print(f"O aluno passou de ano? {resultado}")