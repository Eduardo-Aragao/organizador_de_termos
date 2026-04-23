import shutil
from pathlib import Path
import datetime
from .config import pasta_destino_ativos_raiz, pasta_destino_si_raiz, pasta_backup


def backup_termos_ativos():
    """Realiza backup dos termos de ativos organizados."""
    if not pasta_backup.exists():
        pasta_backup.mkdir(parents=True, exist_ok=True)

    destino_backup = pasta_backup / pasta_destino_ativos_raiz.name
    if destino_backup.exists():
        print(f"O backup já existe em: {destino_backup}")
        return
    shutil.copytree(pasta_destino_ativos_raiz, destino_backup)
    print(f"Backup realizado em: {destino_backup}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def backup_termos_si():
    """Realiza backup dos termos de SI organizados."""
    if not pasta_backup.exists():
        pasta_backup.mkdir(parents=True, exist_ok=True)

    destino_backup = pasta_backup / pasta_destino_si_raiz.name
    if destino_backup.exists():
        print(f"O backup já existe em: {destino_backup}")
        return

    shutil.copytree(pasta_destino_si_raiz, destino_backup)
    print(f"Backup realizado em: {destino_backup}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def backup_termos():
    """Realiza backup de todos os termos organizados."""
    backup_termos_ativos()
    backup_termos_si()
