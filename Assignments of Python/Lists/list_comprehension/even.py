list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = [i for i in list1 if i % 2 == 0]
print("Even numbers:", even_numbers)


# alternative solution.
for i in list1: 
    if i % 2 == 0:
        print(f"Even number:", i)




