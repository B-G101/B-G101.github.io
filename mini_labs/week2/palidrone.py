class Palindrome:
    def __call__(self, j):
        # Remove special characters from a string
        n = ''.join(filter(str.isalnum, j))
        n = n.lower()
        revn = n[::-1]
        if revn == n:
            print(j + " is a palidrome.")
        else:
            print(j + " is not a palidrome.")


palidrome_of = Palindrome()  # object instantiation and run __init__ method
print(palidrome_of("hgj"))  # object running __call__ method


def palidrone(j):
    # Remove special characters from a string
    n = ''.join(filter(str.isalnum, j))
    n = n.lower()
    revn = n[::-1]
    if revn == n:
        print(j + " is a palidrome.")
    else:
        print(j + " is not a palidrome.")


def tester():
    palidrone("jerry")
    palidrone("ava")
    palidrone("racecar")
    palidrone("A man, a plan, a canal -- Panama!")
    j = input()
    print(palidrome_of(j))  # print the nth term


if __name__ == "__main__":
    tester()
