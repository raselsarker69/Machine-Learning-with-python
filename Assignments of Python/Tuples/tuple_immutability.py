tuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)


# When I will Trying to modify an element (this will raise an error)
try:
    tuple1[0] = 100   # 0 index a nai but jodi access kortay cai then show error message
except TypeError as e:
    print('Error:', e)