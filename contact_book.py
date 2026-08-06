"""
A simple contact book application that allows users to add, search, update,
delete, and list contacts.

Each contact consists of a name, phone number, and email address.

Classes:
    ContactBook: Manages a collection of contacts with various operations.
    
Methods:
    add_contact(name, phone, email): Adds a new contact to the contact book.
    search_contact(name): Searches for a contact by name.
    update_contact(name, phone=None, email=None): Updates an existing contact's details. Only provided fields are updated.
    delete_contact(name): Deletes a contact from the contact book.
    list_all_contacts(): Lists all contacts in the contact book.
    find_by_phone(phone): Finds a contact by phone number.
"""
class ContactBook:
    def __init__ (self):
        """ Initialize the contact book with an empty dictionary """
        self.contacts = {}  # Instance variable - each ContactBook has its own
    
    def __str__(self):
        """ String representation of the contact book for easy viewing """
        if not self.contacts:
            return "Contact Book is empty"
        result = "=== Contact Book ===\n"
        for name, details in self.contacts.items():
            result += f"{name}: {details['phone']}, {details['email']}\n"
        result += "===================="
        return result
    
    def add_contact(self, name, phone, email):
        """ Add a new contact. Returns True if successful, False if duplicate. """
        if name in self.contacts:
            return False # Indicate failure due to duplicate
        self.contacts[name] = {'phone': phone, 'email': email}
        return True # Indicate successful addition
    
    def search_contact(self, name):
        """ Search for a contact by name. Returns contact dict or None. """
        return self.contacts.get(name, None) # Safe lookup - returns None if not found
    
    def update_contact(self, name, phone=None, email=None):
        """ Update an existing contact. Returns True if successful, False if not found. """
        if name not in self.contacts:
            return False # Indicate failure due to non-existent contact
        if phone is not None:
            self.contacts[name]['phone'] = phone
        if email is not None:
            self.contacts[name]['email'] = email
        return True # Indicate successful update
    
    def delete_contact(self, name):
        """ Delete a contact. Returns True if successful, False if not found. """
        if name not in self.contacts:
            return False # Indicate failure due to non-existent contact
        self.contacts.pop(name) 
        return True # Indicate successful deletion
    
    def list_all_contacts(self):
        """ Return dictionary of all contacts. """
        return self.contacts
    
    def find_by_phone(self, phone):
        """ Find a contact by phone number. Returns name or None. """
        for name, details in self.contacts.items():
            if details['phone'] == phone:
                return name
        return None
    
if __name__ == "__main__":
    # Example usage:
    book = ContactBook()

    # Test add
    print("=== Testing Add ===")
    print(f"Add Alice: {book.add_contact('Alice', '555-1234', 'alice@example.com')}")  # True
    print(f"Add Bob: {book.add_contact('Bob', '555-5678', 'bob@example.com')}")  # True
    print(f"Add Charlie: {book.add_contact('Charlie', '555-9999', 'charlie@example.com')}")  # True
    print(f"Add Alice again: {book.add_contact('Alice', '555-0000', 'alice2@example.com')}")  # False (duplicate)

    # Test __str__
    print("\n=== Testing Pretty Print ===")
    print(book)

    # Test search
    print("\n=== Testing Search ===")
    print(f"Search Alice: {book.search_contact('Alice')}")
    print(f"Search David: {book.search_contact('David')}")  # None

    # Test find_by_phone (THIS WILL NOW WORK CORRECTLY!)
    print("\n=== Testing Find by Phone ===")
    print(f"Find 555-1234: {book.find_by_phone('555-1234')}")  # Alice
    print(f"Find 555-5678: {book.find_by_phone('555-5678')}")  # Bob (THIS WOULD HAVE FAILED BEFORE!)
    print(f"Find 555-9999: {book.find_by_phone('555-9999')}")  # Charlie
    print(f"Find 555-0000: {book.find_by_phone('555-0000')}")  # None

    # Test update
    print("\n=== Testing Update ===")
    print(f"Update Alice phone: {book.update_contact('Alice', phone='555-XXXX')}")  # True
    print(f"Alice after update: {book.search_contact('Alice')}")
    print(f"Update David: {book.update_contact('David', phone='555-1111')}")  # False

    # Test delete
    print("\n=== Testing Delete ===")
    print(f"Delete Bob: {book.delete_contact('Bob')}")  # True
    print(f"Delete David: {book.delete_contact('David')}")  # False
    print("\nFinal contact book:")
    print(book)