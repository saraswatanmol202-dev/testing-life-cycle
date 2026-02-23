from fastapi import APIRouter
from orders.order_service import create_order

router = APIRouter()

@router.post("/api/orders")
async def place_order(user_id: int, cart_id: int, items: list):
    # No duplicate check before calling create
    order = await create_order(user_id, cart_id, items)
    return {"order_id": order["id"], "status": "created"}