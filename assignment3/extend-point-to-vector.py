import math

# Task 1: Define a class named Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# Task 2: Define a class named Vector that inherits from Point
class Vector(Point):
    def __str__(self):
        # override the __str__ method to make Vector's __str__ different from Point's
        return f"Vector([{self.x}, {self.y}])"

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError("Can only add Vector or Point")
        # override the __add__ method to add two vectors
        return Vector(self.x + other.x, self.y + other.y)


# Task 3: Main program: display all functions
if __name__ == "__main__":
    # test Point
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    print("--- test Point ---")
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p1 equals Point(1, 2)? {p1 == Point(1, 2)}")
    print(f"p1 to p2's distance: {p1.distance_to(p2)}")

    # test Vector
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print("\n--- test Vector ---")
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    
    # test Vector addition (+)
    v3 = v1 + v2
    print(f"v1 + v2 result: {v3} (type: {type(v3).__name__})")