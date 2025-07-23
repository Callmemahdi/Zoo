from animals.Snake import Snake

def test_snake_behavior():
    snake = Snake("S001", "george", 3, 12, True, 250, "striped",' yellow' , 8)
    assert snake.make_sound() == "Hissssss"
    assert snake.eat() == "Snake is seating rabbits"
    assert snake.sleep() == "it sleeps at 5PM"
    assert "S001" in snake.info()

def test_is_snake_venomous():
    snake = Snake("S001", "george", 3, 12, True, 250, "striped",' yellow' , 8)
    assert "venomous" in snake.info()
