import view
import model
import text


def start():
    """ """
    pb = model.PhoneBook()
    while True:
        response = view.select_option()
        match response:
            case 1:
                pb.open_file()
                view.print_msg(msg=text.open_book)
            case 2:
                view.show_contact(show_data=pb.phone_book)
            case 3:
                view.search_contact(ser_data=pb.phone_book)
            case 4:
                resp_new_data = view.data_new_contact(new_data=pb.phone_book)
                if resp_new_data:
                    pb.add_contact(add_data=resp_new_data)
                    view.print_msg(msg=text.new_contact, dop_msg=resp_new_data)
                else:
                    view.print_msg(msg=text.false_contact)
            case 5:
                resp_search = view.search_contact(ser_data=pb.phone_book)
                if resp_search:
                    current_index = int([i for i in resp_search.keys()][0])
                    resp_new_change = view.data_new_contact(new_data=pb.phone_book)
                    if resp_new_change:
                        resp_check = pb.check_data(
                            old_data=resp_search[str(current_index)],
                            new_data=resp_new_change,
                        )
                        pb.add_contact(
                            add_data=resp_check, index=current_index
                        ) if resp_check else None
                        view.print_msg(msg=text.change_contact)

            # case 6:
            #     if tmp_data:
            #         print(f'\nУдалить контакт\n{"-"*30}')
            #         resp_del = del_contact(all_cont=tmp_data['contacts'])
            #         tmp_data['contacts'] = resp_del if resp_del else tmp_data['contacts']
            #     else:
            #         print(f'\n{"-"*30}\nНеобходимо открыть файл!\n{"-"*30}\n')
            # case 7:
            #     print(f'\nСохранить данные\n{"-"*30}')
            #     save = input('Уверены что хотите перезаписать файл? (y/n) ')
            #     if tmp_data and save == 'y':
            #         save_file(save_data=tmp_data)
            #         print(f'\n{"-"*20}\nФайл перезаписан!\n{"-"*20}\n')
            #         break
            # case 8:
            #     print(f'\nВозврат файла к шаблону\n{"-"*30}')
            #     replace = input('Уверены что хотите перезаписать файл? (y/n) ')
            #     if replace == 'y':
            #         save_file(save_data=main_dict)
            #         print(f'\n{"-"*20}\nФайл перезаписан!\n{"-"*20}\n')
            #         break
            case 9:
                view.print_msg(msg=text.exit_msg)
                break
            # case _:
            #     print(f'\n{"-"*25}\nНе корректный выбор действия!\n{"-"*25}\n')
