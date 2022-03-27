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