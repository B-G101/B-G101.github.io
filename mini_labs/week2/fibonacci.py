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