
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def data_entry_cleanup(customers_id):
    id_data = set(customers_id)
    print(id_data.difference())

data_entry_cleanup(customer_ids)