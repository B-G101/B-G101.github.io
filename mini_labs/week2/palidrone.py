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
