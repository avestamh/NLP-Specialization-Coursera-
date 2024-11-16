my_list = ['apple', 'banana', 'cherry', '', 'cherry']
for i, item in enumerate(my_list):
    print(f'index {i}: {item}' )

lll= [i for i, item in enumerate(my_list) if item]
print(lll)