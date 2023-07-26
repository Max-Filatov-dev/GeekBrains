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

    def del_contact(self, del_data: list):
        """ """
        [self.phone_book["contacts"].pop(key) for key in del_data]

    def save_file(self):
        """ """
        with open(self.path_pb, "w", encoding="utf-8") as pb:
            json.dump(self.phone_book, pb, indent=4, ensure_ascii=False)
