alunos = []
while True:
    nome = str(input("\nNorm: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    alunos.append([nome, nota1, nota2])
    var = input("Quer continuar? [S/N]: ").upper().strip()[0]
    if var in "N":
        break
print(f"{'//':-^25}\n{'No.':5}{'NOME':10}{'MÉDIA':>8}\n{'--':-^25}")
for pos, aluno in enumerate(alunos):
    print(f"{pos:<5}{aluno[0]:10}{(aluno[1]+aluno[2])/2:>8.1f}")
while True:
    aluno = str(input("Mostrar as notas de qual aluno? ('Cancelar' interrompe): ")).lower()[0]
    if aluno in 'c':
        break
    aluno = int(aluno, 0)
    print(f'As notas de {alunos[aluno][0]} são {alunos[aluno][1]} e {alunos[aluno][2]}.\n{"-":-^25}')
