from src.arthimetic import add, sub

def test_add():
    assert add(1,8) == 9
    assert add(2,3) == 5

def test_sub():
    assert sub(7,2) == 5
    assert sub(4,1) == 3