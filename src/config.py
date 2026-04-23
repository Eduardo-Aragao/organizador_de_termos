import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env (se existir)
load_dotenv()

# Caminhos configuráveis via variáveis de ambiente ou padrões relativos
pasta_entrada = Path(os.getenv('PASTA_ENTRADA', r"C:\Caminho\Entrada"))
pasta_destino_ativos_raiz = Path(os.getenv('PASTA_DESTINO_ATIVOS', r"C:\Caminho\DEPARTAMENTOS"))
pasta_destino_si_raiz = Path(os.getenv('PASTA_DESTINO_SI', r"C:\Caminho\SI"))
pasta_backup = Path(os.getenv('PASTA_BACKUP', r"C:\Caminho\Backup_Termos"))

# Subpastas
pasta_invalidos_ativos = pasta_destino_ativos_raiz / "INVALIDOS"
pasta_invalidos_si = pasta_destino_si_raiz / "INVALIDOS"