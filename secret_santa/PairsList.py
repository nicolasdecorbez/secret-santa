"""
Register different methods to manage Pairs lists, 
i.e. finding a pair or adding / deleting some
"""

from .Person import Person
from .Pair import Pair

class PairsList:
    """
    Register a person by its name, email and rules.
    """
    def __init__(self):
        """
        Initalize a PairsList object with following specs: 
            - pairs: list of Pair() objects
        """
        self.pairs = list()
    
    # More methods to interact with pairs. Unused on 0.1.0
    #
    # def find_receiver(self, sender: Person) -> Person:
    #     """
    #     Returns a paired person object based on the sender, or None. 
    #     """
    #     for i in range(len(self.pairs)):
    #         if sender == self.pairs[i].sender:
    #             return self.pairs[i].receiver
    #     return None

    # def find_sender(self, receiver: Person) -> Person:
    #     """
    #     Returns a paired person object based on the receiver, or None. 
    #     """
    #     for i in range(len(self.pairs)):
    #         if receiver == self.pairs[i].receiver:
    #             return self.pairs[i].sender
    #     return None

    # def find_sender_pair(self, sender: Person) -> Pair:
    #     """
    #     Returns the Pair() object based on the sender, or None. 
    #     """
    #     for i in range(len(self.pairs)):
    #         if sender == self.pairs[i].sender:
    #             return self.pairs[i]
    #     return None

    # def find_receiver_pair(self, receiver: Person) -> Pair:
    #     """
    #     Returns the Pair() object based on the receiver, or None. 
    #     """
    #     for i in range(len(self.pairs)):
    #         if receiver == self.pairs[i].receiver:
    #             return self.pairs[i]
    #     return None

    def find_pair(self, pair: Pair) -> Pair:
        """
        Returns a registered Pair() object, or None. 
        """
        for i in range(len(self.pairs)):
            if pair == self.pairs[i]:
                return self.pairs[i]
        return None

    def register(self, pair: Pair) -> bool:
        """
        Add a Pair() object to the list.
        """
        if self.find_pair(pair):
            print("ERROR: Pair already exists.")
            return False
        self.pairs.append(pair)
        print("SUCCESS: Pair added.")
        return True
        
    def remove(self, pair: Pair) -> bool:
        """
        Remove a Pair() from the Person object.
        """
        self.pairs.remove(pair)
        print("SUCCESS: Pair deleted.")
        return True

    def print(self) -> None:
        """
        Print the pairs list.
        """
        for i in range(len(self.pairs)):
            print(f'{i}: "{self.pairs[i].sender.email}" to "{self.pairs[i].receiver.email}"')