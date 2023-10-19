def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    # keep prompting the user to enter a valiid number
    while True:
        try:
            x = int(input("Enter a random number: "))
        except ValueError:
            print("x is not a valid number")
        else:
            return x
            

   


main()