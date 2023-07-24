import json

"""
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""

main_dict = {'menu': ('1. Открыть файл', '2. Показать контакты', '3. Найти контакт','4. Добавить контакт',
                      '5. Изменить контакт', '6. Удалить контакт', '7. Сохранить файл', '8. Вернуть файл к шаблону', '9. Выход'),
             'contacts': [(1, 'Филатов Максим', 123, 'Software'), (2, 'Морозов Евгений', 456, 'Engeenies')]}


def check_data() -> str:
    while True:
        menu = [i for i in main_dict['menu']]
        print('\nГлавное меню:', *menu, sep='\n\t')
        option = input('\nВыберите действие: ')
        # Проверка на пустату и отсутствие букв
        if option.isdigit():
            return option
        else:
            print(f'\n{"-"*45}\nВведите Номер (1, 2...)\n{"-"*45}\n')


def open_file():
    """ """
    with open('lesson_8/phone_book.json') as pb:
        data = json.load(pb)
    return data


def new_contact():
    """ """
    name_fio = input('\nВведите ФИО: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name_fio, phone, comment


def change_contact(contacts: list):
    """ """
    change_name = input('\nВведите имя: ').lower()
    select = [k for k in contacts if change_name in k[1].lower()]
    if select:
        print(f'{"-"*30}\n{select[0]}')
        resp = select[0][0], *new_contact()
        contacts[resp[0]-1] = resp
        return contacts
    else:
        print(f'{"-"*30}\nНет таких контактов!')

    
def del_contact(del_cont: list):
    """ """
    del_name = input('\nВведите имя: ').lower()
    del_serch = [k for k in del_cont if del_name in k[1].lower()]
    if del_serch:
        del_cont.pop(del_serch[0][0]-1)
        print(f'Контак удален: {del_serch[0]}')
        return del_cont
    else:
        print(f'{"-"*30}\nНет таких контактов!')


def save_file(save_data: dict):
    """ """
    with open('lesson_8/phone_book.json', 'w', encoding='utf-8') as pb:
        json.dump(save_data, pb, indent=4, ensure_ascii=False)


def main():
    """ """
    tmp_data = None

    while True:
        response = int(check_data())
        match response:
            case 1:
                tmp_data = open_file()
                print(f'\n{"-"*30}\nФайл успешно открыт.\n{"-"*30}\n') if tmp_data else print(f'\n{"-"*30}\nАбшибка открытия!')
            case 2:
                if tmp_data:
                    contacts = [k for k in tmp_data['contacts']]
                    print(f'\nПоказать контакты\n{"-"*30}', *contacts, sep='\n\t')
                else:
                    print(f'\n{"-"*30}\nНеобходимо открыть файл!\n{"-"*30}\n')
            case 3:
                if tmp_data:
                    search_name = input(f'\nНайти контакт\n{"-"*20}\nВведите имя: ').lower()
                    result_search = [k for k in tmp_data['contacts'] if search_name in k[1].lower()]
                    print(f'{"-"*30}\n{result_search}') if result_search else print(f'{"-"*30}\nНет таких контактов!')
                else:
                    print(f'\n{"-"*30}\nНеобходимо открыть файл!\n{"-"*30}\n')
            case 4:
                if tmp_data:
                    resp_new = new_contact()
                    next_number = max([i[0] for i in tmp_data['contacts']])+1
                    tmp_data['contacts'].append([next_number, *resp_new]) if resp_new else None
                    print(f'{"-"*30}\nДобавлен контакт: {next_number} {resp_new}\n')
                else:
                    print(f'\n{"-"*30}\nНеобходимо открыть файл!\n{"-"*30}\n')
            case 5:
                if tmp_data:
                    resp_change = change_contact(contacts=tmp_data['contacts'])
                    tmp_data['contacts'] = resp_change if resp_change else tmp_data['contacts']
                else:
                    print(f'\n{"-"*30}\nНеобходимо открыть файл!\n{"-"*30}\n')
            case 6:
                if tmp_data:
                    resp_del = del_contact(del_cont=tmp_data['contacts'])
                    tmp_data['contacts'] = resp_del if resp_del else tmp_data['contacts']
                else:
                    print(f'\n{"-"*30}\nНеобходимо открыть файл!\n{"-"*30}\n')
            case 7:
                save_file(save_data=tmp_data) if tmp_data else print(f'\n{"-"*30}\nНеобходимо открыть файл!\n{"-"*30}\n')
            case 8:
                sogl = input('Уверены что хотите перезаписать файл? (y/n) ')
                if sogl == 'y':
                    save_file(save_data=main_dict)
                    print(f'\n{"-"*20}\nФайл перезаписан!\n{"-"*20}\n')
                    break
            case 9:
                print(f'\n{"-"*10}\nВыход.\n{"-"*10}\n')
                break
            case _:
                print(f'\n{"-"*25}\nНе корректный выбор действия!\n{"-"*25}\n')


if __name__ == '__main__':
    main()
    # save_file()
