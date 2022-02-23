"""
Define the Person() object, and methods to manage rules.
"""

class Person:
    """
    Register a person by its name, email and rules.
    """
    def __init__(self, name, email):
        """
        Initalize a Person object with following specs: 
            - name: str
            - email: str
            - rules: list (empty by default)
        """
        self.name = name
        self.email = email
        self.rules = []
        self.rules.append(self.email)

    def create_rule(self, email: str) -> bool:
        """
        Add a rule (an email to avoid) to the Person object.
        """
        if email in self.rules:
            print("ERROR: Rule already exists.")
            return False
        self.rules.append(email)
        print("SUCCESS: Rule added.")
        return True
        
    def remove_rule(self, email: str) -> bool:
        """
        Remove a rule (an email to avoid) from the Person object.
        """
        for i in range(len(self.rules)):
            if self.rules[i] == email:
                self.rules.pop(i)
                print("SUCCESS: Rule deleted.")
                return True
        print("ERROR: Rule doesn't exists.")
        return False