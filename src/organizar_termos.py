import shutil
from pathlib import Path


'''LEMBRETE: CONFIGURAR OS CAMINHOS CONFORME O SERVIDOR DE PASTAS'''
pasta_entrada = Path(r"C:\Users\eduardo.silva\Desktop\Teste de RPA")
pasta_destino_ativos_raiz = Path(r"C:\Users\eduardo.silva\Desktop\DEPARTAMENTOS")
pasta_invalidos_ativos = pasta_destino_ativos_raiz / "INVALIDOS"
pasta_destino_si_raiz = Path(r"C:\Users\eduardo.silva\Desktop\SI")
pasta_invalidos_si = pasta_destino_si_raiz / "INVALIDOS"


def organizar_termos_ativos():
    """Organiza os termos em pastas por setor."""
    if not pasta_destino_ativos_raiz.exists():
        pasta_destino_ativos_raiz.mkdir(parents=True, exist_ok=True)
    if not pasta_invalidos_ativos.exists():
        pasta_invalidos_ativos.mkdir(parents=True, exist_ok=True)

    contador = 0

    for arquivo in pasta_entrada.rglob("*.pdf"):
        contador += 1
        try:
            nome_completo = arquivo.stem
            partes = nome_completo.split('-')

            if len(partes) == 3:
                '''Categorias = VPN, Mídias Removíveis, Monitores, Periféricos, Notebooks'''
                nome, categoria, setor = partes
                caminho_setor = pasta_destino_ativos_raiz / setor

                if not caminho_setor.exists():
                    caminho_setor.mkdir(parents=True, exist_ok=True)

                shutil.move(str(arquivo), str(caminho_setor / arquivo.name))
                print(f"Sucesso: {nome} movido para {setor}")
            else:
                shutil.move(str(arquivo), str(pasta_invalidos / arquivo.name))
                print(f"Arquivo inválido movido para INVALIDOS: {arquivo.name}")
        except Exception as e:
            print(f"Erro ao processar {arquivo.name}: {e}")

    if contador == 0:
        print("Nenhum termo foi encontrado na pasta de entrada.")

    def organizar_termos_si():
        if not pasta_destino_si_raiz.exists():
        pasta_destino_si_raiz.mkdir(parents=True, exist_ok=True)
    if not pasta_invalidos_si.exists():
        pasta_invalidos_si.mkdir(parents=True, exist_ok=True)

    contador = 0

    for arquivo in pasta_entrada.rglob("*.pdf"):
        contador += 1
        try:
            nome_completo = arquivo.stem
            partes = nome_completo.split('-')

            if len(partes) == 3:
                '''Categorias = VPN, Mídias Removíveis, Monitores, Periféricos, Notebooks'''
                nome, categoria, setor = partes
                caminho_setor = pasta_destino_ativos_raiz / setor

                if not caminho_setor.exists():
                    caminho_setor.mkdir(parents=True, exist_ok=True)

                shutil.move(str(arquivo), str(caminho_setor / arquivo.name))
                print(f"Sucesso: {nome} movido para {setor}")
            else:
                shutil.move(str(arquivo), str(pasta_invalidos / arquivo.name))
                print(f"Arquivo inválido movido para INVALIDOS: {arquivo.name}")
        except Exception as e:
            print(f"Erro ao processar {arquivo.name}: {e}")

    if contador == 0:
        print("Nenhum termo foi encontrado na pasta de entrada.")
