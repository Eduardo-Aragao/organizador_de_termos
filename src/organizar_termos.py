import shutil
from pathlib import Path
from .config import pasta_entrada, pasta_invalidos, pasta_destino_equipamentos, pasta_destino_notebooks, pasta_destino_si, pasta_backup_equipamentos, pasta_backup_notebooks, pasta_backup_si

'''Leitura dos arquivos'''
def leitura_arquivos():
    arquivos = list(pasta_entrada.rglob("*.pdf"))
    if not arquivos:
        print("Nenhum termo foi encontrado na pasta de entrada.")
    return arquivos


'''Fragmentação do nome do arquivo através do formato esperado: nome-categoria-setor.pdf'''
def parse_nome(nome_completo):
    partes = nome_completo.lower().rsplit('-', 2)
    if len(partes) == 3:
        nome, categoria, setor = partes
        return {"nome": nome.strip(), "categoria": categoria.strip(), "setor": setor.strip()}
    else:
        return None


'''Organização dos arquivos'''
def garantir_pasta(destino):
    destino.mkdir(parents=True, exist_ok=True)

'''Responsável por mover os arquivos para o destino correto ou para a pasta de inválidos em caso de erro ou formato incorreto'''
def mover_arquivo(arquivo, destino):
    garantir_pasta(destino)
    try:
        shutil.move(str(arquivo), str(destino / arquivo.name))
        print(f"Sucesso: {arquivo.name} movido para {destino}")
    except Exception as e:
        print(f"Erro ao mover {arquivo.name}: {e}")
        garantir_pasta(pasta_invalidos)
        shutil.move(str(arquivo), str(pasta_invalidos / arquivo.name))
        print(f"{arquivo.name} movido para INVALIDOS devido ao erro.")

'''Função principal para organizar os termos e validar os arquivos de acordo com as categorias e setores pré-definidos'''
def organizar_termos():
    arquivos  = leitura_arquivos()
    SETORES_VALIDOS = ["abastecimento", "comercial", "compras", "controladoria", "cq", "custos", "diretoria", "dp", "engenharia", "expedição", "ferramentaria",
    "fiscal", "inovação", "logistica", "manutenção", "metrologia", "moinho", "novos negócios", "pcp", "produção", "qualidade", "recebimento", "rh", "ti", "transporte",
    "tutilabs"]
    
    CATEGORIAS_EQUIPAMENTOS = ["teclado", "mouse", "adaptador", "monitor", "suporte", "headset", "pendrive", "headfone", "kit"]

    CATEGORIAS_SI = ["midias-removiveis", "vpn", "smartphone"]

    for arquivo in arquivos:
        resultado = parse_nome(arquivo.stem)
        if resultado:
            categoria = resultado["categoria"].lower()
            setor = resultado["setor"].lower()

            if categoria in CATEGORIAS_EQUIPAMENTOS and setor in SETORES_VALIDOS:
                mover_arquivo(arquivo, pasta_destino_equipamentos)
            elif categoria == "notebook" and setor in SETORES_VALIDOS:
                mover_arquivo(arquivo, pasta_destino_notebooks)
            elif categoria in CATEGORIAS_SI and setor in SETORES_VALIDOS:
                mover_arquivo(arquivo, pasta_destino_si)
            else:
                print(f"Categoria ou setor inválido para {arquivo.name} (categoria={categoria}, setor={setor}). Movendo para INVALIDOS.")
                mover_arquivo(arquivo, pasta_invalidos)
        else:
            print(f"Formato de nome inválido para {arquivo.name}. Movendo para INVALIDOS.")
            mover_arquivo(arquivo, pasta_invalidos)
    
        
                
