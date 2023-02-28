from collections import UserDict, UserList


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record(Name, Phone):
    phones = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = []
        if phone:
            self.phones.append(phone)

    def name_name(self):
        self.value = Name

    def phone_phone(self):
        self.value = Phone

    def add_phone(self, phone):
        if not phone in self.phones:
            self.phones.append(phone)

    def chenge_phone(self, phone, ph):
        if phone in self.phones:
            ind = self.phones.index(phone)
            self.phones[ind] = ph

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return self.data


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    print(ab['Bill'].phones[0])

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')