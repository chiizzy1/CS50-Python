def main():

    x = int(input("what's x? "))
    print(f"x squared is {square(x)}")


def square(n):
    return n ** 2

if __name__ == "__main__":
    main()