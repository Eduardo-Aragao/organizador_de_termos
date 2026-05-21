import os
from pathlib import Path
from dotenv import load_dotenv

"""
Configuração do projeto.

As variáveis podem vir de um arquivo `.env` (carregado aqui) ou do
ambiente do sistema. NÃO comite seu arquivo `.env` — mantenha segredos
e caminhos locais fora do repositório. Use `.env.example` como modelo.
"""

# Carrega variáveis do arquivo .env (se existir)
load_dotenv()

# Diretório base do projeto (um nível acima de src/)
BASE_DIR = Path(__file__).resolve().parents[1]

# Caminhos configuráveis via variáveis de ambiente ou padrões relativos ao projeto
# Use strings como caminhos nas variáveis de ambiente; aqui garantimos que viram Path.
pasta_entrada = Path(os.getenv('PASTA_ENTRADA', str(BASE_DIR / 'entrada')))
pasta_invalidos = Path(os.getenv('PASTA_INVALIDOS', str(BASE_DIR / 'invalidos')))


pasta_destino_equipamentos = Path(os.getenv('PASTA_DESTINO_EQUIPAMENTOS', str(BASE_DIR / 'destinos' / 'Destino-Equipamentos')))
pasta_destino_notebooks = Path(os.getenv('PASTA_DESTINO_NOTEBOOKS', str(BASE_DIR / 'destinos' / 'Destino-Notebooks')))
pasta_destino_si = Path(os.getenv('PASTA_DESTINO_SI', str(BASE_DIR / 'destinos' / 'Destino-SI')))


pasta_backup_equipamentos = Path(os.getenv('PASTA_BACKUP_EQUIPAMENTOS', str(BASE_DIR / 'backup_equipamentos')))
pasta_backup_notebooks = Path(os.getenv('PASTA_BACKUP_NOTEBOOKS', str(BASE_DIR / 'backup_notebooks')))
pasta_backup_si = Path(os.getenv('PASTA_BACKUP_SI', str(BASE_DIR / 'backup_si')))