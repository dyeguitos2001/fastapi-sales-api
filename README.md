# FastAPI Sales API

API REST desenvolvida com FastAPI para disponibilizar dados de vendas de forma simples, organizada e pronta para consumo analítico.

Este projeto simula uma pequena camada de serviço sobre dados de vendas, expondo endpoints para consulta geral, filtro por região, resumo de receita e health check.

## O que este projeto demonstra

- construção de API com FastAPI
- organização modular em rotas, schemas e serviços
- leitura de dados com Pandas
- serialização de respostas
- filtros por parâmetros de consulta
- documentação automática com Swagger
- testes automatizados com pytest

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

## Endpoints

### Health check
- `GET /health`

### Vendas
- `GET /sales`
- `GET /sales/summary`
- `GET /sales/region/{region}`

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

## Destaque para currículo

**API de vendas com FastAPI e Python**
- Desenvolvi uma API REST para disponibilização de dados de vendas para consumo analítico.
- Estruturei endpoints para consulta geral, filtros e métricas agregadas.
- Organizei o projeto com rotas, serviços, schemas e testes automatizados.
- Utilizei FastAPI, Pandas e documentação automática via Swagger.

## Autor

Dyego Simões Cabral Metelo
