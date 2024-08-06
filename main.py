# main.py
from pessoa import Pessoa as ClassP

def menu():
    pessoas = []
    ano_atual = 2024

    while True:
        print("\nMenu:")
        print("1. Adicionar pessoa")
        print("2. Calcular idade de uma pessoa")
        print("3. Listar todas as pessoas")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome: ")
            ano_nascimento = int(input("Digite o ano de nascimento: "))
            pessoa = ClassP(nome, ano_nascimento)
            pessoas.append(pessoa)
            print(f"{nome} adicionada com sucesso!")

        elif escolha == '2':
            nome = input("Digite o nome da pessoa: ")
            pessoa_encontrada = next((p for p in pessoas if p.nome == nome), None)
            if pessoa_encontrada:
                idade = pessoa_encontrada.calcular_idade(ano_atual)
                print(f"{pessoa_encontrada.nome} tem {idade} anos.")
            else:
                print("Pessoa não encontrada.")

        elif escolha == '3':
            if pessoas:
                for pessoa in pessoas:
                    idade = pessoa.calcular_idade(ano_atual)
                    print(f"{pessoa.nome} nasceu em {pessoa.ano_nascimento} e tem {idade} anos.")
            else:
                print("Nenhuma pessoa cadastrada.")

        elif escolha == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()