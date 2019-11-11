import math


def translate(x, y, z):
    t = Matrix(4, 4)
    t.set(0, 0, 1)
    t.set(1, 1, 1)
    t.set(2, 2, 1)
    t.set(3, 0, x)
    t.set(3, 1, y)
    t.set(3, 2, z)
    t.set(3, 3, 1)

    return t


def basic_scale(x, y, z):
    t = Matrix(4, 4)
    t.set(0, 0, x)
    t.set(1, 1, y)
    t.set(2, 2, z)
    t.set(3, 3, 1)

    return t


def scale(x, y, z, cx, cy, cz):
    a = translate(-cx, -cy, -cz)
    b = basic_scale(x, y, z)
    c = translate(cx, cy, cz)

    t = a.multiply(b).multiply(c)
    return t


def rotate_x(theta, cx, cy, cz):
    a = translate(-cx, -cy, -cz)
    b = translate(cx, cy, cz)
    r = Matrix(4, 4)
    r.set(0, 0, 1)
    r.set(1, 1, math.cos(theta))
    r.set(1, 2, math.sin(theta))
    r.set(2, 1, -math.sin(theta))
    r.set(2, 2, math.cos(theta))
    r.set(3, 3, 1)

    t = a.multiply(r).multiply(b)
    return t


def rotate_y(theta, cx, cy, cz):
    a = translate(-cx, -cy, -cz)
    b = translate(cx, cy, cz)
    r = Matrix(4, 4)
    r.set(0, 0, math.cos(theta))
    r.set(0, 2, math.sin(theta))
    r.set(1, 1, 1)
    r.set(2, 0, -math.sin(theta))
    r.set(2, 2, math.cos(theta))
    r.set(3, 3, 1)

    t = a.multiply(r). multiply(b)
    return t


def rotate_z(theta, cx, cy, cz):
    a = translate(-cx, -cy, -cz)
    b = translate(cx, cy, cz)
    r = Matrix(4, 4)
    r.set(0, 0, math.cos(theta))
    r.set(0, 1, math.sin(theta))
    r.set(1, 0, -math.sin(theta))
    r.set(1, 1, math.cos(theta))
    r.set(2, 2, 1)
    r.set(3, 3, 1)

    t = a.multiply(r).multiply(b)
    return t


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.mat = [0] * rows
        for i in range(rows):
            self.mat[i] = [0] * cols

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def at(self, i, j):
        return self.mat[i][j]

    def set(self, i, j, val):
        self.mat[i][j] = val

    def multiply(self, m):
        x = Matrix(self.rows, m.get_cols())
        for i in range(self.rows):
            for j in range(m.get_cols()):
                result = 0
                for k in range(m.get_rows()):
                    result += (self.mat[i][k] * m.at(k, j))
                    x.set(i, j, result)
        return x

    def print_mat(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.at(i, j), " ", end='')
            print()
