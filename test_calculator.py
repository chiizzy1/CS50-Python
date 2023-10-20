# from calculator import square


# def main():

#     test_square()

# def test_square():
#     # if square(2) != 4:
#     #     print("2 square should be 4")
#     # if square(3) != 9:
#     #     print("3 square should be 9")

#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-3) == 9
#     assert square(-2) == 4
#     assert square(0) == 9

# if __name__ == "__main__":
#     main()


from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0