from db import database

async def create_order(user_id: int, cart_id: int, items: list):
    # No idempotency check — this is the bug
    order = await database.orders.insert({
        "user_id": user_id,
        "cart_id": cart_id,
        "items": items,
        "status": "pending"
    })
    return order

async def get_order(order_id: int):
    return await database.orders.find_one({"id": order_id})

async def cancel_order(order_id: int):
    return await database.orders.update(
        {"id": order_id},
        {"status": "cancelled"}
    )