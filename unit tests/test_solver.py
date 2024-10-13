from solver import solve

def test_no_roots():
    assert solve(1, 0, 1) == []  #тест отсутствия корней
