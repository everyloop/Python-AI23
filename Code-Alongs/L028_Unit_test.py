from L027_Module import square, greet

def test_positive_square():
    assert square(2) == 4
    assert square(5) == 25

def test_negative_square():
    assert square(-2) == 4
    assert square(-5) == 25

def test_zero_square():
    assert square(0) == 0

def test_greet_default():
    assert greet() == "Hello, world"

def test_greet_argument():
    assert greet("Fredrik") == "Hello, Fredrik"


# import math
# print(L027_Module.square(9))
# print(L027_Module.sqrt(9))
# print(math.sqrt(9))

