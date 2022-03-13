"""
Introduction to Console Programming
Writing a function to print a menu
"""
import time


# Menu options in print statement
def print_menu1():
    print('1 -- Stringy')
    print('2 -- Numby')
    print('3 -- Listy')
    print('4 -- Swap')
    print('5 -- Matrices')
    print('6 -- Ship')
    print('7 -- Exit')
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Stringy',
    2: 'Numby',
    3: 'Listy',
    4: 'Swap',
    5: 'Matrices',
    6: 'Ship',
    7: 'Exit'
}


# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    runOptions()


# menu option 1
def stringy():
    print('You chose \' 1 -  Stringy\'')


# menu option 2
def numby():
    print('You chose \' 2 - Numby\'')


# menu option 3
def listy():
    print('You chose \'3 - Listy\'')


def swap():
    x = int(input('input a number '))
    y = int(input('input a number '))
    swap2(x, y)
    print(x, y)


def swap2(a, b):
    if (a > b or a == b):
        temp = a
        a = b
        b = temp
        return a, b


def matrice():
    matrix = [[
        input("input a number "),
        input("input a number "),
        input("input a number ")
    ],
              [
                  input("input a number "),
                  input("input a number "),
                  input("input a number ")
              ],
              [
                  input("input a number "),
                  input("input a number "),
                  input("input a number ")
              ]]
    newMatrix = []
    matrice2(matrix, newMatrix)
    matrice3(newMatrix)


def matrice2(matrix, newMatrix):
    for w in range(len(matrix)):
        for y in range(len(matrix[w])):
            newMatrix.append(matrix[w][y])
    return (newMatrix)


def matrice3(newMatrix):
    print(newMatrix[0], newMatrix[1], newMatrix[2])
    print(newMatrix[3], newMatrix[4], newMatrix[5])
    print(newMatrix[6], newMatrix[7], newMatrix[8])

    # terminal print commands


ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"


def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "▀██▀─▄███▄─▀██─██▀██▀▀█")
    print(sp + "─██─███─███─██─██─██▄█")
    print(sp + "─██─▀██▄██▀─▀█▄█▀─██▀█")
    print(sp + "▄██▄▄█▀▀▀─────▀──▄██▄▄█")
    print(SHIP_COLOR, end="")
    print(RESET_COLOR)


# ship function, iterface into this file
def ship():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        ship_print(position)  # call to function with parameter
        time.sleep(.1)


#prefuncy.py

Blue = "\033[94m"
Pink = "\033[91m"
BrightPink = "\033[95m"


def christmasTree():
    print("\033[93m           * \033[92m")
    time.sleep(.5)
    print("\033[92m          * *")
    time.sleep(.5)
    print("         * \033[94m*\033[92m *")
    time.sleep(.5)
    print("        * * \033[95m*\033[92m *")
    time.sleep(.5)
    print("       * \033[94m*\033[92m * * *")
    time.sleep(.5)
    print("      * * * * \033[95m*\033[92m *")
    time.sleep(.5)
    print("     * * \033[94m*\033[92m * * * *")
    time.sleep(.5)
    print("    * \033[94m*\033[92m * * * \033[95m*\033[92m * *")
    time.sleep(.5)
    print("   * * \033[95m*\033[92m * * \033[94m*\033[92m * * *")
    time.sleep(.5)
    print("  * * * * * \033[94m*\033[92m * * * *")
    time.sleep(.5)
    print(" * * * \033[95m*\033[92m * * * * * * * \033[93m")
    time.sleep(.5)
    print("         * * *")
    time.sleep(.5)
    print("         * * * \u001b[37m")


# call functions based on input choice


def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-6: '))
            if option == 1:
                stringy()
            elif option == 2:
                numby()
            elif option == 3:
                listy()
            elif option == 4:
                swap()
            # Exit menu
            elif option == 5:
                matrice()
            elif option == 6:
                ship()
            elif option == 7:
                print('Exiting! Thank you! Good Bye...')
                exit()  # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


if __name__ == '__main__':
    # print_menu1()
    print_menu2()
