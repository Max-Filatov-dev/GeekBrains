import json

"""
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""

main_dict = {'menu': ('1. Открыть файл', '2. Показать контакты', '3. Добавить контакт',
                      '4. Найти контакт', '5. Изменить контакт', '6. Удалить контакт', '7. Сохранить файл', '8. Выход'),
             'contacts': {1: ('Филатов Максим', 123, 'Software'), 2: ('Морозов Евгений', 456, 'Engeenies')}}

def check_data() -> str:
    while True:
        menu = [i for i in main_dict['menu']]
        print('\nГлавное меню:', *menu, sep='\n\t')
        option = input('\nВыберите действие: ')
        # Проверка на пустату и отсутствие букв
        if option.isdigit():
            return option
        else:
            print(f'\n{"-"*45}\nНеобходимо ввести номер действия (1, 2...)\n{"-"*45}\n')


def open_file():
    """ """
    with open('lesson_8/phone_book.json') as pb:
        data = json.load(pb)
    return data


def save_file():
    """ """
    with open('lesson_8/phone_book.json', 'w', encoding='utf-8') as pb:
        json.dump(main_dict, pb, indent=4, ensure_ascii=False)


def new_contact(person: list):
    """ """
    print(person)
    # main_dict['contacts'].update({
    #     3: person
    # }
    # )


def main():
    """ """
    tmp_data = None

    while True:
        response = int(check_data())
        match response:
            case 1:
                tmp_data = open_file()
                print(f'\n{"-"*30}\nФайл успешно открыт.\n{"-"*30}\n') if tmp_data else print(f'\n{"-"*30}\nError open!')
            case 2:
                if tmp_data:
                    contacts = [k for k in tmp_data['contacts'].values()]
                    print(f'\n{"-"*30}\nКонтакты:', *contacts, sep='\n\t')
                else:
                    print(f'\n{"-"*30}\nНеобходимо открыть файл!\n{"-"*30}\n')
            case 3:
                new_pers = []
                name_fio = input('\nВведите ФИО: ')
                phone = input('Введите телефон: ')
                comment = input('Введите комментарий: ')
                new_pers.extend((name_fio, phone, comment)) if name_fio and phone and comment else None
                new_contact(person=new_pers) if new_pers else print(f'\n{"-"*30}\nВведены не все данные!\n{"-"*30}\n')
            case 8:
                print(f'\n{"-"*10}\nВыход.\n{"-"*10}\n')
                break

    # save_file()


if __name__ == '__main__':
    main()
