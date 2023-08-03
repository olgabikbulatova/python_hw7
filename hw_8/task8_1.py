import os

filename = 'c:/Users/obikb/OneDrive/Рабочий стол/домашка питон/hw_8/tel.txt'

def load_data():
    if os.path.isfile(filename):
        with open(filename, encoding='utf-8') as f1:
            r = f1.readlines()
            book = []
            for line in r:
                book.append(line.split())
        return book
    book = []
    return book

def add_tel(book):
    last_name = input('введите фамилию: ').capitalize() 
    first_name = input('введите имя: ').capitalize() 
    second_name = input('введите отчество: ').capitalize() 
    tel = input('введите телефон: ')
    with open(filename, 'a', encoding='utf-8') as f1:
        f1.write(f'{last_name} {first_name} {second_name} {tel} \n')
    book.append([last_name, first_name, second_name, tel])
    return book


def show_book(book):
    for line in book:
        print((' ').join(line))


def search_phone(book, object):
    for line in book:
        if object in line:
            return (' ').join(line)
    return 'такой записи нет'


def change_phone(book, object):
    for line in book:
        if object in line:
            print((' ').join(line))
            line_new = input('Введите корректные данные(ФИО телефон): ').split()
            book.insert(book.index(line), line_new)
            book.pop(book.index(line))
            return f'Запись изменена {(" ").join(line_new)}'  
    with open(filename, 'w', encoding='utf-8') as f1:
        for line in book:
            f1.write(f"{(' ').join(line)}\n")
    return 'такой записи нет'
     

def delete_phone(book, object):
    for line in book:
        if object in line:
            print((' ').join(line))
            book.pop(book.index(line))
            return 'Запись удалена'
    with open(filename, 'w', encoding='utf-8') as f1:
        for line in book:
            f1.write(f"{(' ').join(line)}\n")        
    return 'такой записи нет'
    

if __name__ == '__main__':
    book = load_data()
    while True:
        act = input('Меню:\n1 -добавить данные \n2 - искать данные \n3 - показать всю книгу\n4 - изменить запись\n5 - удалить запись\n6 - выход\nвыберите пукт меню: ')
        if act == '1':
            book = add_tel(book)  
        elif act == '2':
            object = input('Введите что выхотите найти: ').capitalize()  
            print(search_phone(book, object))   
        elif act == '3':
            book = show_book(book)
        elif act == '4':
            object = input('Введите запись, которую вы хотите изменить: ').capitalize()  
            print(change_phone(book, object))
        elif act == '5':
            object = input('Введите запись, которую вы хотите удалить: ').capitalize()  
            print(delete_phone(book, object))
        elif act == '6':
            break
        else:
            print('выберите пункт меню от 1 до 6')