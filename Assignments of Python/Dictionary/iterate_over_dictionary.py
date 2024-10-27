dict1 = {
    'name': 'Rasel sarker',
    'age': '24',
    'country': 'Bangladesh',
    'profession': 'Student',
    'city': 'Rangpur'
}


if dict1.get('name') == 'Rasel sarker':
    print("The name is:", dict1['name'])
    
    
# alternative solution
for key, value in dict1.items():
    print(f'Key: {key}, Value: {value}')