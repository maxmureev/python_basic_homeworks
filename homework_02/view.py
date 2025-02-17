from tabulate import tabulate
from colorama import Fore, Style


class PhoneBookView:
    """Class for displaying information to user"""

    @staticmethod
    def show_menu():
        print(
            "\nМеню:\n"
            "0. Показать меню\n"
            "1. Показать все контакты\n"
            "2. Найти контакт\n"
            "3. Создать новый контакт\n"
            "4. Изменить контакт\n"
            "5. Удалить контакт\n"
            "6. Создать бэкап контактов\n"
            "7. Сохранить контакты\n"
            "8. Сохранить и выйти\n"
            "9. Выйти без сохранения\n"
        )

    @staticmethod
    def show_contacts(contacts, all_contacts=None):
        """Show contacts in a table format"""
        if not contacts:  # Проверка на пустоту списка контактов
            print(
                Fore.RED
                + "Телефонная книга пуста, создайте новый контакт"
                + Style.RESET_ALL
            )
        elif all_contacts and len(all_contacts) > 0:
            print(Fore.RED + "Контакт с таким ID не найден." + Style.RESET_ALL)
        else:
            table_data = [
                [
                    contact.id,
                    contact.surname,
                    contact.name,
                    contact.phone,
                    contact.birthday,
                    contact.address,
                    contact.comment,
                ]
                for contact in contacts
            ]
            headers = [
                "ID",
                "Фамилия",
                "Имя",
                "Телефон",
                "Дата рождения",
                "Адрес",
                "Комментарий",
            ]
            print(tabulate(table_data, headers, tablefmt="grid"))

    @staticmethod
    def show_message(message, color=Fore.WHITE):
        """Print message"""
        print(color + message + Style.RESET_ALL)

    @staticmethod
    def get_input(prompt, color=Fore.YELLOW):
        """Get input from user"""
        return input(color + prompt + Style.RESET_ALL)

    def get_new_contact(self, current_contact=None):
        """Requests data for contact"""
        contact_data = {}
        fields = [
            ("Surname", "Фамилия"),
            ("Name", "Имя"),
            ("Phone", "Телефон"),
            ("Birthday", "Дата рождения (дд.мм.гггг)"),
            ("Address", "Адрес"),
            ("Comment", "Комментарий"),
        ]

        for field, prompt in fields:
            current_value = (
                getattr(current_contact, field.lower(), "") if current_contact else ""
            )
            new_value = self.get_input(f"{prompt} [{current_value}]: ")
            contact_data[field] = new_value if new_value else current_value

        return contact_data

    def get_search_query(self):
        """Get search query"""
        return self.get_input("Введите запрос для поиска: ")

    def get_contact_id(self, action):
        """Get contact ID"""
        while True:
            try:
                return int(self.get_input(f"Введите ID контакта для {action}: "))
            except ValueError:
                self.show_message("Ошибка: ID должен быть числом", Fore.RED)
