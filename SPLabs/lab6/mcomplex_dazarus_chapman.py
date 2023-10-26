import math

class complex:
    def __init__(self, r: int, i: int):
        """
        Constructor for this complex object
        :param r: A int value representing the real part of this complex object
        :param i: A int value representing the imaginary part of this complex object
        :return: None
        """
        self.r = r
        self.i = i
      

    def print(self):
        """
        Defines the method print for a complex object
        and prints to STDOUT
        :return: None
        """
        print(f"{self.r} + {self.i}i")

    def __add__(self, other) -> complex:
        """
        Defines the behavior of the operator + with two complex objects
        according to the following math operation
            (a + bi) + (c + di) = (a + c) + (b + d)i
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        result = complex(a + c, b + d)
        return result

    def __sub__(self, other) -> complex:
        """
        Defines the behavior of the operator - with two complex objects
        according to the following math operation
            (a + bi) - (c + di) = (a - c) + (b - d)i
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        result = complex(a - c, b - d)
        return result

    def __eq__(self, other) -> bool:
        """
        Defines the behavior of the operator == with two complex objects
        :return: A boolean value comparing the two complex objects
        """
        return self.r == other.r and self.i == other.i

    def __ne__(self, other) -> bool:
        """
        Defines the behavior of the operator != with two complex objects
        :return: A boolean value comparing the two complex objects
        """
        return self.r != other.r or self.i != other.i

    # ========= The functions below need to be defined ==================
    def __mul__(self, other) -> complex:
        """
        Defines the behavior of the operator * with two complex objects
        according to the following math operation
            (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        result = complex((a * c) - (b * d),(a * d) + (b * c))
        return result 

    def __truediv__(self, other) -> complex:
        """
        Defines the behavior of the operator / with two complex objects
        according to the following math operation
            (a + bi) / (c + di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2)
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        result = complex((a * c) + (b * d) / (c^2 + d^2),(b * c) - (a * d) / (c^2 + d^2))
        return result

    def __lt__(self, other) -> bool: # we are looking for a true or false
        # if self is less than other then you return true
        """
        Defines the behavior of the operator < with two complex objects
        according to the following logic operation
            distance of self < distance of other
        :return: A boolean value comparing the euclidean distance between
                 two complex objects
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i
        self.d = math.sqrt((self.r) ** 2 + (self.i) ** 2)
        other.d = math.sqrt((other.r) ** 2 + (other.i) ** 2)
        if self.d < other.d:
            return True
        else:
            return False   
        
        


    def __gt__(self, other) -> bool: # we are looking for a true or false
        # if self is greater than other then you return true
        """
        Defines the behavior of the operator < with two complex objects
        according to the following logic operation
            distance of self > distance of other
        :return: A boolean value comparing the euclidean distance between
                 two complex objects
        """
        
        a = self.r
        b = self.i
        c = other.r
        d = other.i
        self.d = math.sqrt((self.r) ** 2 + (self.i) ** 2)
        other.d = math.sqrt((other.r) ** 2 + (other.i) ** 2)
        if self.d > other.d:
            return True
        else:
            return False
        
    # ===================================================================

def test():
    """
    You can define any test case for complex objects
    """
    x = complex(1, 2)
    y = complex(2, 4)
    z = x * y
    z.print()
    z = x - y
    z.print()
    print(f"X complex is greater than Y complex: {x > y}")
    print(f"X complex is less than Y complex: {x < y}")


if __name__ == "__main__":
    test()
