"""
Register different methods to manage Persons lists, i.e. register 
or delete a person, find one ...
"""

from src.Person import Person

class PersonList:
    """
    Register a person by its name, email and rules.
    """
    def __init__(self):
        """
        Initalize a PersonList object with following specs: 
            - persons: list of Person() objects
        """
        self.persons = list()
        
    def find(self, email) -> Person:
        """
        Returns a registered person object based on an email address, or None. 
        """
        for i in range(len(self.persons)):
            if email == self.persons[i].email:
                return self.persons[i]
        return None

    def register(self, person: Person) -> bool:
        """
        Add a rule (an email to avoid) to the Person object.
        """
        if self.find(person.email):
            print("ERROR: Person already exists.")
            return False
        self.persons.append(person)
        print("SUCCESS: Person added.")
        return True
        
    def delete(self, email: str) -> bool:
        """
        Remove a rule (an email to avoid) from the Person object.
        """
        to_delete: Person = self.find(email)
        if not to_delete:
            print("ERROR: Person doesn't exists.")
            return False
        self.persons.remove(to_delete)
        print("SUCCESS: Person deleted.")
        return True

    def print(self) -> None:
        """
        Print the persons list with or without indexes.
        """
        for i in range(len(self.persons)):
            print(f'{i}: "{self.persons[i].name}", "{self.persons[i].email}", {self.persons[i].rules}')