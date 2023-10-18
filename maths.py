def main():
        x = int(input("enter a number? "))

        if is_even(x):
                print(f"{x} is an even number")
        else:
                print(x, "is not an even number!")

def is_even(x):
        return x % 2 == 0

main()