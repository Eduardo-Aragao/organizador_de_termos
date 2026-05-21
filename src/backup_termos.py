import shutil
from pathlib import Path
import datetime
from .config import (
    pasta_backup_equipamentos,
    pasta_backup_notebooks,
    pasta_backup_si,
    pasta_destino_equipamentos,
    pasta_destino_notebooks,
    pasta_destino_si,
)

def backup_termos():
    """Realiza backup de todos os termos organizados."""
    data_hora = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Backup de equipamentos
    backup_equipamentos = pasta_backup_equipamentos / f"backup_equipamentos_{data_hora}"
    shutil.copytree(pasta_destino_equipamentos, backup_equipamentos)
    print(f"Backup de equipamentos criado em: {backup_equipamentos}")

    # Backup de notebooks
    backup_notebooks = pasta_backup_notebooks / f"backup_notebooks_{data_hora}"
    shutil.copytree(pasta_destino_notebooks, backup_notebooks)
    print(f"Backup de notebooks criado em: {backup_notebooks}")

    # Backup de SI
    backup_si = pasta_backup_si / f"backup_si_{data_hora}"
    shutil.copytree(pasta_destino_si, backup_si)
    print(f"Backup de SI criado em: {backup_si}")
