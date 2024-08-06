class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def calcular_idade(self, ano_atual):
        return ano_atual - self.ano_nascimento


pessoa1 = Pessoa("Maria", 1990)
ano_atual = 2024
idade = pessoa1.calcular_idade(ano_atual)
print(f"{pessoa1.nome} tem {idade} anos.")
