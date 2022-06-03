import pandas as pd

data_add = pd.read_csv('film_94_add.csv', sep = ';', skipinitialspace = True)
#print(data_add.head()) #вывод первых 5 строк для проверки, верно ли загружен csv в dataframe

#print(data_add.columns.tolist()) # посмотреть названия столбцов
#print(data_add) # вывод всего dataframe
=======
data = pd.read_csv('film_94_add.csv', sep = ';', skipinitialspace = True)
#print(data.head()) #вывод первых 5 строк для проверки, верно ли загружен csv в dataframe
#s = data[['s1', 's2']].sum(axis=1) #складываем столбцы под названием s1 и s2


#print(data.columns.tolist()) # посмотреть названия столбцов
#print(data) # вывод всего dataframe


data1 = pd.read_csv('film_94_nonadd.csv', sep = ';', skipinitialspace = True)

result = data[['s2']] - data1[['s2']]
print(result)

'''if result!=0:
    print(data[['State']])'''




'''import csv
S = []
C = ''
with open("film_94_add.csv", encoding='utf-8') as add_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(add_file, delimiter = ";", skipinitialspace = True)
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    cnt = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if cnt == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Пишем строку в список
            S.append(float(row))
            print(row[1])
        cnt += 1
    print(S)
    print(cnt)
    
S = S.split()
print(S)

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
                C+=str(row1)
            cnt1 += 1




data_nonadd = pd.read_csv('film_94_nonadd.csv', sep = ';', skipinitialspace = True)

# Вычитаем базу данных с аддитивными энергиями от базы с неаддитивными энергиями
for index, row in data_add.iterrows():
    result = data_add - data_nonadd

def differ(result, df, S):
  idx = result[result[S]!=0].index
  print(df[S].iloc(idx))

S = ''
S = 's1'
differ(result, data_nonadd, S)


'''# Находим индекс отличающихся элементов

idx1 = result[result['s1']!=0].index
idx2 = result[result['s2']!=0].index
idx3 = result[result['s3']!=0].index
idx4 = result[result['s4']!=0].index
idx5 = result[result['s5']!=0].index
idx6 = result[result['s6']!=0].index

<<<<<<< HEAD
print(data_nonadd['s1'].iloc[idx1])
print(data_nonadd['s2'].iloc[idx2])
print(data_nonadd['s3'].iloc[idx3])
print(data_nonadd['s4'].iloc[idx4])
print(data_nonadd['s5'].iloc[idx5])
print(data_nonadd['s6'].iloc[idx6])

S = ''

for i in idx1:
    S = 'E = 1-' + str(data_nonadd['n1'].iloc[i])+ '*n1-' + str(data_nonadd['n2'].iloc[i])+ '*n2-'+ str(data_nonadd['n3'].iloc[i]) + '*n3-' + str(data_nonadd['n4'].iloc[i]) + '*n4-'+ str(data_nonadd['n5'].iloc[i]) + '*n5-' + str(data_nonadd['n6'].iloc[i])+'='+str(data_nonadd['s1'].iloc[i])
    print(S)
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



    
