def product_data_transformer():
    """
        Product Data Transformer
    """
    # Step 1: Ask user for product names
    names = input("Enter product names comma-separated: ").split(",")
    names = [name.strip() for name in names]

    # Step 2: Ask user for product prices
    try:
        prices = input("Enter product prices (comma-separated): ").split(",")
        prices = [float(price.strip()) for price in prices]
    except ValueError:
        print(" Prices must be numbers.")
        return

    # Step 3: Pair products with prices using zip
    paired = list(zip(names, prices))

    # Step 4: Filter out invalid prices (<= 0)
    filtered = list(filter(lambda item: item[1] > 0, paired))

    # Step 5: Transform each pair into dictionary with discount
    transformed = list(map(lambda item: {
        "product": item[0],
        "price": item[1],
        "discounted": round(item[1] * 0.9, 2)  
    }, filtered))

    # Step 6: Save results as JSON
    with open("./day3/products.json", "w") as f:
        f.write("[\n")
        for i, product in enumerate(transformed):
            line = (
                "  {\n"
                f'    "product": "{product["product"]}",\n'
                f'    "price": {product["price"]},\n'
                f'    "discounted": {product["discounted"]}\n'
                "  }"
            )
            # Add a comma after each object except the last one
            if i < len(transformed) - 1:
                line += ","
            f.write(line + "\n")
        f.write("]")

    # Step 7: Print preview (first 5)
    print(" Preview of first 5 results:")
    for product in transformed[:5]:
        print(product)


