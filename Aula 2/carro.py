class Carro:
    def __init__(self, modelo, ano, cor, portas, velocidade_max):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.portas = portas
        self.velocidade_max = velocidade_max
        self.motor = False
        self.velocidade = 0
    
    def __str__(self):
        return f'{self.modelo} {self.ano} {self.cor} {self.portas} portas'

    def buzinar(self):
        print(f'OLHA O {self.modelo.upper()} BUZINANDO')

    def chave(self):
        if self.motor:
            self.motor = False
            self.velocidade = 0
            print(f"'barulho de motor parou'... O {self.modelo} agora vai descansar um pouco!")
        else:
            self.motor = True
            print(f"'barulho de motor ligando'... O {self.modelo} agora tá ligado!")
        return True
    
    def acelerar(self, velocidade=10):
        if self.motor:
            if self.velocidade >= self.velocidade_max:
                print(f'O {self.modelo} já tá na velocidade máxima!')
            elif self.velocidade + velocidade > self.velocidade_max:
                self.velocidade = self.velocidade_max
                print(f'O {self.modelo} tava acelerando e atingiu a velocidade máxima! Nova velocidade {self.velocidade}km/h')
            else:
                self.velocidade = self.velocidade + velocidade
                print(f'O {self.modelo} tá acelerando! Nova velocidade {self.velocidade}km/h')
            return True
        else:
            print(f'O {self.modelo} está desligado.')
            return False
    
    def frear(self, velocidade=10):
        if self.motor:
            if velocidade >= self.velocidade:
                self.velocidade = 0
                print(f'O {self.modelo} parou totalmente e agora está estacionado.')
            else:
                self.velocidade = self.velocidade - velocidade
                print(f'O {self.modelo} tá freando! Nova velocidade {self.velocidade}km/h')
            return True
        else:
            print(f'O {self.modelo} está desligado.')
            return False
    
    def status(self):
        if self.motor:
            if self.velocidade > 0:
                print(f'O {self.modelo} está ligado e andando a {self.velocidade}km/h.')
            else:
                print(f'O {self.modelo} está ligado e estacionado.')
    
    def corrida(self, rival):
        print('\n...... INÍCIO DA CORRIDA! ......\n')
        if rival.motor == False and self.motor == False:
            print('Não tem como fazer uma corrida com dois carros parados, pô.')
            print('\n...... FIM DA CORRIDA! ......\n')
            return False
        if rival.motor == False or rival.velocidade <= 0:
            print(f'O {rival.modelo} tá parado e não pode correr assim, né?')
            print('\n...... FIM DA CORRIDA! ......\n')
            return False
        if self.motor == False or self.velocidade <= 0:
            print(f'O {self.modelo} tá parado e não pode correr assim, né?')
            print('\n...... FIM DA CORRIDA! ......\n')
            return False

        if rival.velocidade > self.velocidade:
            print(f'O fi da peste do {rival.modelo} tá chutado a {rival.velocidade}km/h tá dando um pau no {self.modelo}, que tá só a {self.velocidade}km/h!')
        elif rival.velocidade < self.velocidade:
            print(f'O {self.modelo} tá chutado a {self.velocidade}km/h tá dando um pau no {rival.modelo}, que tá só a {rival.velocidade}km/h!')
        else:
            print(f'Impressionante! O {self.modelo} e o {rival.modelo} tão pau a pau nesse racha e cruzaram a linha no mesmo tempo, os dois a {self.velocidade}km/h!')
        print('\n...... FIM DA CORRIDA! ......\n')
        return True


uno_com_escada = Carro('Uno Mille', 2003, 'Prata', 4, 130)

print(uno_com_escada)
# uno_com_escada.buzinar()
uno_com_escada.chave()
uno_com_escada.acelerar(100)
uno_com_escada.status()
# uno_com_escada.chave()

ferrari_azul = Carro('Hb20', 2023, 'Azul', 4, 200)
ferrari_azul.chave()
ferrari_azul.acelerar(77)

uno_com_escada.corrida(ferrari_azul)
