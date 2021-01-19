class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    daniel = Pessoa(nome='Daniel')
    luana = Pessoa(daniel, nome='Luana')
    print(Pessoa.cumprimentar(luana))
    print(id(luana))
    print(luana.cumprimentar())
    print(luana.nome)
    print(luana.idade)
    for filho in luana.filhos:
        print(filho.nome)
    print(luana.filhos)
    luana.sobrenome = 'maria'
    del luana.filhos
    print(luana.__dict__)
    print(daniel.__dict__)
