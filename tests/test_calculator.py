
'''My Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0
    
from faker import Faker
fake = Faker()

def test_addition():
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    expected = a + b
    assert calculator.add(a, b) == expected
