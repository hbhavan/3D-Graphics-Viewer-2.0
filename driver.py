from graphics import *
from drawline import *
from matrix import *
import tkinter as tk
import time

rot_x_pos = rotate_x(0.01, 0, 0, 0)
rot_x_neg = rotate_x(-0.01, 0, 0, 0)
rot_y_pos = rotate_y(0.01, 0, 0, 0)
rot_y_neg = rotate_y(-0.01, 0, 0, 0)
rot_z_pos = rotate_z(0.01, 0, 0, 0)
rot_z_neg = rotate_z(-0.01, 0, 0, 0)

trn_x_pos = translate(0.1, 0, 0)
trn_x_neg = translate(-0.1, 0, 0)
trn_y_pos = translate(0, 0.1, 0)
trn_y_neg = translate(0, -0.1, 0)
trn_z_pos = translate(0, 0, 0.1)
trn_z_neg = translate(0, 0, -0.1)

scl_up = scale(0.99, 0.99, 0.99, 0, 0, 0)
scl_dn = scale(1.01, 1.01, 1.01, 0, 0, 0)

identity = translate(0, 0, 0)

transform = {'k': rot_x_pos,
             'i': rot_x_neg,
             'l': rot_y_pos,
             'j': rot_y_neg,
             'o': rot_z_pos,
             'u': rot_z_neg,
             'a': trn_x_pos,
             'd': trn_x_neg,
             'e': trn_y_pos,
             'q': trn_y_neg,
             's': trn_z_pos,
             'w': trn_z_neg,
             'z': scl_up,
             'x': scl_dn,
             '': identity
             }


def read_file(file):
    f = open(file, 'r')
    fl = f.readlines()

    count = 0
    for q in fl:
        line = q.split(' ')
        p = []

        for num in line:
            p.append(float(num))

        set_points(p)
        count += 1

    print('Read', count, ' lines from', file)
    return count


def input_gui():
    master = tk.Tk()

    lbl_rot_x = tk.Label(master, text="Press 'i' or 'k' to rotate about the x axis")
    lbl_rot_x.pack()
    lbl_rot_y = tk.Label(master, text="Press 'l' or 'j' to rotate about the y axis")
    lbl_rot_y.pack()
    lbl_rot_z = tk.Label(master, text="Press 'o' or 'u' to rotate about the z axis")
    lbl_rot_z.pack()
    lbl_trn_x = tk.Label(master, text="Press 'a' or 'd' to translate in the x direction")
    lbl_trn_x.pack()
    lbl_trn_y = tk.Label(master, text="Press 'q' or 'e' to translate in the y direction")
    lbl_trn_y.pack()
    lbl_trn_z = tk.Label(master, text="Press 'w' or 's' to translate in the z direction")
    lbl_trn_z.pack()
    lbl_scl = tk.Label(master, text="Press 'z' or 'x' to scale up or down")
    lbl_scl.pack()
    lbl_esc = tk.Label(master, text="Press '0' to stop the transformation, press '0' again to exit")
    lbl_esc.pack()

    w = 360
    h = 200
    ws = master.winfo_screenwidth()
    x = (ws/2) + 150
    y = 100
    master.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    filename = input("Enter a txt file to read from\n")
    try:
        read_file(filename)
    except FileNotFoundError:
        print("File not found")
        exit()
        
    win = GraphWin('3DViewer', 800, 800, autoflush=False)
    draw(win)
    input_gui()

    while True:
        key = win.getKey()
        if key == '0':
            exit()
        while win.checkKey() != '0':
            if key in transform:
                apply_transformation(win, transform[key])


main()
