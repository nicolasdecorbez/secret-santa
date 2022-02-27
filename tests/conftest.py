import pytest

from secret_santa import Pair, Person, PairsList, PersonsList

@pytest.fixture
def valid_person() -> Person.Person:
    """Return a valid Person()"""
    return Person.Person(
        name="person",
        email="person@email.com"
    )

@pytest.fixture
def valid_pair() -> Pair.Pair:
    """Return a valid Pair()"""
    return Pair.Pair(
        sender=Person.Person("sender", "sender@email.com"),
        receiver=Person.Person("receiver", "receiver@email.com")
    )

@pytest.fixture
def valid_person_list() -> PersonsList.PersonsList:
    """Return a valid PersonList()"""
    persons_list = PersonsList.PersonsList()
    persons_list.register(
        Person.Person("p1", "p1@email.com")
    )
    persons_list.register(
        Person.Person("p2", "p2@email.com")
    )
    return persons_list

@pytest.fixture
def valid_pair_lists() -> PairsList.PairsList:
    """Return a valid PersonList()"""
    pairs_list = PairsList.PairsList()
    pairs_list.register(
        Pair.Pair(
            Person.Person("s1", "s1@email.com"),
            Person.Person("r1", "r1@email.com")
        )
    )
    pairs_list.register(
        Pair.Pair(
            Person.Person("s2", "s1@email.com"),
            Person.Person("r2", "r1@email.com")
        )
    )
    return pairs_list