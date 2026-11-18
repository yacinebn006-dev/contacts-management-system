class Contact:
    def __init__(self, name, phone_num):
        if not name.strip() or not phone_num.strip():
            raise ValueError("Error, your enter invalid!")
        if not phone_num.strip().isdigit():
            raise ValueError("Error: phone number must contain digits only!")

        self.phone_num = phone_num.strip()
        self.name = name.strip()

    def edit_contact(self,new_name = None, new_phone_num = None):
        if not new_name and not new_phone_num:
            raise ValueError("Error: you most provid at least one value to edit!")
        
        if new_name is not None and new_name.strip():
            self.name = new_name.strip()
            
        if new_phone_num is not None and new_phone_num.strip():
            if not new_phone_num.strip().isdigit():
                raise ValueError("Error: New phone number must contain digits only!")
            self.phone_num = new_phone_num.strip()

    def __str__(self):
        return f"info: Name: {self.name}, phone: {self.phone_num}"
