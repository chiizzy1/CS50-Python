# print a 3 d block

def main():
    # get the number of blocks dimensions
    x = int(input("Enter the number of blocks dimension: "))

    # loop through each row
    for i in range(x):
        get_row(x)
        # print()

# print the elements of the row 
# def get_row(size):
#     for i in range(size):
#         print("#", end="")


def get_row(size):
    print("#" * size)
main()
