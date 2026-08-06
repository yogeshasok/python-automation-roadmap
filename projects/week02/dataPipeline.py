# Raw dataset: A mix of user purchases, cancellations, and system errors
from functools import reduce


raw_ecom_data = [
    {"order_id": 101, "customer": "Alice", "amount": 150.00, "currency": "USD", "status": "completed", "tags": "electronics,sale"},
    {"order_id": 102, "customer": "Bob", "amount": 0.00, "currency": "USD", "status": "failed", "tags": "book"},
    {"order_id": 103, "customer": "Charlie", "amount": 85.50, "currency": "EUR", "status": "completed", "tags": "clothing"},
    {"order_id": 104, "customer": "David", "amount": 420.00, "currency": "USD", "status": "completed", "tags": "electronics,premium"},
    {"order_id": 105, "customer": "Eva", "amount": 12.99, "currency": "USD", "status": "cancelled", "tags": "home"},
    {"order_id": 106, "customer": "Frank", "amount": 3000.00, "currency": "JPY", "status": "completed", "tags": "books,gift"},
    {"order_id": 107, "customer": "Grace", "amount": None, "currency": "USD", "status": "failed", "tags": ""},
    {"order_id": 108, "customer": "Hank", "amount": 45.00, "currency": "EUR", "status": "completed", "tags": "clothing,sale"},
    {"order_id": 109, "customer": "Ivy", "amount": 95.00, "currency": "USD", "status": "completed", "tags": "home"},
    {"order_id": 110, "customer": "Jack", "amount": 110.50, "currency": "USD", "status": "completed", "tags": "electronics"}
]



def normalize_transaction(transaction):
    if transaction['currency'] == 'USD':
        return transaction['amount']
    elif transaction['currency'] == 'EUR':
        return transaction['amount'] * 1.10
    elif transaction['currency'] == 'JPY':
        return transaction['amount'] * 0.007
    else:
        return None

filtered_data = filter(lambda x: x["status"] == "completed" and x['amount'] and 'electronics' in x['tags'], raw_ecom_data)
finalized_data = map(normalize_transaction, filtered_data)
total_revenue = reduce(lambda x, y: x + y, finalized_data)
print(list(finalized_data))
print(total_revenue)



