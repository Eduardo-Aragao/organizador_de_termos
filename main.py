from src.organizar_termos import organizar_termos
from src.backup_termos import backup_termos


def print_banner():
    banner = r"""
  ______ ______  ____   __  __  ____   _____
 |__  __|  ____|  __  \|  \/  |/ __ \ / ____|
    | |  | |__  | |__) | \  / | |  | | (___
    | |  |  __| |  _  /| |\/| | |  | |\___ \
    | |  | |____| | \ \| |  | | |__| |____) |
    |_|  |______|_|  \_\_|  |_|\____/|_____/
"""
    print(banner)
    print("""Bem-vindo ao sistema TERMOS.
Use as opções abaixo para organizar seus arquivos de termos, fazer backup ou gerar relatórios.
""")


def menu():
    while True:
        print_banner()
        print("" + "=" * 60)
        print(" 1. Organizar termos")
        print(" 2. Fazer backup")
        print(" 3. Gerar relatório")
        print(" 4. Sobre")
        print(" 0. Sair")
        print("" + "=" * 60)

        escolha = input("Opção: ").strip()

        match escolha: 
            case "1":
                organizar_termos()
            case "2":
                backup_termos()
            case "3":
                print("Gerar relatório - Em desenvolvimento")
            case "4":
                print("Sobre - Em desenvolvimento")
            case "0":
                print("Saindo... Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()