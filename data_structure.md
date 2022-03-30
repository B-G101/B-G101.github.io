{% include navigation.html %}

### Replit

<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="600px" src="https://replit.com/@BG101/B-G101githubio-1?lite=true#main.py"></iframe>
</div>


### Code Snippets

Fibonacci with Classes
```python
class Fibonacci:
    def __init__(self):
        self.fiboSeq = [0, 1]
      
    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2) # two recursive calls to self (__call__(self, n))
            self.fiboSeq.append(fib_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.fiboSeq[n]
      
fibo_of = Fibonacci() # object instantiation and run __init__ method
      

def tester():
    # Make a fibonacci object
    while True:
        fibo_of = Fibonacci()
        n = input("Enter the number of terms: ")
        try:
            n = int(n)
            # Validate the value of n
            #The isinstance() function in Python returns true or false if a variable matches a
            # specified data type. isinstance(variable_to_check, data_type)
            if not (isinstance(n, int) and n >= 0):
                raise ValueError
            print("{0}th term  of Fibonacci sequence is: ".format(n))
            print(fibo_of(n-1)) # print the nth term
            print("Fibonacci sequence of {0} terms is: ".format(n))
            print([fibo_of(i) for i in range(0,n)])
            break
        except:
            print(f'Positive integer number expected, got "{n}" Try again.')

if __name__ == "__main__":
    tester()
```
Factorial
```python
class Factorial:
    def __init__(self):
        self.factSeq = [1, 1]
      
    def __call__(self, n):
        if n < len(self.factSeq):
            return self.factSeq[n]
        else:
            # Compute the requested Factorial number
            fact_number = n * self(n - 1) # two recursive calls to self (__call__(self, n))
            self.factSeq.append(fact_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.factSeq[n]
      
facto_of = Factorial() # object instantiation and run __init__ method
 

def tester():
    # Make a factonacci object
    while True:
        facto_of = Factorial()
        n = input("Enter the number that you want the factorial of: ")
        try:
            n = int(n)
            # Validate the value of n
            #The isinstance() function in Python returns true or false if a variable matches a
            # specified data type. isinstance(variable_to_check, data_type)
            if not (isinstance(n, int) and n >= 0):
                raise ValueError
            print("{0}! is: ".format(n))
            print(facto_of(n)) # print the nth term
            print("Factorial sequence of 0 to the number {0} is: ".format(n))
            print([facto_of(i) for i in range(0,n+1)])
            break
        except:
            print(f'Positive integer number expected, got "{n}" Try again.')

if __name__ == "__main__":
    tester()
```
Factors (Math Function)
```python

def factors(n):
    factors = []
    x = range(1, n + 1)
    for i in x:
        if (n % i == 0):
            factors.append(i)
            print(i, end=' ')
          
    print(factors)


class Factors:
    def __init__(self):
        self.factors = []
      
    def __call__(self, n):
      for i in range(1, n + 1):
        if n % i == 0:
            self.factors.append(i)
      return self.factors
      
factors_of = Factors() # object instantiation and run __init__ method



def tester():
  factors(89)
  factors(66)
  try:
    n = int(input("Pick a Number to Get the Factors of "))
    if not (isinstance(n, int) and n >= 0):
      raise ValueError
    print("Factors of {0} is: ".format(n))
    print(factors_of(n)) # print the nth term
  except:
    print(f'Positive integer number expected, got "{n}" Try again.')

if __name__ == "__main__":
    tester()
```
Palindrome
```python
class Palindrome:
    def __call__(self, j):
        # Remove special characters from a string
        n = ''.join(filter(str.isalnum, j))
        n = n.lower()
        revn = n[::-1]
        if revn == n:
            self.result = (j + " is a palidrome.")
        else:
            self.result = (j + " is not a palidrome.")

        return self.result

palidrome_of = Palindrome()  # object instantiation and run __init__ method



def palidrone(j):
    # Remove special characters from a string and changes all letters to lowercase
    n = ''.join(filter(str.isalnum, j))
    n = n.lower()
    # reverses the string
    revn = n[::-1]
    # checks if the string is the same as the reversed string
    if revn == n:
        print(j + " is a palidrome.")
    else:
        print(j + " is not a palidrome.")


def tester():
    palidrone("jerry")
    palidrone("ava")
    palidrone("racecar")
    palidrone("A man, a plan, a canal -- Panama!")
    print("Pick a number to check whether or not it is a Palidrome")
    j = input()
    print(palidrome_of(j))  # print the nth term


if __name__ == "__main__":
    tester()

```

