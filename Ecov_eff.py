import pandas as pd
from tkinter import *
from tkinter import filedialog


# Функция для поиска индексов неаддитивных значений и вывода самих значений
def differ():
    n = int(number_sort_text.get(1.0, END)) # число сортов атомов берем из поля ввода
    data_add = pd.read_csv(file_add, sep = ';', skipinitialspace = True) #'film_94_add.csv'
    data_nonadd = pd.read_csv(file_nonadd, sep = ';', skipinitialspace = True) # 'film_94_nonadd.csv'

    # Вычитаем базу данных с аддитивными энергиями от базы с неаддитивными энергиями
    for index, row in data_add.iterrows():
        result = data_add - data_nonadd

    E = '' # строка для записи неаддитивных энергий
    lines = [] # массив строк неаддитивных энергий
    S = 's' # заготовка для названия колонок
    m = 0 # счетчик неаддитинвых энергий
    
    for j in range(1, (n+1)):   # перебираем все колонки s[i]
        S = S + str(j)
        idx = result[result[S]!=0].index # находим индексы ненулевых элементов в базе разницы между адд и неадд энергиями

        # ищем окружение для неаддитивных состояний
        for i in idx: # перебираем все строки в базе индексов ненулевых элементов
            E = 'E' + str(j) 
            for k in range(1, (n+1)):
                # условие - если количество соседей не равно 0, то выводим это число соседей:
                if data_nonadd['n'+str(k)].iloc[i]!=0:
                    E = E + '-' + str(data_nonadd['n'+str(k)].iloc[i])+ '*n' + str(k)
            E = E + '='+str(data_nonadd[S].iloc[i]) # добавляем значение неаддитивной энергии для данного окружения
            lines.append(E)
            m = m + 1
        S = 's' # обнуляем название колонки
        
    # Записываем массив неаддитивных энергий в файл
    f = open('text.txt', 'w')
    if m != 0:
        for line in lines:
            f.write(line + "\n")
        f.close()
    else:
        f.write("Неаддитивные энергии не найдены")
        f.close()


# GUI
window = Tk()
window.title("Поиск неаддитивных энергий")
window.geometry("500x300")

def click_add():
    global file_add
    file_add = filedialog.askopenfilename() # эта переменная будет содержать путь к файлу
    
def click_nonadd():
    global file_nonadd
    file_nonadd = filedialog.askopenfilename()

def click_result():
    differ()
    btn_ready = Button(window, text = "Готово!", font = ("Arial", 12))
    btn_ready.place(x = 150, y = 170)


# Функция считывания названий сортов из окошек
def sort_input():
    S = [] # список названий сортов
    n = int(number_sort_text.get(1.0, END))
    for i in range (0, n):
        S.append(sort_inputs[i].get('1.0', 'end-1c'))
    print(S)
    # Выберите файл с аддитивными энергиями
    label2 = Label(text = "2. Выберите файл с аддитивными энергиями")
    label2.config(font = ("Arial", 12), justify = LEFT)
    label2.place(x = 10, y = 50)

    # Выбор файла с аддитивными энергиями
    btn_add_file = Button(window, text = "Выбрать...", font = ("Arial", 12), height = 1, width = 10, command = click_add)
    btn_add_file.place(x = 360, y = 45)


    # Выберите файл с неаддитивными энергиями
    label3 = Label(text = "3. Выберите файл с неаддитивными энергиями")
    label3.config(font = ("Arial", 12), justify = LEFT)
    label3.place(x = 10, y = 85)

    # Выбор файла с неаддитивными энергиями
    btn_nonadd_file = Button(window, text = "Выбрать...", font = ("Arial", 12), height = 1, width = 10, command = click_nonadd)
    btn_nonadd_file.place(x = 360, y = 85)


    # Записать неаддитивные энергии в файл
    label4 = Label(text = "4. Записать неаддитивные энергии в файл")
    label4.config(font = ("Arial, 12"), justify = LEFT)
    label4.place(x = 10, y = 120)

    btn_result = Button(window, text = "Записать", font = ("Arial", 12), height = 1, width =10, command = click_result)
    btn_result.place(x = 360, y = 120)

    
# Функция для создания окошек для ввода названий сортов
def sort(event):
    global sort_inputs
    sort_inputs = []
    n = int(number_sort_text.get(1.0, END))
    for i in range (1, (n+1)):
        sort1_text = Text(window, width = 10, height = 1)
        sort1_text.place(x = 150, y = 50+i*50)
        sort_inputs.append(sort1_text)
    btn_sort = Button(window, text = "OK", command = sort_input)
    btn_sort.place(x = 150, y = 400)    
        

        
# Введите число сортов
label1 = Label(text = "1. Введите число сортов ")
label1.config(font = ("Arial", 12), justify = LEFT)
label1.place(x = 10, y = 10)

# Поле ввода для числа сортов
number_sort_text = Text(window, width = 5, height = 1)
number_sort_text.place(x = 200, y = 15)

number_sort_text.bind('<Return>', sort)




window.mainloop()










