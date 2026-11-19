def find_product_by_name(products, name):
    for product in products:
        if product["name"].lower() == name.strip().lower():
            return product
    return None


def low_stock_products(products, threshold=5):
    return [p for p in products if p["stock"] < threshold]



def products_sorted_by_price(products):
    products.sort(key=lambda p: p["price"])
    return products


def category_summary(products):
    summary = {}

    for product in products:
        category = product["category"]

        if category not in summary:
            summary[category] = {"product_count": 0, "total_stock": 0}

        summary[category]["product_count"] += 1 #these two were backwards. was adding stock to product count and incrementing the actual stock count.
        summary[category]["total_stock"] += product["stock"]

    return summary


def revenue_summary(processed_orders):
    total_revenue = 0
    valid_orders = 0

    for order in processed_orders: #only went through one order before, now it parses through all
        if order["valid"]:
            valid_orders += 1
            total_revenue += order["subtotal"]

    return {
        "valid_orders": valid_orders,
        "total_revenue": round(total_revenue, 2),
    }
