from sdk import TradingSDK

sdk = TradingSDK()

print("INSTRUMENTS:")
print(sdk.get_instruments())

print("\nPLACING ORDER:")
order = sdk.place_order("TCS", "BUY", "MARKET", 10)
print(order)

print("\nORDER STATUS:")
print(sdk.get_order(order["orderId"]))

print("\nTRADES:")
print(sdk.get_trades())

print("\nPORTFOLIO:")
print(sdk.get_portfolio())
