tuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Convert tuple to list
tuple_list = list(tuple1)
tuple_list.pop(2)  # This will remove the element 30
tuple1 = tuple(tuple_list)


print("Tuple after removal:", tuple1)
