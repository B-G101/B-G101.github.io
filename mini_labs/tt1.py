# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with FavoriteColors

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


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"],
          InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Favorite Colors: ",
          end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(
        InfoDb[n]
        ["FavoriteColors"]))  # join allows printing a string list with separator
    print()


# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
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


# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n - 1)


def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion


# for loop iterates on length of InfoDb


def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))


def fibonacci():
    try:
        nterms = int(input('Input a number:'))
        if nterms <= 0:
            print("Plese enter a positive integer")
        else:
            print("Your saucy sequence:")
            for i in range(nterms):
                print(recursive_fibonacci(i))
    except ValueError:
        # not a number error
        print(f"Not a number")


if __name__ == '__main__':
    # print_menu1()
    fibonacci()
