class ContactsBook:
    def __init__(self):
        self.contacts = []

    def _find_by_phone(self, phone):
        return next((c for c in self.contacts if c.phone_num == phone),None)

    def add_contact(self, contact):
        
        if self._find_by_phone(contact.phone_num):
            raise ValueError("ُError, the contact is already exist in contacts book")
        self.contacts.append(contact)

    def edit_contact(self, phone_num, new_name, new_phone_num):
        cont = self._find_by_phone(phone_num)

        if not cont:
            raise ValueError("Error: The contact is not found in contactbook.")
        if new_phone_num and new_phone_num.strip() and new_phone_num.strip() != phone_num:
            if self._find_by_phone(new_phone_num.strip()):
                raise ValueError("Error: The new phone number already exists for another contact!")
        
        cont.edit_contact(new_name, new_phone_num)

    def view_contact(self, phone):
        cont = self._find_by_phone(phone)
        if not cont:
            raise ValueError("ُError, the contact is not found in contacts book")
        return cont

    def delete_contact(self, phone):
        cont = self._find_by_phone(phone)
        if not cont:
            raise ValueError("ُError, the contact is not found in contacts book")
        self.contacts.remove(cont)

    def __iter__(self):
        return iter(self.contacts)