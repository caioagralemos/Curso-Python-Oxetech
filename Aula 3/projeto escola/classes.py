class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, cpf, idade, matricula, notas):
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.notas = notas
        self.frequencia = 0
    
    def realizar_prova(self, prova):
        respostas = []
        acertos = 0
        print(f'\nOlá, {self.nome}! A partir de agora você está realizando a prova "{prova.assunto}".\n\n')
        for i in range(len(prova.questoes)):
            alternativa = input(f'Insira a alternativa da questão {i + 1}: ').upper()
            while alternativa not in 'ABCDE':
                alternativa = input(f'É necessário que sua resposta esteja entre A, B, C, D ou E\nInsira a alternativa da questão {i+1}: ').upper()
            respostas.append(alternativa)
        for i in range(len(prova.questoes)):
            if prova.questoes[i] == respostas[i]:
                acertos += 1
        
        nota = (acertos / len(prova.questoes)) * 10
        self.notas.append(nota)
        prova.notas.append({'aluno': self, 'nota': nota})
        return nota


class Professor(Pessoa):
    def __init__(self, nome, cpf, idade, materia, salario):
        super().__init__(nome, cpf, idade)
        self.materia = materia
        self.salario = salario
    
    def planejarAula(self):
        print(f'O {self.nome} está planejando a aula.')
    
    def criarProva(self):
        print(f'Olá, {self.nome}! Vamos te ajudar a criar uma nova prova.\n\n')
        assunto = input('Nos diga o assunto da prova: ')
        try:
            qtd_questoes = int(input('E a quantidade de questões? '))
        except:
            print('Algo deu errado. Tente novamente')
        respostas = []
        for i in range(qtd_questoes):
            alternativa = input(f'Insira a alternativa correta da questão {i + 1}: ').upper()
            while alternativa not in 'ABCDE':
                alternativa = input(f'É necessário que a alternativa correta esteja entre A, B, C, D ou E\nInsira a alternativa da questão {i+1}: ').upper()
            respostas.append(alternativa)
        prova = Prova(self, assunto, respostas)
        return prova

    
class Turma:
    def __init__(self, capacidade, id, professor, materia):
        self.capacidade = capacidade
        self.id = id
        self.professor = professor
        self.materia = materia

class Prova:
    def __init__(self, professor, assunto, questoes):
        self.professor = professor
        self.assunto = assunto
        self.questoes = questoes
        self.notas = []

matriculas_validas = ['BB2021JS709', 'AD2022PY991', 'GL2020ND000', 'VE2023AO212', 'BB2023PY991', 'BB2022IN123', 'MD2023GT134', 'BB2023PY100']
alunos_in = []