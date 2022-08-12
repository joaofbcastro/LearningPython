def notas(*args, sit: bool = False):
    """Uma função para analisar notas e situações de alunos.

    Parameters
    ----------
        args: Uma ou mais notas do aluno
        sit: (Opcional) Indica se deve ser incluída ou não a situação do aluno

    Returns
    -------
        dict: Dicionário com as informações do aluno.
    """

    aluno = {
        'total': len(args),
        'maior': max(args),
        'menor': min(args),
        'média': round(sum(args) / len(args), 1),
    }

    if sit:
        aluno['situação'] = 'Aprovado' if aluno['média'] >= 6 else 'Reprovado'

    return aluno


resp = notas(5, 6, 7, 10, 0, 5, 6, 9)
print(resp)
