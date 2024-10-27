list1 = [10, 11, 12, 13, 14, 15,100, 200, 300]
min_value = list1[0]

for val in list1:
    if val < min_value:
        min_value = val

print(min_value)