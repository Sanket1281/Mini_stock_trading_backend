# Stock Trading Backend System

A lightweight, high-performance stock trading backend built with **FastAPI**. This project simulates a trading environment where users can place orders, execute trades, and manage a portfolio using an in-memory data store.

It includes a custom **Python SDK** to interact with the API programmatically.

## 🚀 Features

* **Order Management**: Place `MARKET` or `LIMIT` orders for Equity instruments.
* **Trade Execution**: Simulates trade execution and updates order status.
* **Portfolio Management**: real-time updates of holdings, average price, and current valuation.
* **Instrument Data**: Fetch live (mock) market data for symbols like TCS, INFY, and RELIANCE.
* **Input Validation**: robust validation for order quantities and pricing using Pydantic.
* **Client SDK**: A dedicated Python class (`TradingSDK`) for easy API integration.

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Framework**: FastAPI
* **Server**: Uvicorn
* **Client Library**: Requests (for SDK)

---

## 📂 Project Structure

```text
.
├── main.py        # The FastAPI backend application and business logic
├── sdk.py         # Python SDK wrapper for the API
├── test_sdk.py    # specific script to demonstrate SDK usage
└── README.md      # Project documentation
