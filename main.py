from src.organizar_termos import organizar_termos_ativos, organizar_termos_si
from src.backup_termos import backup_termos


def menu():
    while True:
        print("\n" + "=" * 40)
        print("1. Organizar termos ativos")
        print("2. Organizar termos SI")
        print("3. Fazer backup")
        print("4. Sair")
        print("=" * 40)

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            organizar_termos_ativos()
        elif escolha == "2":
            organizar_termos_si()
        elif escolha == "3":
            backup_termos()
        elif escolha == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()