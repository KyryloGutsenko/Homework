# Ex. 1
new_list = [23, 12, 45, 12]
new_list.extend([10, 20])
new_list.remove(10)
sum_of_num = 0
new_double_list = []

for i in new_list:
    sum_of_num += i

for i in new_list:
    new_double_list.append(i ** 2)

print(f'List after manipulate: {new_list}')
print(f'Sum of numbers in the list: {sum_of_num}')
print(f'That is new list with every double\n values of old list: {new_double_list}')