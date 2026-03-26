from fastapi import APIRouter, HTTPException, Query
from app.schemas.sales import SaleRecord, SalesSummary
from app.services.sales_service import get_all_sales, get_sales_by_region, get_sales_summary

router = APIRouter()

@router.get("", response_model=list[SaleRecord])
def list_sales(category: str | None = Query(default=None, description="Filtrar por categoria")):
    return get_all_sales(category=category)

@router.get("/summary", response_model=SalesSummary)
def sales_summary():
    return get_sales_summary()

@router.get("/region/{region}", response_model=list[SaleRecord])
def sales_by_region(region: str):
    results = get_sales_by_region(region)
    if not results:
        raise HTTPException(status_code=404, detail="Region not found")
    return results
