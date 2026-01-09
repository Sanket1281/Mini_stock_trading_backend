from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# -------------------- DATA STORAGE --------------------

instruments = [
    {"symbol": "TCS", "exchange": "NSE", "instrumentType": "EQUITY", "lastTradedPrice": 3500},
    {"symbol": "INFY", "exchange": "NSE", "instrumentType": "EQUITY", "lastTradedPrice": 1500},
    {"symbol": "RELIANCE", "exchange": "NSE", "instrumentType": "EQUITY", "lastTradedPrice": 2500},
]

orders = []
trades = []
portfolio = {}

order_counter = 1
trade_counter = 1

# -------------------- MODELS --------------------

class OrderRequest(BaseModel):
    symbol: str
    orderType: str   # BUY / SELL
    orderStyle: str  # MARKET / LIMIT
    quantity: int
    price: float | None = None

# -------------------- APIs --------------------

@app.get("/api/v1/instruments")
def get_instruments():
    return instruments


@app.post("/api/v1/orders")
def place_order(order: OrderRequest):
    global order_counter, trade_counter

    if order.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0")

    if order.orderStyle == "LIMIT" and order.price is None:
        raise HTTPException(status_code=400, detail="Price is required for LIMIT orders")

    order_id = order_counter
    order_counter += 1

    new_order = {
        "orderId": order_id,
        "symbol": order.symbol,
        "orderType": order.orderType,
        "orderStyle": order.orderStyle,
        "quantity": order.quantity,
        "price": order.price,
        "status": "EXECUTED"
    }

    orders.append(new_order)

    # ----- Create Trade -----
    trade = {
        "tradeId": trade_counter,
        "symbol": order.symbol,
        "quantity": order.quantity,
        "price": order.price if order.price else get_price(order.symbol)
    }
    trade_counter += 1
    trades.append(trade)

    # ----- Update Portfolio -----
    if order.orderType == "BUY":
        if order.symbol in portfolio:
            portfolio[order.symbol]["quantity"] += order.quantity
        else:
            portfolio[order.symbol] = {
                "quantity": order.quantity,
                "averagePrice": trade["price"]
            }

    elif order.orderType == "SELL":
        if order.symbol not in portfolio or portfolio[order.symbol]["quantity"] < order.quantity:
            raise HTTPException(status_code=400, detail="Not enough quantity to sell")
        portfolio[order.symbol]["quantity"] -= order.quantity

    return new_order


@app.get("/api/v1/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["orderId"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")


@app.get("/api/v1/trades")
def get_trades():
    return trades


@app.get("/api/v1/portfolio")
def get_portfolio():
    result = []
    for symbol, data in portfolio.items():
        result.append({
            "symbol": symbol,
            "quantity": data["quantity"],
            "averagePrice": data["averagePrice"],
            "currentValue": data["quantity"] * get_price(symbol)
        })
    return result


# -------------------- HELPER --------------------

def get_price(symbol):
    for inst in instruments:
        if inst["symbol"] == symbol:
            return inst["lastTradedPrice"]
    return 0
