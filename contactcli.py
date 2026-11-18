from contacts_book import ContactsBook
from contact import Contact

class ContactCLI:
    def __init__(self):
        self.book = ContactsBook()

    def add_contact_to_book(self):
        try:
            name = input("enter the name here: ")
            phone_num = input("enter the phone number here: ")

            count = Contact(name, phone_num)
            self.book.add_contact(count)
            print("your entry is valid, the contact has been added successfully")

        except ValueError as e:
            print(e)
    
    def show_all_conacts(self):
        print("\n---- All contacts ----")

        if not self.book.contacts:
            print("the contacts book is empty")
            return
        for cont in self.book.contacts:
            print(cont)
            print("- -"*20)
            
    def view_contact(self):
        try:
            phone_num = input("enter the phone number here: ")

            contact = self.book.view_contact(phone_num)
            print(contact)
            print("your entry is valid, the contact has been showed successfully")

        except ValueError as e:
            print(e)
    
    
    def edit_contact(self):
        try:
            current_phone_num = input("enter the current phone number here: ")
            current_contact = self.book.view_contact(current_phone_num)
            print(current_contact)
            
            new_name = input("enter the new name here: ")
            new_phone_num = input("enter the new phone number here: ")

            self.book.edit_contact(current_phone_num, new_name, new_phone_num)
            print("your entry is valid, the contact has been edited successfully")

        except ValueError as e:
            print(e)
            
    def delete_contact(self):
        try:
            phone_num = input("enter the phone number here: ")

            self.book.delete_contact(phone_num)
            print("your entry is valid, the contact has been deleted successfully")

        except ValueError as e:
            print(e)
    
    def run(self):
        choices = { 1 : "\n1- Add contact",
                    2 : "2- Show all contacts",
                    3 : "3- View contact",
                    4 : "4- Edit contact",
                    5 : "5- Delete contact",
                    6 : "6- Exit\n"
        }

        while True:
            for c in choices.values():
                print(c)

            try:
                choice = int(input("enter your choice: "))
            except ValueError :
                print("your entry is invaild,try agine")
                continue
           
            if choice == 1:
                self.add_contact_to_book()
            elif choice == 2:
                self.show_all_conacts()
            elif choice == 3:
                self.view_contact()
            elif choice == 4:
                self.edit_contact()
            elif choice == 5:
                self.delete_contact()
            elif choice == 6:
                print("Exiting program...")
                break
            else:
                print("Error: Choose a valid number from the menu.")
                continue