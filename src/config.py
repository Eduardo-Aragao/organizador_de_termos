import os
from pathlib import Path

# Caminhos configuráveis via variáveis de ambiente ou padrões relativos
pasta_entrada = Path(os.getenv('PASTA_ENTRADA', r"C:\Users\eduardo.silva\Desktop\Teste de RPA"))
pasta_destino_ativos_raiz = Path(os.getenv('PASTA_DESTINO_ATIVOS', r"C:\Users\eduardo.silva\Desktop\DEPARTAMENTOS"))
pasta_destino_si_raiz = Path(os.getenv('PASTA_DESTINO_SI', r"C:\Users\eduardo.silva\Desktop\SI"))
pasta_backup = Path(os.getenv('PASTA_BACKUP', r"C:\Users\eduardo.silva\Desktop\Backup_Termos"))

# Subpastas
pasta_invalidos_ativos = pasta_destino_ativos_raiz / "INVALIDOS"
pasta_invalidos_si = pasta_destino_si_raiz / "INVALIDOS"