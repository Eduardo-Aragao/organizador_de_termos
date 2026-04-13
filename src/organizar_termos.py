import shutil
from pathlib import Path

pasta_entrada = Path(r"C:\Users\eduardo.silva\Desktop\Teste de RPA")
pasta_destino_raiz = Path(r"C:\Users\eduardo.silva\Desktop\DEPARTAMENTOS")
pasta_invalidos = pasta_destino_raiz / "INVALIDOS"


def organizar_termos():
    """Organiza os termos em pastas por setor."""
    if not pasta_destino_raiz.exists():
        pasta_destino_raiz.mkdir(parents=True, exist_ok=True)
    if not pasta_invalidos.exists():
        pasta_invalidos.mkdir(parents=True, exist_ok=True)

    contador = 0

    for arquivo in pasta_entrada.rglob("*.pdf"):
        contador += 1
        try:
            nome_completo = arquivo.stem
            partes = nome_completo.split('-')

            if len(partes) == 3:
                nome, categoria, setor = partes
                caminho_setor = pasta_destino_raiz / setor

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
