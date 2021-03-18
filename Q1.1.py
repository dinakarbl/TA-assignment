# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):




    def rt():

    # Use a breakpoint in the code line below to debug your script.
        n=int(input("Enter value of n   "))
        k = 2 * n - 2

    # outer loop to handle number of rows
        for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
            for j in range(0, k):
                print(end=" ")

        # decrementing k after each loop
            k = k - 2

        # inner loop to handle number of columns
        # values changing acc. to outer loop
            for j in range(0, i + 1):
            # printing stars
                print("* ", end="")

        # ending line after each row
            print("\r")
    rt()


# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
