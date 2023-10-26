#Dazarus Chapman

import math

class Triangle: 
    def __init__(self, base, height):
        self.set_base(base)
        self.set_height(height)

    def set_base(self, b):
        if b > 0:
            self.base = float(b)

        else:
            print("Base must be greater than 0.")

    def set_height(self, height):
        if height > 0:
            self.height = float(height)
         
        else:
            print("Height must be greater than 0.")

    def calc_side(self):
        side = math.sqrt((self.base/2 ) ** 2 + self.height ** 2)
        return side

    def calc_perimeter(self):
        perimeter = self.base + 2 * self.calc_side()
        return perimeter

    def calc_area(self):
        area = 0.5 * self.base * self.height
        return area

    def calc_alpha(self):
        alpha = math.degrees(math.atan((self.height * 2 ) / self.base))
        return alpha

    def calc_beta(self): #define function as beta
        beta = math.degrees(math.acos(self.height / self.calc_side()) * 2)
        return beta
    
    def print_all(self) -> None:
      print(f"------------------------------")
      print(f"base : {self.base}")
      print(f"height : {self.height}")
      print(f"side : {self.calc_side()}")
      print(f"perimeter: {self.calc_perimeter()}")
      print(f"area : {self.calc_area()}")
      print(f"alpha : {self.calc_alpha()}")
      print(f"beta : {self.calc_beta()}")
      print(f"------------------------------")

x = Triangle(2, 3)
x.print_all()

x.set_height(5)
x.print_all()

x.set_base(2)
x.set_height(3)
x.print_all()
