from classes import *

caio = Aluno('Caio', 1523, 20, 'BB2023PY100', [10, 10, 10, 10])
zeca_pg = Aluno('Zeca Pica-Obesa', 19933, 18, 'BB2023PY991', [10, 10, 10, 10])
sandro = Aluno('Sandro Gol', 9921, 19, 'BB2021JS709', [10, 10, 10, 10])

prof = Professor('Ulpio', 12398121, 25, 'Programação em Python', 3000)

def catraca(aluno):
    ok = str(type(aluno))
    if ok != "<class 'classes.Aluno'>":
        return False
    
    if aluno.matricula.upper() not in alunos_in:
        if aluno.matricula.upper() in matriculas_validas:
            print(f'Bem vindo(a), {aluno.nome}!')
            aluno.frequencia += 1
            alunos_in.append(aluno.matricula.upper())
            return True
        else:
            print(f'Algo deu errado! Consulte a secretaria')
            return False
    else:
            print(f'Volte sempre, {aluno.nome}!')
            alunos_in.remove(aluno.matricula.upper())
            return True
    
catraca(caio)
catraca(zeca_pg)
catraca(caio)
catraca(sandro)

print(f'Temos {len(alunos_in)} alunos dentro da escola agora.')

prova = prof.criarProva()

print(zeca_pg.realizar_prova(prova))

print(prova.notas)