def notas(*num, sit=False):
    '''
    :parametro num: nota dos alunos de uma turma
    :parametro sit: verifica se quer ou não saber a situação da turma no dicionário
    :return: dicionário com as informações da turma
    '''
    import statistics
    nota = {'total': len(num), 'maior nota': max(num), 'menor nota': min(num), 'média': statistics.mean(num)}
    if sit == True:
        if statistics.mean(num) > 7.0:
            nota['situação'] = 'boa'
        else:
            nota['situação'] = 'ruim'
    print(nota)
notas(10, 10, 10, 10, 10, 10, sit=True)