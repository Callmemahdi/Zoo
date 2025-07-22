from animals.Lion import Lion

def test_lion_make_sound():
    lion = Lion("Oscar", 5, 160, 25, 60, 40, 30, "alpha", 110)
    assert lion.make_sound() == "roar"

def test_lion_eat():
    lion = Lion("Oscar", 5, 160, 25, 60, 40, 30, "alpha", 110)
    assert lion.eat() == "it's eating meet"

def test_lion_sleep():
    lion = Lion("Oscar", 5, 160, 25, 60, 40, 30, "alpha", 110)
    assert lion.sleep() == "it sleeps at 11AM"


def test_lion_info():
    lion = Lion("Oscar", 5, 160, 25, 60, 40, 30, "alpha", 110)
    info = lion.info()
    assert "Oscar" in info
    assert "mane_size" in info.lower()

def test_lion_eat_and_sleep():
    lion = Lion("Oscar", 5, 160, 25, 60, 40, 30, "alpha", 110)
    assert lion.eat() == "it's eating meet"
    assert lion.sleep() == "it sleeps at 11AM"

def test_lion_eat_and_sleep():
    lion = Lion("Oscar", 5, 160, 25, 60, 40, 30, "alpha", 110)
    assert lion.eat() == "it's eating meet"
    assert lion.sleep() == "it sleeps at 11AM"

def test_lion_properties():
    lion = Lion("Oscar", 5, 160, 25, 60, 40, 30, "alpha", 110)
    lion.age = 10
    lion.weight = 300
    assert lion.age == 10
    assert lion.weight == 300

def test_lion_str_repr():
    lion = Lion("Oscar", 5, 160, 25, 60, 40, 30, "alpha", 110)
    assert "Lion" in str(lion)
    assert "Oscar" in repr(lion)
