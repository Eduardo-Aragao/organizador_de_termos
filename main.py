from src.organizar_termos import organizar_termos
from src.backup_termos import backup_termos


def menu():
    while True:
        print("\n" + "=" * 40)
        print("1. Organizar termos")
        print("2. Fazer backup")
        print("3. Sair")
        print("=" * 40)

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            organizar_termos()
        elif escolha == "2":
            backup_termos()
        elif escolha == "3":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()