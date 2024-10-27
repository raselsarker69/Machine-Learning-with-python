list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

sum = 0 

for i in range(0, len(list1)):
    sum = sum + list1[i]
    avg = 0
    avg = sum / len(list1)
    
print("Sum of all elements:", sum)
print("Avarage of all elements:", avg)