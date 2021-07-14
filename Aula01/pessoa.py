from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome , idade, comendo= False, falando= False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        variavel = 'valor'

    def outro_metodo(self):
        print(self.nome)

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return
        if self.falando:
            print(f'{self.nome} esta falando, não é possivel comer.')
            return
        else:
            print(f'{self.nome} está comendo {alimento}.')
            self.comendo = True

    def pararcomer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer!')
        self.comendo = False


    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre: {assunto}')
        self.falando = True

    def parardefalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        print(f'{self.nome} parou de falar.')

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
