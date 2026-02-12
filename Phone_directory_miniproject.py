from operator import truediv


class Contact: # class which stores all contacts
     phone_directory = []      # class variable it shares all details to all objects
     def __init__(self,name,phone_number):  # instance variable used to accept values and not shown to other
         self.phone = phone_number
         self.name = name
         Contact.phone_directory.append(self)

     def  show_contact(self):  #  instance methods as function to provide outputs
         return f"Name: {self.name}, Phone Number: {self.phone}"

     @classmethod     # class method created to use class variable
     def show_all_contact(cls):   # class method function to access class variable
         if len(Contact.phone_directory) == 0:
             print("No contact found int the phone directory!!")
         else:
             print("All contacts from the directory ==>")
             for contact in Contact.phone_directory:
                 print(contact.show_contact())

     @classmethod
     def search_contact(cls,search_name):
         for contact in Contact.phone_directory:
             if contact.name.lower() == search_name.lower():
                 return contact.phone
         return f"No contact found for this {search_name} "

     @staticmethod  #static method not bound to any class variable
     def validate_phone_number(number):
         if len(number) >=8 and number.isdigit():
             return True
         else:
             return False


n_contacts = int(input("How many number you want to add : "))
for i in range(n_contacts):
    name = input("Enter the name of contact: ")
    phone_number = input("Enter your phone number: ")
    if Contact.validate_phone_number(phone_number):
        Contact(name, phone_number)
    else:
        print(f"Invalid phone number for {name}, phone number should be 8 digits and contains digit in it..")

Contact.show_all_contact()
