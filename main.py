from src.organizar_termos import organizar_termos_ativos, organizar_termos_si
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
        print(" 1. Organizar termos ativos")
        print(" 2. Organizar termos SI")
        print(" 3. Fazer backup")
        print(" 4. Gerar relatório")
        print(" 5. Sobre")
        print(" 0. Sair")
        print("" + "=" * 60)

        escolha = input("Opção: ").strip()

        if escolha == "1":
            organizar_termos_ativos()
        elif escolha == "2":
            organizar_termos_si()
        elif escolha == "3":
            backup_termos()
        elif escolha == "0":
            print("Fechando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()