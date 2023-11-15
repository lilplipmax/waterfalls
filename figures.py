class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}; {self.y})"

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False


class Segment():
    def __init__(self, point1, point2):
        if point1.y > point2.y:
            self.p_top, self.p_bottom = point1, point2
        else:
            self.p_top, self.p_bottom = point2, point1

    def __str__(self):
        return f"({self.p_bottom.x}; {self.p_bottom.y}) --- ({self.p_top.x}; {self.p_top.y})"

    def in_x(self, point):
        return self.p_top.x <= point.x and point.x <= self.p_bottom.x or \
               self.p_top.x >= point.x and point.x >= self.p_bottom.x

    def get_y(self, point):
        return self.p_top.y - (self.p_top.y - self.p_bottom.y) * (self.p_top.x - point.x) / (
                    self.p_top.x - self.p_bottom.x)


if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(14, 7)
    p = Point(6, 7)
    print(p1)
    print(p1 == p2)
    s = Segment(p1, p2)
    print(s)
    print(s.in_x(p))
    print(s.get_y(p))