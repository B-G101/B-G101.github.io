"""
Introduction to Console Programming
Writing a function to print a menu
"""


# Menu options in print statement
def print_menu1():
    print('1 -- Stringy')
    print('2 -- Numby')
    print('3 -- Listy')
    print('4 -- Swap')
    print('5 -- Matrices')
    print('6 -- Exit')
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Stringy',
    2: 'Numby',
    3: 'Listy',
    4: 'Swap',
    5: 'Matrices',
    6: 'Exit'
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
    x, y = swap2(x, y)
    print(x, y)


def swap2(a, b):
    if (a > b or a == b):
        temp = a
        a = b
        b = temp
        return a, b


def matrice():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    newMatrix = []
    matrice2(matrix, newMatrix)
    print (newMatrix)
    matrice3(newMatrix)

def matrice2(matrix, newMatrix):
    for w in range(len(matrix)):
        for y in range(len(matrix[w])):
            newMatrix.append(matrix[w][y])
    return(newMatrix)

def matrice3(newMatrix):
    


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
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
                print('Exiting! Thank you! Good Bye...')
                exit()  # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


if __name__ == '__main__':
    # print_menu1()
    print_menu2()
