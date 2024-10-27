list1 = [10, 11, 12, 13, 14, 15,100, 200, 300]
max_value = list1[0]

for val in list1:
    if val > max_value:
        max_value = val

print(max_value)