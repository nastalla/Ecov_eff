import pandas as pd
data_add = pd.read_csv('film_94_add.csv', sep = ';', skipinitialspace = True)
#print(data_add.head()) #вывод первых 5 строк для проверки, верно ли загружен csv в dataframe

#print(data_add.columns.tolist()) # посмотреть названия столбцов
#print(data_add) # вывод всего dataframe


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

    
