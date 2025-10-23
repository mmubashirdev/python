import pytest
from mathOperation import add, sub, mul, div
def test_add():
    assert add(3, 2) == 5
def test_sub():
    assert sub(10, 2) == 8
def test_mul():
    assert mul(5, 5) == 25
def test_div():
    assert div(4,2) == 2
        
def test_addEdge():
    assert add(0,0) == 0
    assert add(-1,1) == 0
def test_subEdge():
    assert sub(0,-10) == 10
def test_mulEdge():
    assert mul(0,2) == 0
    assert mul(-2,2) == -4
def test_divEdge():
     assert div(-10,5) == -2
     assert div(0,5) == 0

def test_divError():
    with pytest.raises(ValueError):
        div(25,0)
def test_InvalidInput():
  with pytest.raises(TypeError):
    add("a",4)