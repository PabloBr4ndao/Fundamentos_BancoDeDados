# 🚗 UniCarona — Plataforma de Caronas Solidárias Universitárias

O **UniCarona** é uma plataforma desenvolvida como projeto final para a disciplina de **QXD0011 - Fundamentos de Banco de Dados** na **Universidade Federal do Ceará (UFC) — Campus Quixadá**, sob a orientação do **Prof. Francisco Victor da Silva Pinheiro**.

A aplicação visa resolver um problema real enfrentado diariamente pela comunidade acadêmica: a escassez, a inflexibilidade e o custo do transporte público até o campus universitário. O UniCarona conecta estudantes e servidores que possuem veículo próprio (motoristas) a outros membros da instituição que necessitam de deslocamento (passageiros), promovendo a divisão de despesas, otimização da mobilidade urbana e integração social com total segurança.

---

## 📂 Estrutura do Repositório

Com base na organização oficial do projeto, os arquivos estão distribuídos da seguinte forma dentro do repositório:

```text
📁 Projeto_Unicarona/
│
├── 📁 codigo_app/                      # Código-fonte da aplicação em Python (FastAPI)
│   ├── 📄 database.py                  # Configuração e inicialização da sessão com o SQLAlchemy
│   ├── 📄 models.py                    # Mapeamento objeto-relacional (ORM) das tabelas do PostgreSQL
│   ├── 📄 schemas.py                   # Esquemas de validação de dados via Pydantic (JSON)
│   ├── 📄 crud.py                      # Camada de regras de negócio e persistência de dados
│   ├── 📄 main.py                      # Coração da API, definição de rotas (endpoints) e inicialização
│   └── 📄 requirements.txt             # Lista de dependências e bibliotecas do ecossistema Python
│
├── 📁 documents/                       # Documentação, slides e entregas do projeto
│   ├── 📁 diagrams/                    # Arquivos de imagem da modelagem de dados
│   │   ├── 🖼️ UniCarona DER.jpg
│   │   └── 🖼️ UniCarona diagrama relacional.png
│   │  
│   ├── 📄 SLIDE Unicarona (Apresentação).pdf
│   ├── 📄 UniCarona Entrega 1 – Definição da Equipe e Descrição da Aplicação.pdf
│   ├── 📄 UniCarona Entrega 2 – Modelagem Entidade Relacionamento.pdf
│   ├── 📄 UniCarona Entrega 3 – Modelo Relacional e Implementação no SGBD.pdf
│   └── 📄 UniCarona Entrega 4 – Visões, Controle de Acesso e Aplicação Final.pdf
│
├── 📁 printscreen_app/                 # Capturas de tela da aplicação e do banco em funcionamento (CRUD)
│
├── 📄 unicarona.sql                    # Script unificado da Entrega 3 (DDL, DML com +120 registros e Consultas)
├── 📄 unicarona_visoes_and_cons.sql    # Script da Entrega 4 (Criação de Views e comandos de segurança DCL)
└── 📄 README.md

```

## 🛠️ Tecnologias Utilizadas

- **Banco de Dados:** PostgreSQL (SGBD Relacional robusto).
- **Linguagem Backend:** Python 3.10+.
- **Framework Web API:** FastAPI (Alta performance, documentação automática via Swagger).
- **ORM (Mapeamento Relacional):** SQLAlchemy (Tradução declarativa de tabelas para classes Python).
- **Validação de Dados:** Pydantic v2 (Segurança de tipos e parsing de requisições HTTP).
- **Servidor ASGI:** Uvicorn (Servidor de implantação rápido e assíncrono).

---

## 📐 Arquitetura do Sistema e Banco de Dados

