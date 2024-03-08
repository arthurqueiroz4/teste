def isInFib(target):
    a, b = 0, 1
    while a <= target:
        if a == target:
            return True
        else:
            a, b = b, a + b
    return False

try:
    assert isInFib(1) == True
    assert isInFib(2) == True
    assert isInFib(3) == True
    assert isInFib(5) == True
    assert isInFib(8) == True
    assert isInFib(13) == True
    assert isInFib(21) == True
    assert isInFib(34) == True
    assert isInFib(56) == False
    assert isInFib(90) == False
    print("All tests passed")
except:
    print("Some tests failed")