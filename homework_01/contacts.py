import json
import os.path
import datetime
import shutil

from tabulate import tabulate
from colorama import Fore, Style


def open_file(file_name):
    """Open file and upload contacts"""
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            contacts = json.load(file)
    else:
        contacts = []
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(contacts, file, ensure_ascii=False, indent=4)
    return contacts


def save_file(contacts, file_name):
    """Save contacts to file"""
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)


def show_contacts(contacts):
    """Show contacts in table"""
    if contacts:
        table_data = [
            [
                contact["ID"], contact["Surname"], contact["Name"], contact["Phone"],
                contact["Birthday"], contact["Address"], contact["Comment"]
            ]
            for contact in contacts
        ]
        headers = ["ID", "Фамилия", "Имя", "Телефон", "Дата рождения", "Адрес", "Комментарий"]
        print(tabulate(table_data, headers, tablefmt="grid"))
    else:
        print(Fore.RED + "\nКонтакты не найдены" + Style.RESET_ALL)


def create_contact(contacts):
    """Create new contact"""
    new_id = max([contact["ID"] for contact in contacts], default=0) + 1

    print('Создание нового контакта:\n')
    surname = input(Fore.BLUE + "Фамилия: ")
    name = input("Имя: ")
    phone = input("Телефон: ")
    birthday = input("Дата рождения (дд.мм.гггг): ")
    address = input("Адрес: ")
    comment = input("Комментарий: " + Style.RESET_ALL)

    new_contact = {
        "ID": new_id,
        "Surname": surname,
        "Name": name,
        "Phone": phone,
        "Birthday": birthday,
        "Address": address,
        "Comment": comment
    }

    contacts.append(new_contact)
    print(Fore.GREEN + "\nКонтакт успешно добавлен. Не забудьте сохранить изменения" + Style.RESET_ALL)


def find_contact(contacts):
    """Find contacts"""
    search = input(Fore.BLUE + "Введите запрос для поиска: " + Style.RESET_ALL)
    found_contacts = [contact for contact in contacts if
                      search.lower() in contact["Surname"].lower() or
                      search.lower() in contact["Name"].lower() or
                      search.lower() in contact["Comment"].lower() or
                      search.lower() in contact["Phone"].lower()]
    if found_contacts:
        show_contacts(found_contacts)
    else:
        print(Fore.RED + "\nКонтакт не найден" + Style.RESET_ALL)


def edit_contact(contacts):
    """Change contact"""
    try:
        contact_id = int(input(Fore.BLUE + "Введите ID контакта для редактирования: " + Style.RESET_ALL))
    except ValueError:
        print("\nВведенное значение должно быть числом")
        return delete_contact(contacts)

    contact = next((contact for contact in contacts if contact["ID"] == contact_id), None)

    if contact:
        print(f"Редактирование контакта: {contact['Name']} {contact['Surname']}\n")

        contact["Surname"] = input(f"Фамилия ({contact['Surname']}): ") or contact["Surname"]
        contact["Name"] = input(f"Имя ({contact['Name']}): ") or contact["Name"]
        contact["Phone"] = input(f"Телефон ({contact['Phone']}): ") or contact["Phone"]
        contact["Birthday"] = input(f"Дата рождения ({contact['Birthday']}): ") or contact["Birthday"]
        contact["Address"] = input(f"Адрес ({contact['Address']}): ") or contact["Address"]
        contact["Comment"] = input(f"Комментарий ({contact['Comment']}): " + Style.RESET_ALL) or contact["Comment"]
        print(Fore.GREEN + "\nКонтакт успешно изменен. Не забудьте сохранить изменения" + Style.RESET_ALL)
    else:
        choice = input(f"\nКонтакт с таким ID не найден. Попробовать еще раз? [yes|No]: ")
        if choice == 'yes':
            return edit_contact(contacts)


def delete_contact(contacts):
    """Remove contact"""
    try:
        contact_id = int(input(Fore.BLUE + "Введите ID контакта для удаления: " + Style.RESET_ALL))
    except ValueError:
        print("\nВведенное значение должно быть числом")
        return delete_contact(contacts)

    contact = next((contact for contact in contacts if contact["ID"] == contact_id), None)
    if contact:
        choice = input(f"Удалить контакт \"{contact['Name']} {contact['Surname']}\"? [yes|No]: ")
        if choice == 'yes':
            contacts.remove(contact)
            print(Fore.GREEN + "\nКонтакт успешно удален. Не забудьте сохранить изменения" + Style.RESET_ALL)
        else:
            print("\nКонтакт не был изменен")
    else:
        choice = input(f"\nКонтакт с таким ID не найден. Попробовать еще раз? [yes|No]: ")
        if choice == 'yes':
            return delete_contact(contacts)


def create_backup(file_name):
    """Backup contacts"""
    backup_name = os.path.splitext(os.path.basename(file_name))[0] + "_" + str(datetime.date.today()) + "_backup.json"
    shutil.copyfile(file_name, backup_name)
    print(Fore.GREEN + "\nБэкап сохранен в файл: " + backup_name + Style.RESET_ALL)


def menu():
    """User menu"""
    file_name = 'contacts.json'
    contacts = open_file(file_name)

    def help_func():
        print("\nМеню:")
        print("1. Показать все контакты")
        print("2. Найти контакт")
        print("3. Создать новый контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Создать бэкап контактов")
        print("7. Сохранить контакты")
        print("8. Сохранить и выйти")
        print("9. Выйти без сохранения")

    help_func()

    while True:
        choice = input(Fore.BLUE + "\nВыберите пункт меню [1-9]: " + Style.RESET_ALL)
        if choice == '1':
            show_contacts(contacts)
        elif choice == '2':
            find_contact(contacts)
        elif choice == '3':
            create_contact(contacts)
        elif choice == '4':
            show_contacts(contacts)
            edit_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            create_backup(file_name)
        elif choice == '7':
            save_file(contacts, file_name)
            print(Fore.GREEN + "\nКонтакты успешно сохранены" + Style.RESET_ALL)
        elif choice == '8':
            save_file(contacts, file_name)
            print("\nКонтакты сохранены")
            break
        elif choice == '9':
            print("\nЗакрытие контактов")
            break
        elif choice == 'help':
            help_func()
        else:
            print(Fore.RED + "\nНеверный выбор, попробуйте еще раз" + Style.RESET_ALL)
            help_func()


menu()
