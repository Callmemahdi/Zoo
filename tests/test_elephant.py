from animals.Elephant import Elephant
def test_elephant_behavior():
    elephant = Elephant('E001', 'Horton', 11, 3500, 450, 250, 'Asian', 'jungle', 43,)
    assert elephant.make_sound() == "Pawooooo"
    assert elephant.eat() == "Elephant is eating vegetables"
    assert elephant.sleep() == "Elephant is sleeping at 9AM"
    assert "E001" in elephant.info()
