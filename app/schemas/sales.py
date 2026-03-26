from pydantic import BaseModel

class SaleRecord(BaseModel):
    order_day: str
    region: str
    category: str
    total_orders: int
    total_quantity: float
    revenue: float
    completed_orders: int
    avg_ticket: float

class SalesSummary(BaseModel):
    total_revenue: float
    total_orders: int
    total_quantity: float
    total_completed_orders: int
