import pytest

from secret_santa import Pair, Person, PairsList, PersonsList

@pytest.fixture
def valid_person() -> Person:
    """Return a valid Person()"""
    return Person(
        name="person",
        email="person@email.com"
    )

@pytest.fixture
def valid_pair() -> Pair:
    """Return a valid Pair()"""
    return Pair(
        sender=Person("sender", "sender@email.com"),
        receiver=Person("receiver", "receiver@email.com")
    )

@pytest.fixture
def valid_person_list() -> PersonsList:
    """Return a valid PersonList()"""
    persons_list = PersonsList()
    persons_list.register(
        Person("p1", "p1@email.com")
    )
    persons_list.register(
        Person("p2", "p2@email.com")
    )
    return persons_list

@pytest.fixture
def valid_pair_lists() -> PairsList:
    """Return a valid PersonList()"""
    pairs_list = PairsList()
    pairs_list.register(
        Pair(
            Person("s1", "s1@email.com"),
            Person("r1", "r1@email.com")
        )
    )
    pairs_list.register(
        Pair(
            Person("s2", "s1@email.com"),
            Person("r2", "r1@email.com")
        )
    )
    return pairs_list