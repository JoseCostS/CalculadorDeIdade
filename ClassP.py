class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def calcular_idade(self, ano_atual):
        return ano_atual - self.ano_nascimento
