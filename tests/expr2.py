def test_boolOp():
    a: bool
    b: bool
    a = False
    b = True
    a = a and b
    b = a or True
    a = a or b
    a = a and b == b
    a = a and b != b
    a = b or b
