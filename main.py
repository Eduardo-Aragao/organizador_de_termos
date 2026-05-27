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
    
def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def tela_organizar_termos():
    limpar_tela()
    print("Organizando termos...")
    organizar_termos()
    print("Organização concluída. Pressione Enter para voltar ao menu.")
    input()

def tela_backup_termos():
    limpar_tela()
    print("Fazendo backup dos termos organizados...")
    backup_termos()
    print("Backup concluído. Pressione Enter para voltar ao menu.")
    input()

def tela_gerar_relatorio():
    limpar_tela()
    print("Gerar relatório - Em desenvolvimento")
    print("Pressione Enter para voltar ao menu.")
    input()

def tela_sobre():
    limpar_tela()
    print("\nEste projeto consiste em um sistema de Robotic Process Automation (RPA) desenvolvido para otimizar a gestão de documentos digitais do setor de TI. " \
    "O foco é automatizar a triagem, renomeação e backup de termos de responsabilidade de equipamentos, eliminando o erro humano e o tempo gasto em tarefas repetitivas.\n")
    print("Pressione Enter para voltar ao menu.")
    input()


def menu():
    while True:
        limpar_tela()
        print_banner()
        print("" + "=" * 60)
        print(" 1. Organizar termos")
        print(" 2. Fazer backup")
        print(" 3. Gerar relatório - Em desenvolvimento")
        print(" 4. Sobre")
        print(" 0. Sair")
        print("" + "=" * 60)

        escolha = input("Opção: ").strip()

        match escolha: 
            case "1":
                tela_organizar_termos()
            case "2":
                tela_backup_termos()
            case "3":
                tela_gerar_relatorio()
            case "4":
                tela_sobre()
            case "0":
                print("Saindo... Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    limpar_tela()
    menu()