def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0):

    price=float(base_price)+ sum(float(item) for item in items )

    discounted = price *(1-discount/100)

    tax_value = discounted * tax_rate

    final_bill=round(discounted + tax_value + delivery_fee , 2)
    

    print(f"{final_bill:.2f}")


calculate_cafeteria_bill(100)
calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)