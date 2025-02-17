from dataclasses import dataclass


@dataclass
class Contact:
    """Class representing contact"""

    def __init__(self, id, surname, name, phone, birthday, address, comment):
        self.id = id
        self.surname = surname
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.address = address
        self.comment = comment

    def to_dict(self):
        """Returns the contact as a dictionary"""
        return {
            "ID": self.id,
            "Surname": self.surname,
            "Name": self.name,
            "Phone": self.phone,
            "Birthday": self.birthday,
            "Address": self.address,
            "Comment": self.comment,
        }
