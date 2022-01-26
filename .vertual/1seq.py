user_list = []
number_element = int(input('Введите количество списков: '))
for i in range(number_element):
    n_element = 1
while n_element <= number_element:  
    user_list.append(int(input("Сохранить в " + str(n_element) + " список: ")))
    n_element += 1
user_list.sort()
print(user_list)