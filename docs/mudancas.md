# Mudanças Realizadas no Script main.py

## Resumo das Correções
O script `main.py` foi corrigido para resolver erros de "no such file or directory" relacionados aos caminhos dos departamentos. As principais mudanças incluem:

1. **Correção de sintaxe nos caminhos**: Uso de strings raw (`r""`) para evitar erros de escape Unicode em caminhos com barras invertidas.
2. **Criação recursiva de diretórios**: Adição de `parents=True, exist_ok=True` aos métodos `mkdir` para criar diretórios pais se necessário.
3. **Busca recursiva de arquivos**: Troca de `glob` para `rglob` para buscar arquivos PDF em subpastas (como TI e RH).

## Diff das Mudanças

### Antes (Código Original)
```python
# Configurações de caminhos
pasta_entrada = Path("C:\Users\eduardo.silva\Desktop\Teste de RPA")
pasta_destino_raiz = Path("C:\Users\eduardo.silva\Desktop\Teste de RPA\DEPARTAMENTOS")

def organizar_termos():
    if not pasta_destino_raiz.exists():
        pasta_destino_raiz.mkdir()

    for arquivo in pasta_entrada.glob("*.pdf"):  
        nome_completo = arquivo.stem
        
        try:
    
            partes = nome_completo.split('-')
            
            if len(partes) == 3:
                nome, categoria, setor = partes
                
                caminho_setor = pasta_destino_raiz / setor
                
                if not caminho_setor.exists():
                    caminho_setor.mkdir()
                
                shutil.move(str(arquivo), str(caminho_setor / arquivo.name))
                print(f"Sucesso: {nome} movido para {setor}")
            else:
                print(f"Erro de padrão: {arquivo.name}")
                
        except Exception as e:
            print(f"Erro ao processar {arquivo.name}: {e}")
```

### Depois (Código Modificado)
```python
# Configurações de caminhos
pasta_entrada = Path(r"C:\Users\eduardo.silva\Desktop\Teste de RPA")
pasta_destino_raiz = Path(r"C:\Users\eduardo.silva\Desktop\Teste de RPA\DEPARTAMENTOS")

def organizar_termos():
    if not pasta_destino_raiz.exists():
        pasta_destino_raiz.mkdir(parents=True, exist_ok=True)

    for arquivo in pasta_entrada.rglob("*.pdf"):  
        nome_completo = arquivo.stem
        
        try:
    
            partes = nome_completo.split('-')
            
            if len(partes) == 3:
                nome, categoria, setor = partes
                
                caminho_setor = pasta_destino_raiz / setor
                
                if not caminho_setor.exists():
                    caminho_setor.mkdir(parents=True, exist_ok=True)
                
                shutil.move(str(arquivo), str(caminho_setor / arquivo.name))
                print(f"Sucesso: {nome} movido para {setor}")
            else:
                print(f"Erro de padrão: {arquivo.name}")
                
        except Exception as e:
            print(f"Erro ao processar {arquivo.name}: {e}")
```

## Explicação Detalhada
- **Linhas 4-5**: Adicionado `r` antes das aspas para tornar as strings raw, evitando interpretação de `\U` como sequência de escape Unicode.
- **Linha 9**: `mkdir()` alterado para `mkdir(parents=True, exist_ok=True)` para criar diretórios pais recursivamente e não falhar se já existir.
- **Linha 11**: `glob("*.pdf")` alterado para `rglob("*.pdf")` para buscar arquivos PDF recursivamente em todas as subpastas.
- **Linha 21**: Mesmo ajuste em `mkdir()` para o caminho do setor.

Essas mudanças garantem que o script funcione mesmo se os diretórios pais não existirem e busque arquivos em subpastas como TI e RH.