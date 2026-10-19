sales = [
    ("Apple", 5, 2.00),
    ("Banana", 3, 1.50),
    ("Apple", 4, 2.00),
    ("Orange", 6, 3.00),
    ("Banana", 2, 1.50)
]

updated_records = {}
total_rev = 0
for product_name, quantity_sold, unit_price in sales: 
    updated_records[product_name] = updated_records.get(product_name,0) + quantity_sold
    item_sold = updated_records[product_name]
    print(quantity_sold,unit_price)
    total_rev += quantity_sold*unit_price
print(updated_records)
print(total_rev)
highest_sold = 0
best_product = ""
for key, values in updated_records.items():
    if values > highest_sold:
        highest_sold=values
        best_product = key
print(best_product)