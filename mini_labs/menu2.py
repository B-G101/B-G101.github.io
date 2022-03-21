# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

import menu
import tt1


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Animation", menu.ship],
    ["Christmas Tree", menu.christmasTree],
    ["Factorial", tt1.for_loop],
    ["Factorial", tt1.while_loop],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Swap", menu.swap],
    ["Matrices", menu.matrice],
]

patterns_sub_menu = [
    ["Patterns", None],
    ["PreFuncy", None],
    ["Funcy", None],
]

loops_sub_menu = [
    ["For Loop", tt1.for_loop],
    ["While Loop", tt1.while_loop],
    ["Recursive Loop", str(tt1.recursive_loop(0))],
    ["All Loops", tt1.tester],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


      
# def patterns_submenuc
# using patterns_sub_menu list:
# patterns_submenuc works similarly to menuc
def patterns_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, patterns_sub_menu)
    m.menu()


def loops_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, loops_sub_menu)
    m.menu()
  
# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    print(title)
    menu_list = main_menu.copy()
    menu_list.append(["Tri One", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    menu_list.append(["Loops", loops_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)
def loops_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, loops_sub_menu)  

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()