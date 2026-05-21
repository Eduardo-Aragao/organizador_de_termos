import shutil
from pathlib import Path
from .config import pasta_entrada, pasta_invalidos, pasta_destino_equipamentos, pasta_destino_notebooks, pasta_destino_si, pasta_backup_equipamentos, pasta_backup_notebooks, pasta_backup_si

'''Leitura'''
def leitura_arquivos():
    arquivos = list(pasta_entrada.rglob("*.pdf"))
    if not arquivos:
        print("Nenhum termo foi encontrado na pasta de entrada.")
    return arquivos


'''Fragmentação do nome do arquivo'''
def parse_nome(nome_completo):
    partes = nome_completo.lower().split('-')
    if len(partes) == 3:
        nome, categoria, setor = partes
        return {"nome": nome.strip(), "categoria": categoria.strip(), "setor": setor.strip()}
    else:
        return None


'''Organização dos arquivos'''
def mover_arquivo(arquivo, destino):
    try:
        shutil.move(str(arquivo), str(destino / arquivo.name))
        print(f"Sucesso: {arquivo.name} movido para {destino}")
    except Exception as e:
        print(f"Erro ao mover {arquivo.name}: {e}")
        shutil.move(str(arquivo), str(pasta_invalidos / arquivo.name))
        print(f"{arquivo.name} movido para INVALIDOS devido ao erro.")


def organizar_termos():
    arquivos  = leitura_arquivos()
    SETORES_VALIDOS = ["Abastecimento", "Comercial", "Compras", "Controladoria", "CQ", "Custos", "Diretoria", "DP", "Engenharia", "Expedição", "Ferramentaria",
    "Fiscal", "Inovação", "Logistica", "Manutenção", "Metrologia", "Moinho", "Novos Negocios", "PCP", "Produção", "Qualidade", "Recebimento", "RH", "TI", "Transporte",
    "Tutilabs"]
    
    CATEGORIAS_EQUIPAMENTOS = ["Teclado", "Mouse", "Adaptador-USB", "Monitor", "Suporte-Notebook", "Fone-headset", "Pen-drive", "Fone-headfone", "Kit"]

    CATEGORIAS_SI = ["Midias-removiveis", "VPN", "Smartphone-pessoal"]

    for arquivo in arquivos:
        resultado = parse_nome(arquivo.stem)
        if resultado:
            categoria = resultado["categoria"].capitalize()
            setor = resultado["setor"].capitalize()

            if categoria in CATEGORIAS_EQUIPAMENTOS and setor in SETORES_VALIDOS:
                mover_arquivo(arquivo, pasta_destino_equipamentos)
            elif categoria == "Notebook" and setor in SETORES_VALIDOS:
                mover_arquivo(arquivo, pasta_destino_notebooks)
            elif categoria in CATEGORIAS_SI and setor in SETORES_VALIDOS:
                mover_arquivo(arquivo, pasta_destino_si)
            else:
                print(f"Categoria ou setor inválido para {arquivo.name}. Movendo para INVALIDOS.")
                mover_arquivo(arquivo, pasta_invalidos)
        else:
            print(f"Formato de nome inválido para {arquivo.name}. Movendo para INVALIDOS.")
            mover_arquivo(arquivo, pasta_invalidos)
    
        
                
