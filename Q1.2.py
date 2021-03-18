# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    def char():
        m = int(input("Enter value of m    "))
        #assigning character A to c in ascii value
        c = 65
        for x in range(0, m):
            for y in range(0, x + 1):
                #converting ascii value to character
                ch = chr(c)
                #printing character
                print(ch, end=" ")
                #incrementing to next character
                c = c + 1
            #ending line after each row
            print("\r")


    char()

# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
