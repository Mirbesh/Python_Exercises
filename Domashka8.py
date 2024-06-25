# Функция действий
def work_with_phonebook():

    choice=show_menu()

    phone_book=read_txt('phon.txt')

    while (choice > 0 and choice < 9):

        if choice==1:
            print_result(phone_book)
        
        elif choice==2:
            last_name=str(input('Введите фамилию абонента: '))
            find_by_lastname(phone_book,last_name)
        
        elif choice==3:
            number=int(input('Введите номер абонента: '))
            find_by_number(phone_book,number)
	    	
        elif choice==4:
            add_user_to_directory('phon.txt')
        
        elif choice == 5:
            filename = str(input("Введите имя нового файла: "))
            export_to_new_file(phone_book, filename)

        elif choice==6:
            filename = str(input("Введите имя нового файла: "))
            write_txt(filename,phone_book)       
        
        elif choice==7:
            # user_data=input('new data ')
            # add_user(phone_book,user_data)
            write_to_new_file('phonebook.txt',phone_book)

        elif choice==8:
            print("Спасибо, что использовали наш справочник!")
            break

        choice=show_menu()

# Функция меню
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в формате csv с заголовками\n"
          "6. Сохранить справочник в формате txt\n"
          "7. Копировать данные из справочника на новый файл\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

# Функция чтения данных из файла справочника
def read_txt(filename): 
    phone_book=[]
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in filter(lambda x: x != '\n', phb):
            phone_book.append(dict(zip(fields, line.strip().split(','))))
     	
    return phone_book

# Функция отображения справочника
def print_result(phb):
     i = 0
     for dict in phb:
        if i < 1:
            print(*dict.keys())
        print(*dict.values())
        i += 1

# Функция поиска пользователя по фамилии
def find_by_lastname(phone_book,last_name):
    j = count = 0
    for i in phone_book:
        ln = str(i['Фамилия'])
        if ((ln.upper()).split()) == ((last_name.upper()).split()):
           print(*i.values())
           count += 1
        j += 1
    if count == 0:
        print("Извините абонент c такой фамилией не найден в справочнике!")
    else:
        print("Количество абонентов с такой фамилией", count)

# Функция поиска пользователя по номеру телефона
def find_by_number(phone_book,number):
    j = count = 0
    number = str(number)
    for i in phone_book:
        tn = str(i['Телефон'])
        if ((tn.upper()).split()) == ((number.upper()).split()):
           print(*i.values())
           count += 1
        j += 1    
    if count == 0:
        print("Извините абонент c таким номером не найден в справочнике!")
    else:
        print("Количество абонентов с этим номером", count)
# Функция добавления пользователя в справочник
def add_user_to_directory(filename):
    add = 'Y'
    count = 0
    while add == 'Y':
        lastname = str(input('Введите фамилию нового абонента: '))
        name = str(input('Введите имя нового абонента: '))
        telephone = int(input(f'Введите телефонный номер нового абонента {lastname} {name}: '))
        description = str(input(f'Введите описание нового абонента {lastname} {name}: '))
        new_user = lastname + ', ' + name + ', ' + str(telephone) + ', ' + description 
        with open(filename,'a',encoding='utf-8') as phout:
           phout.write(f'{new_user[:-1]}\n') 
        print('В справочник добавлен абонент: ',new_user)
        count += 1
        add = str(input('Если хотите добавить введите буву "Y" на латинице: ')).upper()
    print(f'Спасибо! Вы добавили в справочник {count} абонента(ов)')

# Функция экспорта данных на новый csv файл
def export_to_new_file(phone_book, filename):
    i = 0
    result = []
    filename = filename + ".csv"
    with open(filename,'w',encoding='utf-8') as phout:
      
        for dict in phone_book:
            if i == 0:
                result = "Фамилия; Имя; Телефон; Описание"
                phout.writelines(f"{result}\n")
            i += 1
            result = "{Фамилия}; {Имя}; {Телефон}; {Описание}".format(**dict)
            phout.writelines(f"{result}\n")
           
    print("Готово!")

# Функция экспорта данных на новый txt файл
def write_txt(filename , phone_book):
    filename = filename + ".txt"
    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')

# Функция копирования данных на новый файл
def write_to_new_file(filename, phone_book):
    number = int(input(f'Введите номер строки от 1 до {len(phone_book)}: '))
    with open(filename,'a',encoding='utf-8') as phout:
        s=''
        for v in phone_book[number - 1].values():

            s = s + v + ','

        phout.write(f'{s[:-1]}\n')

work_with_phonebook()