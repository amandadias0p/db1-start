# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
resp = "SIM"
while resp == "SIM":
    aluno = input("Digite o nome do(a) aluno(a): ")
    nota1 = int(input("Digite a 1ª nota: "))
    nota2 = int(input("Digite a 2º nota: "))
    media = (nota1 + nota2) / 2
    if media >= 60:
        resultado = "APROVADO(A)"
    else:
        resultado = "REPROVADO(A)"
    print(f"O(A) aluno(a) {aluno} foi {resultado} com media {media}")
    resp = input("Deseja continuar? [SIM/NAO] ").upper()