### 1. Modelo Conceitual e Relacional
O banco de dados foi projetado seguindo rigorosas regras de normalização:
- **Herança/Especialização:** A tabela `MOTORISTA` estende de `USUARIO`, utilizando o CPF como Chave Primária e Estrangeira simultaneamente, evitando redundância de dados cadastrais.
- **Normalização de Rotas:** Criou-se a tabela `LOCAL` para indexar pontos de embarque/desembarque fixos. A tabela `CARONA` referencia apenas os IDs de origem e destino, impedindo erros de digitação e inconsistências de busca.
- **Entidades Associativas:** Relações complexas como `RESERVA`, `PAGAMENTO` e `AVALIACAO` foram isoladas para suportar atributos específicos do mundo real (ex: status do pagamento, notas e logs temporais).

### 2. Visões Complexas (Views) — Implementadas no Banco
Para aliviar o processamento da aplicação, o banco de dados executa a lógica de agregação nativamente por meio de visões:
- `vw_detalhes_caronas`: Consolida informações operacionais realizando o `JOIN` de 5 tabelas distintas. Entrega à aplicação um relatório pronto com nomes dos motoristas, veículos, placas, origens e destinos literais.
- `vw_ranking_motoristas`: Avalia a reputação do ecossistema utilizando as funções agregadoras `AVG` e `COUNT` agrupadas por `GROUP BY`, ordenando os motoristas por score decrescente.

### 3. Controle de Acesso e Segurança (DCL)
A segurança contra privilégios elevados foi estabelecida diretamente no SGBD com dois perfis de usuários distintos:
1. `unicarona_admin`: Possui privilégios totais de leitura e modificação de estado (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
2. `unicarona_leitura`: Perfil estrito para auditoria e listagens. Possui apenas permissão de `SELECT`, tendo qualquer ação de escrita explicitamente revogada via `REVOKE`.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Antes de iniciar, certifique-se de ter instalado em sua máquina:
- [Python 3.10 ou superior](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/) (e o gerenciador pgAdmin)

### Passo 1: Configuração do Banco de Dados
1. Abra o seu **pgAdmin** (ou ferramenta equivalente) e crie um banco de dados chamado `unicarona`.
2. Abra a Query Tool desse banco de dados e execute sequencialmente os scripts:
   - Primeiro, o conteúdo do arquivo `unicarona.sql` (Ele criará as tabelas, inserirá os 120 registros de teste por tabela e validará o esquema).
   - Segundo, o conteúdo do arquivo `unicarona_visoes_and_cons.sql` (Ele criará as Views operacionais e os perfis de usuários DCL).

### Passo 2: Configuração do Ambiente Python
No seu terminal, navegue até a pasta raiz do repositório e acesse o diretório do código:

```bash
cd codigo_app
```

Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
# No Windows:
python -m venv venv
venv\Scripts\activate

# No Linux/Mac:
python3 -m venv venv
source venv/bin/activate
```

Instale todas as dependências exigidas listadas no `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Passo 3: Inicialização da API
Com o ambiente configurado, inicie o servidor de desenvolvimento com o comando:
```bash
uvicorn main:app --reload
```
*Nota: Certifique-se de que as credenciais de conexão com o banco de dados em `database.py` coincidem com a senha local do seu PostgreSQL.*

### Passo 4: Testando no Swagger
Abra o seu navegador e acesse a documentação interativa automatizada:
👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

Por meio desta interface (Swagger UI), você poderá realizar testes práticos de **CRUD** completo (criar, buscar, atualizar e deletar caronas). 

---

## 👥 Integrantes da Equipe

- **Francisca Ariane dos Santos da Silva** (Matrícula: 554930) — francisca.silva@alu.ufc.br
- **Gabriel Braga Martins** (Matrícula: 493659) — gabrielbragamartins@alu.ufc.br
- **Pablo Brandão Passos** (Matrícula: 539730) — pablobrandao@alu.ufc.br
- **Raul Camurça Rabelo de Almeida** (Matrícula: 596042) — raulcamurca@alu.ufc.br

---
<p align="center">UFC Campus Quixadá • 2026</p>
```