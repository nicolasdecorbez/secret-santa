# import random
# import json

from src.Person import Person
from src.PersonList import PersonList
from src.Pair import Pair
from src.PairsList import PairsList


persons_list = PersonList()
pairs_list = PairsList()


def register_new_person(name: str, email: str):
    """
    Create a new Person object to add a new person into the list.
    """
    new_person = Person(name=name, email=email)
    persons_list.register(new_person)


def register_new_pair(sender_email: str, receiver_email: str):
    """
    Create a new Pair object to register a pair of Person().
    """
    new_pair = Pair(
        persons_list.find(sender_email),
        persons_list.find(receiver_email)
    )
    pairs_list.register(new_pair)


def main():
    register_new_person("toto", "toto@gmail.com")
    register_new_person("tata", "tata@gmail.com")
    persons_list.print()
    register_new_pair("toto@gmail.com", "tata@gmail.com")
    pairs_list.print()


if __name__ == "__main__":
    main()