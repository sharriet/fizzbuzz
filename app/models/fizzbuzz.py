class FizzBuzz:

    def input_number(self, n):
        if n % 5 == 0 and n % 3 == 0:
            return "fizzbuzz"
        elif n % 5 == 0:
            return "buzz"
        elif n % 3 == 0:
            return "fizz"
        else:
            return n