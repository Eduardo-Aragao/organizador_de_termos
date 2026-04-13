import shutil
from pathlib import Path

pasta_destino_raiz = Path(r"C:\Users\eduardo.silva\Desktop\DEPARTAMENTOS")
pasta_backup = Path(r"C:\Users\eduardo.silva\Desktop\Backup_Termos")


def backup_termos():
    """Realiza backup dos termos organizados."""
    if not pasta_backup.exists():
        pasta_backup.mkdir(parents=True, exist_ok=True)

    destino_backup = pasta_backup / pasta_destino_raiz.name
    if destino_backup.exists():
        print(f"O backup já existe em: {destino_backup}")
        return

    shutil.copytree(pasta_destino_raiz, destino_backup)
    print(f"Backup realizado em: {destino_backup}")
