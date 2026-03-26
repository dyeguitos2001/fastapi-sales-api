from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.sales import router as sales_router

app = FastAPI(
    title="FastAPI Sales API",
    description="API para consulta e análise de dados de vendas",
    version="1.0.0",
)

app.include_router(health_router, tags=["Health"])
app.include_router(sales_router, prefix="/sales", tags=["Sales"])
