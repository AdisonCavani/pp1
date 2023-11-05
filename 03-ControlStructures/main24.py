curr_product_price = 140
prev_product_price = 200

if (1 - curr_product_price / prev_product_price) >= 0.1:
    print("Buy the product!!")
    print(f"Product price reduced by {(1 - curr_product_price / prev_product_price) * 100}%")