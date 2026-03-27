# FastAPI Sales API

API RESTful desenvolvida com FastAPI para exposição de dados de vendas, com foco em consumo analítico, organização de dados e integração com sistemas.

A aplicação implementa uma camada de serviço responsável por disponibilizar métricas de vendas, permitindo consultas, filtros dinâmicos e agregações de forma estruturada.

## 🔍 O que este projeto demonstra

- Desenvolvimento de APIs REST com FastAPI seguindo boas práticas
- Arquitetura em camadas (routes, services, schemas)
- Processamento e manipulação de dados com Pandas
- Implementação de filtros dinâmicos via query parameters
- Serialização e validação de dados com Pydantic
- Estruturação de endpoints para consumo analítico
- Documentação automática com Swagger/OpenAPI
- Testes automatizados com pytest

## 🧠 Regras de negócio implementadas

- Filtro de vendas por região e categoria
- Cálculo de métricas agregadas (ex: receita total)
- Estrutura de resposta padronizada para consumo analítico
- 
## Estrutura

```text
fastapi-sales-api-project/
├── app/
│   ├── routes/
│   │   ├── health.py
│   │   └── sales.py
│   ├── schemas/
│   │   └── sales.py
│   ├── services/
│   │   └── sales_service.py
│   ├── main.py
│   └── __init__.py
├── data/
│   └── sales_summary_gold.csv
├── tests/
│   └── test_api.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Como executar

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Documentação da API

Depois de rodar a aplicação, acesse:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 📡 Endpoints

### Health Check
- `GET /health` → Verifica o status da API

### Vendas
- `GET /sales` → Retorna todos os registros de vendas
- `GET /sales?category={categoria}` → Filtra vendas por categoria
- `GET /sales/region/{region}` → Filtra vendas por região
- `GET /sales/summary` → Retorna métricas agregadas de vendas

## Exemplos de uso

### Buscar todos os registros
```bash
curl http://127.0.0.1:8000/sales
```

### Filtrar por categoria
```bash
curl "http://127.0.0.1:8000/sales?category=Tecnologia"
```

### Resumo geral
```bash
curl http://127.0.0.1:8000/sales/summary
```

### Buscar por região
```bash
curl http://127.0.0.1:8000/sales/region/Sudeste
```

## ⚙️ Tecnologias utilizadas

- FastAPI
- Python
- Pandas
- Pydantic
- Pytest
- Uvicorn
  
## Destaque 

**API de vendas com FastAPI e Python**
- Desenvolvi uma API REST para disponibilização de dados de vendas para consumo analítico.
- Estruturei endpoints para consulta geral, filtros e métricas agregadas.
- Organizei o projeto com rotas, serviços, schemas e testes automatizados.
- Utilizei FastAPI, Pandas e documentação automática via Swagger.

## Autor

Dyego Simões Cabral Metelo
