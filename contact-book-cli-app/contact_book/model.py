import datetime


class Contact:
    def __init__(self, name, contact_number, position=None, date_created=None, date_updated=None):
        self.name = name
        self.contact_number = contact_number
        self.position = position
        self.date_created = date_created if date_created is not None else datetime.datetime.now().isoformat()
        self.date_updated = date_updated if date_updated is not None else datetime.datetime.now().isoformat()

    def __repr__(self) -> str:
        return f"({self.name}, {self.contact_number}, {self.position}, {self.date_created}, {self.date_updated})"
