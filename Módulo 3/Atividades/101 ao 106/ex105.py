def notas(*args, sit: bool = False):

    aluno = {
        'total': len(args),
        'maior': max(args),
        'menor': min(args),
        'média': round(sum(args) / len(args), 1),
    }

    if sit:
        aluno['situação'] = 'Aprovado' if aluno['média'] >= 6 else 'Reprovado'

    return aluno


resp = notas(5, 6, 7, 10, 0, 5, 6, 9, sit=True)
print(resp)
