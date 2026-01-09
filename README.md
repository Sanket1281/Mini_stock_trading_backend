# Bajaj Broking - Trading SDK Assignment

This project is a backend system and SDK implementation for a simplified stock trading platform. It is designed to demonstrate **REST API development**, **System Design**, and **Trading Domain** concepts as per the Campus Hiring Assignment requirements.

## 📋 Project Overview

The system simulates a core trading engine where users can:
1.  **View Instruments**: Fetch real-time market data (mocked).
2.  **Place Orders**: Buy/Sell stocks using `MARKET` or `LIMIT` orders.
3.  **Execute Trades**: Automatic simulation of order filling.
4.  **Manage Portfolio**: View current holdings and valuations.
5.  **Track Orders**: Check the status of specific orders.

It is built using **FastAPI (Python)** for high performance and includes a **custom Python SDK** to interact with the API programmatically.

---

## 🛠️ Technology Stack

* **Language**: Python 3.10+
* **Framework**: FastAPI (chosen for speed and auto-generated documentation)
* **Server**: Uvicorn (ASGI Server)
* **Database**: In-Memory Storage (Python Lists/Dictionaries) for simplified simulation.

---

## ⚙️ Assumptions Made
*(As requested in the Deliverables)*

1.  **Single User Environment**: The system assumes a single active user. Authentication is mocked/implicit as per the requirement guidelines.
2.  **Immediate Execution**: For simplicity, `MARKET` orders and valid `LIMIT` orders are treated as `EXECUTED` immediately upon placement.
3.  **Data Persistence**: The system uses in-memory storage. All data (orders, trades, portfolio) resets when the application server is restarted.
4.  **Short Selling**: The system validates that a user must own the stock before selling (`SELL` orders require sufficient portfolio quantity).
5.  **Currency**: All prices are assumed to be in INR (₹).

---

## 🚀 Setup and Run Instructions

### 1. Prerequisites
Ensure you have Python installed:
```bash
python --version
