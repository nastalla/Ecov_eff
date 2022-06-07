import pandas as pd
data_add = pd.read_csv('film_94_add.csv', sep = ';', skipinitialspace = True)

data_nonadd = pd.read_csv('film_94_nonadd.csv', sep = ';', skipinitialspace = True)

# Вычитаем базу данных с аддитивными энергиями от базы с неаддитивными энергиями
for index, row in data_add.iterrows():
    result = data_add - data_nonadd

# Функция для поиска индексов неаддитивных значений и вывода самих значений
def differ(result, df):
    E = ''
    S = 's' # заготовка для названия колонок
    for j in range(1, 7):   # перебираем все колонки s[i]
        S = S + str(j)
        idx = result[result[S]!=0].index # находим индексы ненулевых элементов в базе разницы между адд и неадд энергиями


        # ищем окружение для неаддитивных состояний
        for i in idx: # перебираем все строки в базе индексов ненулевых элементов
            E = 'E' + str(j) 
            for k in range(1, 7):
                # условие - если количество соседей не равно 0, то выводим это число соседей:
                if df['n'+str(k)].iloc[i]!=0:
                    E = E + '-' + str(df['n'+str(k)].iloc[i])+ '*n' + str(k)
            E = E + '='+str(df[S].iloc[i]) # добавляем значение неаддитивной энергии для данного окружения
            print(E)
            E = 'E' + str(j) + '-'
        S = 's' # обнуляем название колонки


differ(result, data_nonadd)    # передаем результат вычитания баз энергий и неаддитивную базу в функцию


