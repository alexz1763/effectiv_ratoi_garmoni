from tabulate import tabulate

import matplotlib.pyplot as plt


def inter_num():
    while True:
        num = input('Введите число: ')
        if num.isdecimal() and int(num) > 0:
            return \
                int(num)
            break
        else:
            print('Вы должны ввести целое число, больше нуля, пропробуте снова')

print ('введите минимальное количество узлов')
N_min = inter_num()
print ('введите максимальное количество узлов')
N_mах = inter_num()
S_gar_1 = {i: (1.9602*i)/(8.91+0.11*(i**2)) for i in range(N_min, N_mах+1)}
S_gar_1_1 = {i: (2.15622*i)/(10.7811+0.11*(i**2)) for i in range(N_min, N_mах+1)}
S_gar_1_2 = {i: (2.35224*i)/(12.8304+0.11*(i**2)) for i in range(N_min, N_mах+1)}
columns = ['количество узлов', 'среднегармонический ОКЭ']
print('Kкр=1', tabulate(list(S_gar_1.items()), headers=columns, tablefmt="grid"), sep='\n')
print('Kкр=1_1', tabulate(list(S_gar_1_1.items()), headers=columns, tablefmt="grid"), sep='\n')
print('Kкр=1_2', tabulate(list(S_gar_1_2.items()), headers=columns, tablefmt="grid"), sep='\n')
plt.plot(S_gar_1.keys(), S_gar_1.values(), label='Kкр=1')
plt.plot(S_gar_1_1.keys(), S_gar_1_1.values(), label='Kкр=1_1')
plt.plot(S_gar_1_2.keys(), S_gar_1_2.values(), label='Kкр=1_2')
plt.title('Среднегармонический ОКЭ')
plt.ylabel('Среднегармонический ОКЭ')
plt.xlabel('количество узлов')
plt.legend()
plt.grid(True)
plt.show()