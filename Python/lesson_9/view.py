import text


def show_menu():
    """ """
    return [
        print("\t", f"{num}. {val}") if num else print(text.main_menu[0])
        for num, val in enumerate(text.main_menu)
    ]


def select_option():
    """ """
    while True:
        show_menu()
        select = input(text.select_text)
        if select.isdigit() and 0 < int(select) <= len(text.main_menu) - 1:
            return int(select)
        else:
            print(text.main_menu_input_error)


def show_contact(show_data: dict):
    """ """
    print(text.empty_str)
    return (
        [
            print(f"{k}. {v[0]:<20} {v[1]:<15} {v[2]:<15}")
            for k, v in show_data["contacts"].items()
        ]
        if show_data
        else print(text.empty_book)
    )


def data_new_contact(new_data: dict):
    """ """
    return (
        [input(i) for i in text.fields_new_contact]
        if new_data
        else print(text.empty_book)
    )


def search_contact(ser_data: dict, show=True):
    """ """
    result_search = {"contacts": {}}
    search_name = input(text.menu_search_contact).lower()
    add = (
        [
            result_search["contacts"].update({k: item})
            for k, item in ser_data["contacts"].items()
            for cont in item
            if search_name in str(cont).lower()
        ]
        if ser_data and search_name
        else print(text.empty_book)
    )
    if result_search["contacts"] and show:
        show_contact(show_data=result_search)
        return result_search["contacts"]
    else:
        print(text.not_contact)


def print_msg(msg: str, dop_msg=None):
    """ """
    print(f'{"-"*40}\n{msg}\n{dop_msg}') if dop_msg else print(msg)
