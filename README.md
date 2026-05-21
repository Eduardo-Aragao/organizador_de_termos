# Organizador de Termos de Responsabilidade (Beta)

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/8fd0f92e-7067-4442-88c6-ca3c75bce6a3" />
<p></p>

Este projeto consiste em um sistema de **Robotic Process Automation (RPA)** desenvolvido para otimizar a gestão de documentos digitais do setor de TI. O foco é automatizar a triagem, renomeação e backup de termos de responsabilidade de equipamentos, eliminando o erro humano e o tempo gasto em tarefas repetitivas.

## 🚀 Funcionalidades Atuais (Versão Beta)
- **Backup Automatizado:** Garante a integridade dos arquivos originais antes de qualquer manipulação.
- **Organização por Departamento:** Filtra e move os arquivos para diretórios específicos baseados em regras pré-definidas.
- **Refatoração Modular:** Funções fragmentadas para facilitar a manutenção e escalabilidade do script.

## 🛠️ Tecnologias Utilizadas
- **Python:** Linguagem base para automação.
- **OS & Shutil:** Manipulação de arquivos e diretórios no sistema.
- **Scripts de Automação:** Lógica para padronização de nomenclatura.

## ⚙️ Configuração local
Antes de rodar no seu notebook, crie o ambiente virtual e configure as variáveis de ambiente:

1. Crie e ative o virtualenv na raiz do projeto:
```powershell
python -m venv venv
.\venv\Scripts\activate
```
2. Instale as dependências:
```powershell
python -m pip install -r requirements.txt
```
3. Crie um arquivo `.env` na raiz com os caminhos locais das pastas:
```env
PASTA_ENTRADA=C:\Users\seunome\Desktop\entrada
PASTA_INVALIDOS=C:\Users\seunome\Desktop\invalidos
PASTA_DESTINO_EQUIPAMENTOS=C:\Users\seunome\Desktop\destinos\Destino-Equipamentos
PASTA_DESTINO_NOTEBOOKS=C:\Users\seunome\Desktop\destinos\Destino-Notebooks
PASTA_DESTINO_SI=C:\Users\seunome\Desktop\destinos\Destino-SI
PASTA_BACKUP_EQUIPAMENTOS=C:\Users\seunome\Desktop\backup\Backup-Equipamentos
PASTA_BACKUP_NOTEBOOKS=C:\Users\seunome\Desktop\backup\Backup-Notebooks
PASTA_BACKUP_SI=C:\Users\seunome\Desktop\backup\Backup-SI
```
4. Execute o projeto usando o script:
```powershell
.\executar.bat
```

> O arquivo `.env` não deve ser commitado. Ele está ignorado pelo `.gitignore`.

## 🔮 Roadmap & Visão de Futuro (AI Integration)
O projeto está em constante evolução, com as seguintes implementações planejadas:
- **OCR & NLP:** Uso de IA para leitura inteligente do conteúdo dos PDFs.
- **Renomeação Contextual:** Extração automática de nomes e números de série para padronização total.
- **Data Analytics:** Implementação de **NumPy** e **Pandas** para gerar gráficos de movimentação de ativos e análises preditivas de hardware.

---

### 💡 Impacto no Setor
A implementação deste script visa reduzir em até 80% o tempo dedicado à organização documental, permitindo que a equipe de TI foque em chamados técnicos e melhorias de infraestrutura.



