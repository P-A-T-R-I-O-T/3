user_list = []
number_user_list = input("Введите в списк значения через ',' ';' '/' : ").replace(';', ',').replace('/', ',').split(',')
sorted_directions = sorted(number_user_list)
ready_list = [int(i) for i in sorted_directions]
for i in ready_list:
    if ready_list.count(i) == 1:
        user_list.append(i)

print(str(user_list).strip('[]'))