class Pessoa:
    def __init__(self, nome = None, idade =35):
        self.nome = nome


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Daniel')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)
