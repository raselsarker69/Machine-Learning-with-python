# tuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# tuple2 = (200, 300)


# #add_val = tuple1 + (400,)
# #add_val = tuple1 + tuple2
# add_val = tuple1 + (400,) + tuple2
# print("Combined tuple:", add_val)



product_information = [
    ("Desktop", "Electronics", 500),
    ("Laptop", "Electronics", 1000),
    ("Worker", "People", 20)
]

print(f"Product Information: {product_information}")

# Initialize an empty dictionary 
product_dict = {}

# Loop through each product entry
for product_name, product_cat, product_item in product_information:
    # Check if the category does not already exist in product_dict
    if product_cat not in product_dict:
        product_dict[product_cat] = {}  # Create a new category dictionary

    product_dict[product_cat][product_name] = product_item   # Add the product name and item value to the corresponding category

# Print the categorized product dictionary
print("Categorized Product Dictionary:", product_dict)

# Extract unique categories as a set
unique_information = set(product_dict.keys())

print("Unique Product Categories:", unique_information)
