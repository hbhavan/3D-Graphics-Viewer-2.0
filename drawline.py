from graphics import *
from matrix import *
import math

p_table = []    # List of points
l_table = []    # List of points that make up lines
c = []  # Clipped coordinates
s = []  # Screen coordinates

eye_coordinates = [0, 2, 7.5]
view_distance = 60
screen_size = 30
vsx = 400
vcx = 400
vsy = 400
vcy = 400


def set_point(q):
    p_table.append(q)


def set_line(e):
    l_table.append(e)


def get_cos_y(x, y):
    r = y / math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return r


def get_sin_y(x, y):
    r = x / math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return r


def get_cos_x(x, y, z):
    r1 = math.sqrt(math.pow(x, 2) + math.pow(x, 2))
    r2 = math.sqrt(math.pow(x, 2) +
                   math.pow(y, 2) +
                   math.pow(z, 2))
    return r1 / r2


def get_sin_x(x, y, z):
    r = z / (math.sqrt(math.pow(x, 2) +
                       math.pow(x, 2) +
                       math.pow(z, 2)))
    return r


def view_matrix(xe, ye, ze):
    t1 = translate(-xe, -ye, -ze)

    t2 = Matrix(4, 4)
    t2.set(0, 0, 1)
    t2.set(1, 2, -1)
    t2.set(2, 1, 1)
    t2.set(3, 3, 1)

    t3 = Matrix(4, 4)
    cos_y = get_cos_y(xe, ye)
    sin_y = get_sin_y(xe, ye)
    t3.set(0, 0, -cos_y)
    t3.set(0, 2, sin_y)
    t3.set(1, 1, 1)
    t3.set(2, 0, -sin_y)
    t3.set(2, 2, -cos_y)
    t3.set(3, 3, 1)

    t4 = Matrix(4, 4)
    cos_x = get_cos_x(xe, ye, ze)
    sin_x = get_sin_x(xe, ye, ze)
    t4.set(0, 0, 1)
    t4.set(1, 1, cos_x)
    t4.set(1, 2, sin_x)
    t4.set(2, 1, -sin_x)
    t4.set(2, 2, cos_x)
    t4.set(3, 3, 1)

    t5 = Matrix(4, 4)
    t5.set(0, 0, 1)
    t5.set(1, 1, 1)
    t5.set(2, 2, -1)
    t5.set(3, 3, 1)

    v = t1.multiply(t1).multiply(t2).multiply(t3).multiply(t4).multiply(t5)
    return v


def clip_matrix():
    ds = view_distance / screen_size
    n = basic_scale(ds, ds, 1)
    return n


def get_clipping_coordinates():
    h = view_matrix(eye_coordinates[0],
                    eye_coordinates[1],
                    eye_coordinates[2]
                    ).multiply(clip_matrix())

    a = Matrix(1, 4)
    a.set(0, 3, 1)

    c[:] = []
    for q in p_table:
        a.set(0, 0, q[0])
        a.set(0, 1, q[1])
        a.set(0, 2, q[2])

        b = a.multiply(h)

        c.append([b.at(0, 0),
                  b.at(0, 1),
                  b.at(0, 2)])


def get_screen_coordinates():
    s[:] = []
    for q in c:
        s.append([int(((q[0] / q[2]) * vsx) + vcx),
                  int(((q[1] / q[2]) * vsy) + vcy)])


def clip(x0, y0, x1, y1):

    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0

    if x0 < 0:
        c0 = 1
    if x0 > 800:
        c1 = 2
    if y0 < 0:
        c2 = 4
    if y0 > 800:
        c3 = 8

    cA = c0 + c1 + c2 + c3

    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0

    if x1 < 0:
        c0 = 1
    if x1 > 800:
        c1 = 2
    if y1 < 0:
        c2 = 4
    if y1 > 800:
        c3 = 8

    cB = c0 + c1 + c2 + c3

    res = []
    if (cA | cB) == 0:
        res[0] = x0
        res[1] = y0
        res[2] = y1
        res[3] = y2

        return res

    elif (cA & cB) != 0:
        res[0] = 0
        res[1] = 0
        res[2] = 0
        res[3] = 0

        return res

    else:
        res = clip(x0, y0, 0, 0)
        if res[0] == 0 and \
           res[1] == 0 and \
           res[2] == 0 and \
           res[3] == 0:
            clip(x0, y0, 800, 800)

        return res


def apply_transformation(win, m):
    a = Matrix(1, 4)
    a.set(0, 3, 1)

    for i in range(len(p_table)):
        a.set(0, 0, p_table[i][0])
        a.set(0, 1, p_table[i][1])
        a.set(0, 2, p_table[i][2])

        b = a.multiply(m)

        p_table[i][0] = b.at(0, 0)
        p_table[i][1] = b.at(0, 1)
        p_table[i][2] = b.at(0, 2)

    draw(win)


def render(win, p0, p1):
    x0 = p0[0]
    y0 = p0[1]

    x1 = p1[0]
    y1 = p1[1]

    dX = x1 - x0
    dY = y1 - y0

    if dX == 0:
        if y1 < y0:
            temp = y0
            y0 = y1
            y1 = temp

            dY = y1 - y0

        x = x0
        for i in range(dY):
            y = i + y0
            pt = Point(x, y)
            pt.draw(win)

    elif dY == 0:
        if x1 < x0:
            temp = x0
            x0 = x1
            x1 = temp

            dX = x1 - x0

        y = y0
        for i in range(dX):
            x = i + x0
            pt = Point(x, y)
            pt.draw(win)

    elif abs(dX) >= abs(dY):
        if x1 < x0:
            tempX = x0
            x0 = x1
            x1 = tempX

            tempY = y0
            y0 = y1
            y1 = tempY

            dX = x1 - x0
            dY = y1 - y0

        m = 1
        if dY < 0:
            m = -1
            dY = -dY

        e = 0
        x = x0
        y = y0
        while x < x1:
            pt = Point(x, y)
            pt.draw(win)

            e = e + dY
            if (e << 2) > dX:
                y = y + m
                e = e - dX

            x = x + 1

    elif abs(dX) < abs(dY):
        if y1 < y0:
            tempX = x0
            x0 = x1
            x1 = tempX

            tempY = y0
            y0 = y1
            y1 = tempY

            dX = x1 - x0
            dY = y1 - y0

        m = 1
        if dX < 0:
            m = -1
            dX = -dX

        e = 0
        x = x0
        y = y0
        while y < y1:
            pt = Point(x, y)
            pt.draw(win)

            e = e + dX
            if (e << 2) > dY:
                x = x + m
                e = e - dY

            y = y + 1


def clear(win):
    for item in win.items[:]:
        item.undraw()


def draw(win):
    clear(win)
    get_clipping_coordinates()
    get_screen_coordinates()

    for line in l_table:
        render(win, s[line[0]], s[line[1]])


def print_3d_points():
    for q in p:
        print(q)


def print_clipped_points():
    for q in c:
        print(q)


def print_2d_points():
    for q in s:
        print(q)
