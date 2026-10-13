from calculator import square
def main():
    test_square()


def test_positive():
   assert square(2) == 4
   assert square(4) == 9

def test_negative():
    assert square(-5) == 25
    assert square(-2) == 4

def test_null():
    assert square(0) == 0

if __name__ == "__main__":
    main()
