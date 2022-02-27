def test_person_init(valid_person):
    """Check Person() init."""
    assert valid_person.name == "person"
    assert valid_person.email == "person@email.com"

def test_person_add_rule(valid_person):
    """Check Person() rules append."""
    assert valid_person.create_rule("rule@email.com") == True
    assert "rule@email.com" in valid_person.rules

def test_person_add_existing_rule(valid_person):
    """Check Person() rules append with an existing rule."""
    valid_person.create_rule("rule@email.com")
    assert "rule@email.com" in valid_person.rules
    assert valid_person.create_rule("rule@email.com") == False

def test_person_remove_rule(valid_person):
    """Check Person() rules remove."""
    valid_person.create_rule("rule@email.com")
    assert valid_person.remove_rule("rule@email.com") == True
    assert not "rule@email.com" in valid_person.rules

def test_person_remove_non_existent_rule(valid_person):
    """Check Person() rules append."""
    assert valid_person.remove_rule("rule@email.com") == False