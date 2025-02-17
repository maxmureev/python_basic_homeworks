import json
import os
import datetime
import shutil
from contact import Contact


class PhoneBook:
    """Telephone directory class"""

    def __init__(self, file_name="contacts.json"):
        self.file_name = file_name
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from file"""
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    return [
                        Contact(
                            id=contact["ID"],
                            surname=contact["Surname"],
                            name=contact["Name"],
                            phone=contact["Phone"],
                            birthday=contact["Birthday"],
                            address=contact["Address"],
                            comment=contact["Comment"],
                        )
                        for contact in data
                    ]
            except json.JSONDecodeError:
                return []
        return []

    def save_contacts(self):
        """Save contacts to file"""
        try:
            with open(self.file_name, "w", encoding="utf-8") as file:
                json.dump(
                    [contact.to_dict() for contact in self.contacts],
                    file,
                    ensure_ascii=False,
                    indent=4,
                )
            return True
        except IOError:
            return False

    def add_contact(self, contact_data):
        """Add new contact"""
        if any(contact.phone == contact_data["Phone"] for contact in self.contacts):
            return False  # Контакт с таким номером уже существует

        new_id = max([contact.id for contact in self.contacts], default=0) + 1

        contact = Contact(
            id=new_id,
            surname=contact_data["Surname"],
            name=contact_data["Name"],
            phone=contact_data["Phone"],
            birthday=contact_data["Birthday"],
            address=contact_data["Address"],
            comment=contact_data["Comment"],
        )

        # Добавляем объект Contact, а не словарь
        self.contacts.append(contact)
        return True

    def find_contacts(self, query):
        """Find contacts by query"""
        return [
            contact
            for contact in self.contacts
            if query.lower() in contact.surname.lower()
            or query.lower() in contact.name.lower()
            or query.lower() in contact.comment.lower()
            or query.lower() in contact.phone.lower()
        ]

    def delete_contact(self, contact_id):
        """Delete_contact by ID"""
        initial_length = len(self.contacts)
        self.contacts = [
            contact for contact in self.contacts if contact.id != contact_id
        ]
        return len(self.contacts) < initial_length

    def update_contact(self, contact_id, new_data):
        """Update contact"""
        for contact in self.contacts:
            if contact.id == contact_id:
                contact.surname = new_data.get("Surname", contact.surname)
                contact.name = new_data.get("Name", contact.name)
                contact.phone = new_data.get("Phone", contact.phone)
                contact.birthday = new_data.get("Birthday", contact.birthday)
                contact.address = new_data.get("Address", contact.address)
                contact.comment = new_data.get("Comment", contact.comment)
                return True
        return False

    def create_backup(self):
        """Create backup"""
        backup_name = f"{os.path.splitext(os.path.basename(self.file_name))[0]}_{datetime.date.today()}_backup.json"
        shutil.copyfile(self.file_name, backup_name)
        return backup_name
