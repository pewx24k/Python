orders = {
    'pizza': 200,
    'burger': 56,
    'pepsi': 25,
    'Coffee': 14}
sorted_dic = sorted(orders.items(), key=lambda x: x[1])
print(sorted_dic)
if sorted_dic=='pepsi' : 25
