import pandas as pd
data_add = pd.read_csv('film_94_add.csv', sep = ';', skipinitialspace = True)
#print(data_add.head()) #вывод первых 5 строк для проверки, верно ли загружен csv в dataframe
#s = data_add[['s1', 's2']].sum(axis=1) #складываем столбцы под названием s1 и s2


#print(data_add.columns.tolist()) # посмотреть названия столбцов
#print(data_add) # вывод всего dataframe


data_nonadd = pd.read_csv('film_94_nonadd.csv', sep = ';', skipinitialspace = True)

for index, row in data_add.iterrows():
    result = data_add - data_nonadd

    
print(result)

print(result[result.eq(0)].stack().reset_index())



    
'''result = data_add[['s4']] - data_nonadd[['s4']] # находим разницу между колонками с энергиями

idx = result[result['s4']!=0].index # находим индекс отличающегося элемента

print(idx)

print(data_nonadd['s4'].iloc[idx]) # выводим неаддитивные значения из базы data1 по найденным индексам

S = ''

S = 'E = 4-' + str(data_nonadd['n2'].iloc[4])+'n2 = ' + str(data_nonadd['s4'].iloc[4])
print(S)'''
