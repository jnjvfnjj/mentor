number = [1,43,26,44,87,56,44,33,90,787,54,23]
list_num = list(filter(lambda numbers: numbers % 2 ==0, number))
new_list = []
for num in list_num:
    new_list.append(num)
print(new_list)