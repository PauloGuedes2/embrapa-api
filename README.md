## Arquitetura do projeto: Hexagonal / Clean Architecture

```
/embrapa_api
├── /src
│   ├── /domain                  # Domínio puro
│   │   ├── entities.py          # Entidades (Producao, Vinho)
│   │   ├── ports.py             # Interfaces (IScraperPort, IRepository)
│   ├── /application             # Regras de negócio
│   │   ├── use_cases.py         # ObterProducaoUseCase
│   ├── /adapters                # Implementações concretas
│   │   ├── scraper.py           # EmbrapaScraperAdapter
│   │   ├── repository.py        # PostgreSQLRepository
│   ├── /api                     # Camada de entrada (HTTP)
│   │   ├── controllers.py       # FastAPIController
│   │   ├── dependencies.py      # Injeção de dependências
│   ├── config.py                # Configurações (DB, Redis)
├── /tests
├── main.py                      # Ponto de entrada
├── requirements.txt
```