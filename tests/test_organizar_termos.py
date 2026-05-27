from pathlib import Path
import shutil
import pytest
from src.organizar_termos import garantir_pasta

def test_garantir_pasta_cria_diretorio(tmp_path):
    # Configura um caminho de destino dentro do diretório temporário
    destino = tmp_path / "nova_pasta"

    # Chama a função para garantir que o diretório seja criado
    garantir_pasta(destino)

    # Verifica se o diretório foi criado corretamente
    assert destino.exists()
    assert destino.is_dir()