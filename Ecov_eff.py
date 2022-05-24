import csv

with open("film_94_add.csv", encoding='utf-8') as add_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(add_file, delimiter = ";")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    cnt = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if cnt == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            print(f'{row[8]} {row[9]}')
            #res = float(row[8]) + float(row[9])
            #print(res)
        cnt += 1

    with open("film_94_nonadd.csv", encoding='utf-8') as non_add_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader1 = csv.reader(non_add_file, delimiter = ";")
        #Счетчик для подсчета количества строк и вывода заголовков столбцов
        cnt1 = 0
        # Считывание данных из CSV файла
        for row1 in file_reader1:
            if cnt1 == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row1)}')
            else:
                # Вывод строк
                print(f'{row1[8]} {row1[9]}')
                #res = float(row[8]) + float(row[9])
                #print(res)
            cnt1 += 1

        res = 0
        for row1 in file_reader1:
            res = float(row[8]) + float(row1[8])
            print(res)


   




'''
add = []
non_add = []
cnt = 0
with open ('film_94_add.csv') as inf_add:
    for s in inf_add:
        s = s.strip().replace(';', '') # удаляем служебные символы, удаляем ;
        add.append(s)
        #print(s)
        cnt = cnt + 1

for i in range (1, cnt):
    add[i].split("  ")


with open ('film_94_nonadd.csv') as inf_nonadd:
    for line in inf_nonadd:
        line = line.strip().replace(';', '')
        non_add.append(line)

for i in range (1, cnt):
    non_add[i].split("  ")


res = float(non_add[4][4]) - float(add[4][4])
print(non_add[4])
print(res)

#for i in range (8, 13):
    '''


