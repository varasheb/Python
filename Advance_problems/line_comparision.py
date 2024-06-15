import math

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def length(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
    def __eq__(self, other):
        if not isinstance(other, Line):
            return False
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2





if __name__=="__main__":
    print("Welcome to Line Comparison Computation Program")

    line1 = Line(1, 2, 4, 6)
    line2 = Line(1, 2, 4, 6)
    line3 = Line(1, 2, 5, 5)
    print("Length of the line1:", line1.length())
    print("Length of the line2:", line2.length())
    print("Length of the line3:", line3.length())


    print("Line1 equals Line2:", line1 == line2) 
    print("Line1 equals Line3:", line1 == line3)



