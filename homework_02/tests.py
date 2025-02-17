import pytest
from model import PhoneBook
from contact import Contact
from controller import Validator


@pytest.fixture
def phonebook():
    file = "test_contacts.json"
    return PhoneBook(file)


def test_load_contacts(phonebook, tmpdir):
    """Add test data to contact and test it"""
    test_data = [
        {
            "ID": 1,
            "Surname": "Иванов",
            "Name": "Иван",
            "Phone": "1234567890",
            "Birthday": "01.01.1990",
            "Address": "Москва",
            "Comment": "Друг",
        }
    ]

    for data in test_data:
        phonebook.add_contact(data)

    # phonebook.save_contacts()

    assert len(phonebook.contacts) == 1
    assert phonebook.contacts[0].id == 1
    assert phonebook.contacts[0].surname == "Иванов"
    assert phonebook.contacts[0].name == "Иван"
    assert phonebook.contacts[0].phone == "1234567890"
    assert phonebook.contacts[0].birthday == "01.01.1990"
    assert phonebook.contacts[0].address == "Москва"
    assert phonebook.contacts[0].comment == "Друг"


def test_add_contact(phonebook):
    """Add new contact and test it"""
    contact_data = {
        "Surname": "Петров",
        "Name": "Петр",
        "Phone": "0987654321",
        "Birthday": "02.02.1992",
        "Address": "Санкт-Петербург",
        "Comment": "Коллега",
    }

    assert phonebook.add_contact(contact_data) is True
    assert len(phonebook.contacts) == 2
    assert phonebook.contacts[1].surname == "Петров"


def test_find_contacts(phonebook):
    """Contact search test"""
    phonebook.contacts = [
        Contact(1, "Иванов", "Иван", "1234567890", "01.01.1990", "Москва", "Друг")
    ]
    found = phonebook.find_contacts("Иванов")
    assert len(found) == 1
    assert found[0].surname == "Иванов"


def test_delete_contact(phonebook):
    """Contact delete test"""
    phonebook.contacts = [
        Contact(1, "Иванов", "Иван", "1234567890", "01.01.1990", "Москва", "Друг")
    ]
    assert phonebook.delete_contact(1) == True
    assert len(phonebook.contacts) == 0


def test_update_contact(phonebook):
    """Contact update test"""
    phonebook.contacts = [
        Contact(1, "Иванов", "Иван", "1234567890", "01.01.1990", "Москва", "Друг")
    ]
    new_data = {"Surname": "Сидоров", "Name": "Сидор"}
    assert phonebook.update_contact(1, new_data) is True
    assert phonebook.contacts[0].surname == "Сидоров"
    assert phonebook.contacts[0].name == "Сидор"


def test_validate_birthday():
    assert Validator.validate_birthday("01.01.1990") == (True, "01.01.1990")
    assert Validator.validate_birthday("32.01.1990")[0] == False
    assert Validator.validate_birthday("01.13.1990")[0] == False
    assert Validator.validate_birthday("01.01.3000")[0] == False


def test_validate_phone_number():
    assert Validator.validate_phone_number("12345") == True
    assert Validator.validate_phone_number("12345678901") == True
    assert Validator.validate_phone_number("+12345678901") == True
    assert Validator.validate_phone_number("1234") == False
    assert Validator.validate_phone_number("123456789012") == False
