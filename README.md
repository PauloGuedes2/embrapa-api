<h1 align="center">🍇 Embrapa Data API</h1>
<p align="center">
  Uma API REST moderna e estruturada em <strong>Python 3.11 + FastAPI</strong> para expor dados públicos da vitivinicultura brasileira, com arquitetura limpa, testes automatizados e scraping de dados diretamente do site da <a href="http://vitibrasil.cnpuv.embrapa.br/">Embrapa</a>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11-blue.svg" alt="Python 3.11">
  <img src="https://img.shields.io/badge/framework-FastAPI-009688?logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/tests-Pytest-informational" alt="pytest">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" alt="MIT License">
</p>

---

## 📌 Índice

- [📝 Sobre o Projeto](#-sobre-o-projeto)
- [🧱 Arquitetura](#-arquitetura)
- [🔗 Rotas da API](#-rotas-da-api)
- [🚀 Como Usar](#-como-usar)
- [✅ Execução dos Testes](#-execução-dos-testes)
- [⚙️ Integração Contínua (CI) com GitHub Actions](#️-integração-contínua-ci-com-github-actions)
- [🛠 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [📜 Licença](#-licença)

---

## 📝 Sobre o Projeto

Este projeto expõe uma **API RESTful** para facilitar o acesso aos dados de vitivinicultura pública brasileira do site da [Embrapa Vitibrasil](http://vitibrasil.cnpuv.embrapa.br/).  
Esses dados, originalmente disponíveis em páginas HTML com tabelas, são **extraídos via web scraping** e organizados para fácil consumo por sistemas e usuários técnicos.

Os dados disponíveis envolvem informações sobre:

- Produção
- Processamento
- Importação
- Exportação
- Comercialização

---

## 🧱 Arquitetura

A aplicação é baseada nos princípios da **Clean Architecture**, dividindo responsabilidades entre:


### 🗂️ Descrição Geral das Pastas

| 📁 Pasta                          | ✨ Descrição                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| `.github/`                        | Contém configurações de CI com GitHub Actions                               |
| `src/app/`                        | Contém o `main.py`, responsável por inicializar o servidor FastAPI          |
| `src/app/adapters/scraper`        | Responsável pela extração e scraping dos dados da Embrapa                   |
| `src/app/api/controllers/`        | Define as rotas públicas que a API disponibiliza                            |
| `src/app/application/usecase/`    | Lógica de negócio que consome os dados extraídos e prepara a resposta final |
| `src/app/application/validators/` | Validações de entrada, como ano e parâmetros de navegação                   |
| `src/app/config/params`           | Configurações e constantes                                                  |
| `src/app/domain/entities`         | Contém as entidades                                                         |
| `src/app/domain/enums`            | Contém os enums                                                             |
| `src/app/domain/ports`            | Contém as interfaces                                                        |
| `src/app/exceptions/`             | Exceções customizadas para padronizar erros retornados pela API             |
| `src/app/util/utils`              | Utilitários e formatadores utilizados em múltiplas partes do sistema        |
| `src/tests/`                      | Testes unitários organizados por camada (com uso de mocks)                  |
| `requirements.txt`                | Lista de dependências da aplicação para instalação                          |
| `pytest.ini`                      | Configurações globais para rodar o Pytest                                   |
---




## 🔗 Rotas da API

| Método | Endpoint                 | Descrição                                   |
|--------|--------------------------|---------------------------------------------|
| `GET`  | `/producao/{year}`       | Retorna dados de produção para o ano        |
| `GET`  | `/processamento/{year}`  | Retorna dados de processamento para o ano   |
| `GET`  | `/importacao/{year}`     | Retorna dados de importação para o ano      |
| `GET`  | `/exportacao/{year}`     | Retorna dados de exportação para o ano      |
| `GET`  | `/comercializacao/{year}` | Retorna dados de comercialização para o ano |

📘 Acesse a documentação interativa em:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🚀 Como Usar

### 1. Clonar o repositório

```bash
  git clone https://github.com/PauloGuedes2/embrapa-api.git
  cd embrapa-api
```

### 2. Criar ambiente virtual

```bash
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Instalar dependências

```bash
  pip install -r requirements.txt
```

### 4. Rodar localmente
```bash
  uvicorn src.app.main:app --reload
```
### OU
```bash
  python -m src.app.main
```

---
## ✅ Execução dos Testes

### A aplicação possui testes unitários utilizando pytest.
```bash
  pytest
```

### Para rodar os testes com cobertura, utilize:
```bash
  pytest --cov=src/
```
---

## ⚙️ Integração Contínua (CI) com GitHub Actions

Este projeto já está integrado com uma pipeline de CI utilizando GitHub Actions, que executa as seguintes validações automaticamente a cada push ou pull request na branch main:

### Validações Realizadas:

| Ferramenta | Finalidade                                       |
|--------|--------------------------------------------------|
| `Ruff`  | `Análise estática e linting de código Python`    |
| `Bandit`  | `Verificação de falhas de segurança no código`   |
| `Safety`  | `Validação de vulnerabilidades nas dependências` |
| `Coverage`  | `Verificação de cobertura de testes com pytest`  |

### Arquivo da pipeline:

```yaml
.github/workflows/python_ci.yml
```
---
## 🛠 Tecnologias Utilizadas
- **Python 3.11**
- **FastAPI**
- **BeautifulSoup4**
- **Uvicorn**
- **Pytest**
- **GitHub Actions**
- **Ruff**
- **Bandit**
- **Safety**

---
## 📜 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
