import math
from typing import List


class Shape:
  """形状类"""

  def __init__(self, name):
    self.name = name


  def perimeter(self):
    raise NotImplementedError("perimeter")
  

  def area(self):
    raise NotImplementedError("area")




class Square(Shape):


  def __init__(self, name, side):
    super().__init__(name)
    
    self.side = side

  
  def perimeter(self):
    return 4 * self.side
  
  
  def area(self):
    return self.side ** 2
  



class Circle(Shape):


  def __init__(self, name, radius):
    super().__init__(name)

    self.radius = radius

  
  def perimeter(self):
    return 2 * math.pi * self.radius
  

  def area(self):
    return math.pi * (self.radius ** 2)




if __name__ == "__main__":
  examples: List[Shape] = [Square("sq", 3), Circle("ci", 2)]
  for thing in examples:
    n = thing.name
    p = thing.perimeter()
    a = thing.area()
    print(f"name: {n}, p: {p:.2f}, n: {a:.2f}")
