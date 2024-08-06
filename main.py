class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def calcular_idade(self, ano_atual):
        return ano_atual - self.ano_nascimento

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar nova pessoa")
    print("2. Calcular idade")
    print("3. Sair")
    
def main():
    pessoas = []
    ano_atual = 2024
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome da pessoa: ")
            ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
            pessoa = Pessoa(nome, ano_nascimento)
            pessoas.append(pessoa)
            print(f"Pessoa {nome} adicionada com sucesso!")
        
        elif opcao == "2":
            if not pessoas:
                print("Nenhuma pessoa cadastrada.")
            else:
                for idx, pessoa in enumerate(pessoas):
                    print(f"{idx + 1}. {pessoa.nome}")
                escolha = int(input("Escolha uma pessoa pelo número: ")) - 1
                if 0 <= escolha < len(pessoas):
                    idade = pessoas[escolha].calcular_idade(ano_atual)
                    print(f"{pessoas[escolha].nome} tem {idade} anos.")
                else:
                    print("Escolha inválida.")
        
        elif opcao == "3":
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
