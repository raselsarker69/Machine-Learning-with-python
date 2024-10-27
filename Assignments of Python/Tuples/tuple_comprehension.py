tuple1 = (10, 11, 20, 30, 40, 50, 60, 70, 80, 90, 100)

squared_tuple = tuple(x**2 for x in range(10))
double_tuple = tuple(x*2 for x in range(10))
even_tuple = tuple(x % 2 == 0 for x in range(10))
odd_tuple = tuple(x % 2 == 1 for x in range(10))

print("Squared tuple:", squared_tuple)
print("Double tuple:", double_tuple)
print("Even tuple:", even_tuple)  # Print boolean values.
print("Odd tuple:", odd_tuple)
