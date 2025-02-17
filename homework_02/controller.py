import re
from datetime import datetime
from model import PhoneBook
from view import PhoneBookView
from colorama import Fore


class Validator:
    @staticmethod
    def validate_birthday(birthday):
        """
        Checks the correctness of the date of birth,
        that the year is not greater than the current one,
        and automatically corrects the format
        """
        match = re.match(r"^(\d{1,2})\.(\d{1,2})\.(\d{4})$", birthday)

        if not match:
            return False, "Ошибка: дата должна быть в формате ДД.ММ.ГГГГ."

        day, month, year = map(int, match.groups())
        birthday = f"{day:02}.{month:02}.{year}"

        if not (1 <= month <= 12):
            return False, "Ошибка: месяц должен быть в диапазоне 1-12."
        if not (1 <= day <= 31):
            return False, "Ошибка: день должен быть в диапазоне 1-31."

        try:
            datetime(year, month, day)
        except ValueError:
            return False, "Ошибка: такой даты не существует."

        current_year = datetime.now().year
        if year > current_year:
            return False, "Ошибка: год рождения не может быть больше текущего года."

        return True, birthday

    @staticmethod
    def validate_phone_number(phone):
        """Check the correctness of the phone number"""
        if len(phone) in [5, 6, 7, 8, 9, 10, 11]:
            return phone.isdigit()
        elif len(phone) == 12 and phone[0] == "+":
            return phone[1:].isdigit()
        return False


class PhoneBookController:
    def __init__(self, file_name="contacts.json"):
        self.view = PhoneBookView()
        self.phonebook = PhoneBook(file_name)

    def run(self):
        self.view.show_menu()
        while True:
            choice = self.view.get_input("Выберите пункт меню [0-9]: ")
            actions = {
                "0": self.view.show_menu,
                "1": self.show_all_contacts,
                "2": self.search_contact,
                "3": self.add_contact,
                "4": self.update_contact,
                "5": self.delete_contact,
                "6": self.create_backup,
                "7": self.save_contacts,
                "8": lambda: (self.save_contacts(), exit()),
                "9": exit,
            }

            action = actions.get(choice)
            if action:
                action()
            else:
                self.view.show_message("Неверный выбор.", Fore.RED)

    def show_all_contacts(self):
        """Show all contacts"""
        self.view.show_contacts(self.phonebook.contacts)

    def validate_phone_input(self, phone):
        """Проверка телефона с выводом сообщения об ошибке"""
        while not Validator.validate_phone_number(phone):
            self.view.show_message(
                "Номер телефона введен неверно. Он должен:\n"
                "- содержать 5, 6, 7, 8 цифр\n"
                "- содержать 11 цифр с возможным знаком + перед ними.",
                Fore.RED,
            )
            phone = self.view.get_input("Введите номер телефона заново: ")
        return phone

    def validate_birthday_input(self, birthday):
        """Checking the correctness of the date of birth"""
        if birthday:  # Проверяем, если дата не пуста
            while True:
                is_valid, birthday_or_error = Validator.validate_birthday(birthday)
                if not is_valid:
                    self.view.show_message(birthday_or_error, Fore.RED)
                    birthday = self.view.get_input("Дата рождения (ДД.ММ.ГГГГ): ")
                else:
                    return birthday_or_error
        return None  # Если дата не введена, возвращаем None

    def add_contact(self):
        """Adds a new contact where phone is required and other fields are optional"""
        self.view.show_message("Поля отмеченные '*' - обязательны для заполнения")
        name = self.view.get_input("Имя: ")
        surname = self.view.get_input("Фамилия: ")

        phone = self.view.get_input("Телефон *: ")
        phone = self.validate_phone_input(phone)

        birthday = self.view.get_input("Дата рождения (ДД.ММ.ГГГГ): ")
        birthday = self.validate_birthday_input(birthday)

        if not phone:
            return

        address = self.view.get_input("Адрес: ")
        comment = self.view.get_input("Комментарий: ")

        # Формируем словарь для контакта
        contact_data = {
            "Surname": surname,
            "Name": name,
            "Phone": phone,
            "Birthday": birthday,
            "Address": address,
            "Comment": comment,
        }

        # Добавляем контакт
        self.phonebook.add_contact(contact_data)
        self.view.show_message("Контакт успешно добавлен!", Fore.GREEN)

    def update_contact(self):
        """Update contact"""
        contact_id = self.view.get_contact_id("изменения")
        current_contact = next(
            (
                contact
                for contact in self.phonebook.contacts
                if contact.id == contact_id
            ),
            None,
        )

        if not current_contact:
            self.view.show_message("Контакт не найден.", Fore.RED)
            return

        new_data = self.view.get_new_contact(current_contact)

        # Валидация телефона и даты рождения
        new_data["Phone"] = self.validate_phone_input(new_data["Phone"])
        new_data["Birthday"] = self.validate_birthday_input(
            new_data.get("Birthday", "")
        )

        # Если данные некорректны, выходим
        if not new_data["Phone"]:
            return

        # Обновление данных контакта
        if self.phonebook.update_contact(contact_id, new_data):
            self.view.show_message("Контакт изменен", Fore.GREEN)
        else:
            self.view.show_message("Не удалось обновить контакт.", Fore.RED)

    def search_contact(self):
        """Search contacts"""
        query = self.view.get_search_query()
        found_contacts = self.phonebook.find_contacts(query)
        if found_contacts:
            self.view.show_contacts(found_contacts)
        else:
            self.view.show_message(
                f"Контакты по запросу '{query}' не найдены.", Fore.RED
            )

    def delete_contact(self):
        """Delete contact"""
        contact_id = self.view.get_contact_id("удаления")
        if self.phonebook.delete_contact(contact_id):
            self.view.show_message("Контакт удален", Fore.GREEN)
        else:
            self.view.show_message("Контакт не найден.", Fore.RED)

    def create_backup(self):
        """Create backup"""
        backup_name = self.phonebook.create_backup()
        self.view.show_message(f"Бэкап создан: {backup_name}", Fore.GREEN)

    def save_contacts(self):
        """Save contacts"""
        if self.phonebook.save_contacts():
            self.view.show_message("Контакты сохранены", Fore.GREEN)
        else:
            self.view.show_message("Ошибка сохранения файла.", Fore.RED)
