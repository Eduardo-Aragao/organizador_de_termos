# Organizador de Termos de Responsabilidade (Beta)

Este projeto consiste em um sistema de **Robotic Process Automation (RPA)** desenvolvido para otimizar a gestão de documentos digitais do setor de TI. O foco é automatizar a triagem, renomeação e backup de termos de responsabilidade de equipamentos, eliminando o erro humano e o tempo gasto em tarefas repetitivas.

## 🚀 Funcionalidades Atuais (Versão Beta)
- **Leitura Inteligente:** Varredura automática de arquivos `.pdf` recursivamente dentro do diretório de entrada.
- **Fragmentação de Nomenclatura:** Sistema baseado em regras para quebrar o nome do arquivo e identificar o colaborador, a categoria do ativo e o setor responsável.
- **Triagem por Regras de Negócio:** Filtra e move os arquivos para diretórios específicos com base em uma lista pré-definida de setores válidos e categorias de hardware/segurança da informação (SI).
- **Tratamento de Exceções:** Arquivos com nomes fora do padrão ou que pertençam a setores/categorias inválidos são movidos automaticamente para uma pasta de contingência (`INVALIDOS`).

## 🛠️ Tecnologias Utilizadas
- **Python:** Linguagem base para o desenvolvimento da automação.
- **Pathlib:** Utilizada como biblioteca principal para manipulação de caminhos do sistema de arquivos de forma moderna e multiplataforma (gerenciamento de diretórios, verificação de existência e fluxos de entrada/saída).
- **Shutil:** Responsável pela movimentação física e segura dos arquivos entre os diretórios.
- **Python-dotenv:** Gerenciamento das configurações e caminhos de pastas de forma isolada por meio de variáveis de ambiente.

## ⚙️ Arquitetura e Regras de Validação

O script processa os documentos aplicando filtros rígidos antes de destinar o arquivo para a sua pasta final:

* **Setores Homologados:** O sistema valida o documento contra uma lista estrita de departamentos (ex: `ti`, `rh`, `produção`, `comercial`, etc.).
* **Divisão por Categorias:**
    * **Destino Equipamentos:** Teclado, mouse, adaptador, monitor, suporte, headset, pendrive, headfone e kit.
    * **Destino Notebooks:** Categoria exclusiva para notebooks.
    * **Destino SI (Segurança da Informação):** Mídias removíveis, vpn e smartphone.

## 🔮 Roadmap & Visão de Futuro (Qualidade & AI Integration)
O projeto está em constante evolução, com as seguintes implementações planejadas para garantir escalabilidade, inteligência e robustez:

- **Desenvolvimento e Automação de Testes:**
    * Implantação de **Testes Unitários (pytest)** para validar as funções de fragmentação de nome (`parse_nome`) e as regras de movimentação de arquivos isoladamente.
    * Criação de cenários de **Testes de Integração** simulando o fluxo completo do RPA (desde a varredura da pasta de entrada até o destino final ou pasta de inválidos) utilizando mocks de sistema de arquivos.
    * Garantia de cobertura de código para prevenir regressões em futuras atualizações das regras de negócio.
- **Refatoração do Módulo de Backup:** Otimização da lógica de integridade dos arquivos originais antes do processamento.
- **OCR & NLP:** Uso de IA para leitura inteligente do conteúdo textual interno dos PDFs, permitindo validações mais profundas além do nome do arquivo.
- **Data Analytics:** Implementação de **NumPy** e **Pandas** para gerar relatórios e gráficos de movimentação de ativos, além de análises preditivas de hardware.
---

### 💡 Impacto no Setor
A implementação deste script visa reduzir em até 80% o tempo dedicado à organização documental, permitindo que a equipe de TI foque em chamados técnicos e melhorias de infraestrutura.