InfoDB List
```python
InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Bria",
    "LastName": "Gilliam",
    "DOB": "September 27",
    "Birth Place": "Los Angeles",
    "Email": "briagee101@gmail.com",
    "FavoriteColors": ["Blue", "Sage Green", "Lilac" , "Amber" , "Bronze"]
})


InfoDb.append({
    "FirstName": "Allison",
    "LastName": "Huang",
    "DOB": "July 27",
    "Birth Place": "Irvine",
    "Email": "allisonhuang@gmail.com",
    "FavoriteColors": ["Blue", "Green", "Hot Pink", "Blurple", "Lavender"]
})


InfoDb.append({
    "FirstName": "Paige",
    "LastName": "McCartin",
    "DOB": "April 30",
    "Birth Place": "San Diego",
    "Email": "paigey@gmail.com",
    "FavoriteColors": ["Purple", "Red", "White", "Yellow", "Torquise"]
})

InfoDb.append({
    "FirstName": "Karis",
    "LastName": "Gilliam",
    "DOB": "June 1",
    "Birth Place": "Los Angeles",
    "Email": "kg202@gmail.com",
    "FavoriteColors": ["Brown", "Black", "White", "Cyan", "Magenta"]
})

InfoDb.append({
    "FirstName": "Riya",
    "LastName": "Anand",
    "DOB": "Feburary 21",
    "Birth Place": "San Diego",
    "Email": "riyanand@gmail.com",
    "FavoriteColors": ["Brown", "Black", "White", "Cyan", "Magenta"]
})

InfoDb.append({
    "FirstName": "Kevin",
    "LastName": "Chen",
    "DOB": "Feburary 25",
    "Birth Place": "San Diego",
    "Email": "kc4922@gmail.com",
    "FavoriteColors": ["Blue", "purple", "red", "sky blue", "green"]
})

```

For, While, and Recursive Loop
```python
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)


## hack 2b: def while_loop(0)
# while loop contains an initial n and an index incrementing statement (n += 1)

def while_loopt():
  while_loop(0)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    #for n in range(len(InfoDb)):
    #    print_data(n)
    #j = int(n)
    #print(j)

    #while j < len(InfoDb):
    #    print_data(j)
    #    j += 1
    #return


## hack 2c : def recursive_loop(0)
# recursion simulates loop incrementing on each call (n + 1) until exit condition is met

def recursive_loopt():
  recursive_loop(0)

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return  # exit condition

```

Fibonacci Function
```python
def recursive_fibonacci(n):
  # if the value is equal to or less than 1 the fibonacci sequence will automatically be 1
    if n <= 1:
        return n
    else:
  # adds the initial value to the total from before     
        return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))


def fibonacci():
    try:
        nterms = int(input('Input a number:'))
        if nterms <= 0:
            print("Plese enter a positive integer")
        else:
            print("Fibonacci Sequence: ")
          # looping through the function for nterms amount of times
            for i in range(nterms):
                print(recursive_fibonacci(i))
    except ValueError:
        # not a number error
        print(f"Not a number")
```

Menu and Patterns Submenu
```python 
main_menu = [
    ["Animation", menu.ship],
    ["Christmas Tree", menu.christmasTree],
    ["Factorial", menu.for_loop],
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


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Tri One", submenu])
    menu_list.append(["Patterns", patterns_submenu])
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
```

Matrix Print
```python
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
```

Animation
```python
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
```

Swap Function
```python
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
```

Hard coded Christmas Tree Animation
```python
Blue = "\033[94m"
Pink = "\033[91m"
BrightPink = "\033[95m"
Blue2 = '\033[96m'
Red = "\33[31m"
Yellow = "\33[33m"
Purple = "\33[35m"
Color = [Blue, Pink, BrightPink, Blue2, Red, Purple]


def christmasTree():
    print("\33[33m           * \033[92m")
    time.sleep(.5)
    print("\033[92m          * *")
    time.sleep(.5)
    print("         * " + random.choice(Color) + "*\033[92m *")
    time.sleep(.5)
    print("        " + random.choice(Color) + "*\033[92m * " +
          random.choice(Color) + "*\033[92m *")
    time.sleep(.5)
    print("       * " + random.choice(Color) + "*\033[92m * * " +
          random.choice(Color) + "*\033[92m")
    time.sleep(.5)
    print("      * " + random.choice(Color) + "*\033[92m * * " +
          random.choice(Color) + "*\033[92m *")
    time.sleep(.5)
    print("     * * " + random.choice(Color) + "*\033[92m * * * " +
          random.choice(Color) + "*\033[92m")
    time.sleep(.5)
    print("    * " + random.choice(Color) + "*\033[92m * * * " +
          random.choice(Color) + "*\033[92m * " + random.choice(Color) +
          "*\033[92m")
    time.sleep(.5)
    print("   * * " + random.choice(Color) + "*\033[92m * * " +
          random.choice(Color) + "*\033[92m * * " + random.choice(Color) +
          "*\033[92m")
    time.sleep(.5)
    print("  * * " + random.choice(Color) + "*\033[92m * * " +
          random.choice(Color) + "*\033[92m * * " + random.choice(Color) +
          "*\033[92m *")
    time.sleep(.5)
    print(" * " + random.choice(Color) + "*\033[92m * " +
          random.choice(Color) + "*\033[92m * * * " + random.choice(Color) +
          "*\033[92m * " + random.choice(Color) + "*\033[92m * \033[93m")
    time.sleep(.5)
    print("         * * *")
    time.sleep(.5)
    print("         * * * \u001b[37m")
```

[Replit](https://replit.com/@BG101/B-G101githubio-1?v=1)
