import json


class PhoneBook:
    """ """

    def __init__(self) -> None:
        self.path_pb = "pb.json"
        self.phone_book = {}

    def open_file(self):
        """ """
        with open(self.path_pb, encoding="utf-8") as pb:
            data_pb = json.load(pb)
            self.phone_book.update(data_pb)

    def check_data(self, old_data: list, new_data: list):
        """ """
        ind_empty_str = [x for x, v in enumerate(new_data) if not v]
        if ind_empty_str:
            [new_data.insert(i, old_data[i]) for i in ind_empty_str]
            return list(filter(None, new_data))

    def add_contact(self, add_data: list, index=None):
        """ """
        if add_data:
            next_uid = int(max(self.phone_book["contacts"])) + 1 if not index else index
            self.phone_book["contacts"][str(next_uid)] = add_data

    # def change_contact(self, all_contacts: dict, chg_data: dict):
    #     """ """
    #     print(chg_data)

    # def del_contact(all_cont: list):
    #     """ """
    #     del_name = input('Введите имя: ').lower()
    #     del_serch = [k for k in all_cont if del_name in k[1].lower()]
    #     del_msg = input(
    #         f'Удалить контакт: {del_serch[0]}? (y/n) ') if del_serch else None
    #     if del_serch and del_msg == 'y':
    #         all_cont.pop(del_serch[0][0]-1)
    #         print(f'Контак удален: {del_serch[0]}')
    #         return all_cont
    #     elif del_serch and del_msg == 'n':
    #         print(f'{"-"*30}\nУдаление отменено!')
    #     else:
    #         print(f'{"-"*30}\nНет таких контактов!')

    # def save_file(save_data: dict):
    #     """ """
    #     with open(path_pb, 'w', encoding='utf-8') as pb:
    #         json.dump(save_data, pb, indent=4, ensure_ascii=False)
