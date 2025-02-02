class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("The denominator cannot be 0.")

        if isinstance(numerator,float) or isinstance(denominator,float):
            raise TypeError("Invalid input. Please input integers or a fraction string.")
        
        if isinstance(numerator,str) and denominator == 1:
            fraction_string = numerator.strip()

            if '/' in fraction_string:
                try:
                    fraction_string = fraction_string.split('/')
                    num, denom = fraction_string[0], fraction_string[1]

                    if denom == 0:
                        raise ZeroDivisionError("The denominator cannot be 0.")
                        
                    self.numerator, self.denominator = num, denom
                
                except ValueError:
                    raise ValueError("Invalid fraction string format.")

        elif isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator
            
        else:
            raise TypeError("Invalid input. Please input integers or a fraction string.")

    def gcd(a, b):
        """
        Return the Greatest Common Divisor (GCD) of two integers.
        If one or both of them is 0, then it returns 0.
        """
        if a == 0 or b == 0:
            return 0

        while b:
            a, b = b, a % b  # Apply Euclidean algorithm

        return abs(a)  # Ensure non-negative output

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        #TODO Attribute error need to debug
        if self.denominator == 1:
            return self.numerator
        
        if self.numerator % self.denominator == 0:
            return self.numerator // self.denominator
        else :
            return str(self.numerator) + "/" + str(self.denominator)
        


