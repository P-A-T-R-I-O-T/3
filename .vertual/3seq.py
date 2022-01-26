user_list_1 = input("Введите в списк значения через ',' ';' '/' : ").replace(';', ',').replace('/', ',').split(',')
user_list_2 = input("Введите в списк значения через ',' ';' '/' : ").replace(';', ',').replace('/', ',').split(',')
remove_element = [int(i) for i in user_list_1 if i not in user_list_2]
print(str(remove_element).strip('[]'))