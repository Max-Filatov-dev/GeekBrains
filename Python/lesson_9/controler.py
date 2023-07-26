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
                view.print_msg(smp_msg=text.open_book)
            case 2:
                view.show_contact(show_data=pb.phone_book)
            case 3:
                view.search_contact(ser_data=pb.phone_book)
            case 4:
                resp_new_data = view.data_new_contact(new_data=pb.phone_book)
                if resp_new_data:
                    pb.add_contact(add_data=resp_new_data)
                    view.print_msg(smp_msg=text.new_contact, dop_msg=resp_new_data)
                else:
                    view.print_msg(smp_msg=text.false_contact)
            case 5:
                resp_search = view.search_contact(ser_data=pb.phone_book)
                if resp_search:
                    change_index = [i for i in resp_search.keys()][0]
                    resp_new_change = view.data_new_contact(new_data=pb.phone_book)
                    if resp_new_change:
                        resp_check = pb.check_data(
                            old_data=resp_search[change_index],
                            new_data=resp_new_change,
                        )
                        pb.add_contact(
                            add_data=resp_check, index=change_index
                        ) if resp_check else None
                        view.print_msg(smp_msg=text.change_contact)
            case 6:
                resp_del_search = view.search_contact(ser_data=pb.phone_book)
                if resp_del_search:
                    resp_del_app = view.approval(app_msg=text.main_menu[6])
                    if resp_del_app == 'y':
                        change_index = [i for i in resp_del_search.keys()]
                        pb.del_contact(del_data=change_index)
                        view.print_msg(smp_msg=text.del_contact)
            case 7:
                resp_save = view.approval(app_msg=text.main_menu[7])
                pb.save_file() if resp_save else None
            case 8:
                view.print_msg(smp_msg=text.exit_msg)
                break
