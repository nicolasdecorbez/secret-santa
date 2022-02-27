"""
Define the Pair() object, to register pairs of Persons (a receiver and a sender)
"""

from .Person import Person

class Pair:
    """
    Register a person by its name, email and rules.
    """
    def __init__(self, sender: Person, receiver: Person):
        """
        Initalize a Person object with following specs: 
            - sender: Person
            - receiver: Person
        """
        self.sender = sender
        self.receiver = receiver