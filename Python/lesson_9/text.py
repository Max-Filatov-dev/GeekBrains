main_menu = (
    "\nГлавное меню",
    "Открыть файл",
    "Показать контакты",
    "Найти контакт",
    "Добавить контакт",
    "Изменить контакт",
    "Удалить контакт",
    "Сохранить файл",
    "Вернуть файл к шаблону",
    "Выход",
)

fields_new_contact = ("\nВведите ФИО: ", "Введите телефон: ", "Введите коммент: ")
select_text = "\nВведите номер меню: "
main_menu_input_error = f'\n{"-"*30}\nВведите номер от 1 до {len(main_menu)-1}'
open_book = f'\n{"-"*35}\nТелефонная книга успешно открыта!\n{"-"*35}\n'
empty_book = f'\n{"-"*40}\nТелефонная книга пустая или не открыта!\n{"-"*40}\n'
empty_str = f'\n{"-"*55}\n'
menu_search_contact = f'\n{"-"*20}\nВведите данные: '
new_contact = "Новый контакт добавлен!"
not_contact = f"\n{'-'*20}\nКонтакт не найден!"
change_contact = f"\n{'-'*20}\nКонтакт изменен!"
false_contact = "\n!!! Ошибка !!! Новый контакт НЕ добавлен!"
exit_msg = f'\n{"-"*10}\nВыход.\n'
