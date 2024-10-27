list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]

#filtering the even number.
filter_even = [i for i in list1 if i % 2 == 0]
print(filter_even)


#filtering the odd number.
odd_number = [i for i in list1 if i % 2 != 0]
print(odd_number)


#filtering the square numbers.
squaring_num = [x ** 2 for x in list1]
print(squaring_num)