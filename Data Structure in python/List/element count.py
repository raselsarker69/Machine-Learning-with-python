list1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

count = 0

for i in range(1, len(list1)):
    list1[i] = list1[i] // 10
    count += list1[i]
    
print(count)
