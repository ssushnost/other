import random as rand
import tkinter as tk
import threading
import time


class Bug:
    def __init__(self):
        self.x = rand.randint(0, 1800)
        self.y = rand.randint(0, 900)
        self.bug = canvas.create_oval(self.x, self.y, self.x + 1, self.y + 1, fill='white', tag='bug')
        self.way = rand.randint(1, 2)
        self.acount = int(((self.x - home_place_x) ** 2 + (self.y - home_place_y) ** 2) ** 0.5)
        self.bcount = int(((self.x - eat_place_x) ** 2 + (self.y - eat_place_y) ** 2) ** 0.5)
        self.pole = canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, tag='pole')
        self.napravlenie = rand.randint(0, 3)
        move_thread = threading.Thread(target=self.moving, args=(()), daemon=True)
        move_thread.start()

    def moving(self):
        while True:
            if not 0 < self.x < 1800 or not 0 < self.y < 900:
                self.napravlenie = abs(self.napravlenie-1)
            if self.napravlenie == 0:
                self.y += 1
                canvas.move(self.bug, 0, 1)
                canvas.move(self.pole, 0, 1)
                self.acount += 1
                self.bcount += 1
                canvas.update()
                time.sleep(0.00001)
            elif self.napravlenie == 1:
                self.x += 1
                canvas.move(self.bug, 1, 0)
                canvas.move(self.pole, 1, 0)
                self.acount += 1
                self.bcount += 1
                canvas.update()
                time.sleep(0.00001)
            elif self.napravlenie == 2:
                self.y -= 1
                canvas.move(self.bug, 0, -1)
                canvas.move(self.pole, 0, -1)
                self.acount += 1
                self.bcount += 1
                canvas.update()
                time.sleep(0.00001)
            elif self.napravlenie == 3:
                self.x -= 1
                canvas.move(self.bug, -1, 0)
                canvas.move(self.pole, -1, 0)
                self.acount += 1
                self.bcount += 1
                canvas.update()
                time.sleep(0.00001)


root = tk.Tk()
root.geometry('1920x1080')
root.resizable(False, False)
root.title('ants')
# x_cords = []
# y_cords = []

canvas = tk.Canvas(root, bg='white')
canvas.place(x=100, y=100, height=900, width=1700)
eat_place = canvas.create_oval(0, 0, 150, 150, fill='blue', tag='eat_place')
eat_place_x = 150
eat_place_y = 150
home_place = canvas.create_oval(1500, 600, 1600, 700, fill='yellow', tag='home_place')
home_place_x = 1500
home_place_y = 600
arr = []
for i in range(100):
    arr.append(Bug())

'''
def check():
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i].acount < arr[j].acount:
                canvas.create_line(arr[i].x, arr[i].y, arr[j].x, arr[j].y, fill='yellow', tag='line')
                canvas.delete('line')


asd = threading.Thread(target=check, args=(()), daemon=True)
asd.start()
'''

root.mainloop()
