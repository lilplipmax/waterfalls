from tk_drawer import TkDrawer
from figures import Point, Segment


class Waterfalls():
    def __init__(self, segments, points):
        self.segments = segments
        self.points = points

    def __str__(self):
        pass

    def run(self):
        for p in self.points:
            _p = p
            while _p.y > 0:
                print(f"Точка: {_p}")
                _segment = None
                y_max = 0

                # отсеиваем лишние отрезки и находим ближайший
                for s in self.segments:
                    if s.in_x(_p):
                        # y-координата точки падения воды
                        ys = s.get_y(_p)
                        if _p.y > ys and ys > y_max:
                            _segment = s
                            y_max = ys

                if _segment != None:
                    p_tmp = Point(_p.x, y_max)
                    tk.draw_line(_p, p_tmp, "green")
                    _p = _segment.p_bottom
                    tk.draw_line(_p, p_tmp, "green")
                else:
                    tk.draw_line(_p, Point(_p.x, 0), "green")
                    _p = Point(_p.x, 0)
                print(f"Отрезок: {_segment}")
            print(f"Координата точки приземления: {_p.x}\n")


tk = TkDrawer()
tk.clean()

points = []
segments = []
for i in range(int(input())):
    px, py, qx, qy = map(int, input().split())
    p = Point(px, py)
    q = Point(qx, qy)
    s = Segment(p, q)
    segments.append(s)
    tk.draw_line(p, q, "red")
for s in segments:
    print(s)

for i in range(int(input())):
    px, py = map(int, input().split())
    p = Point(px, py)
    points.append(p)
    tk.draw_point(p)

for p in points:
    print(p)

print("run ...")
w = Waterfalls(segments, points)
w.run()
tk.root.mainloop()