import tkinter as tk
import random


class Field:
    def __init__(self, master, spot_size, row, col, w, field_color, outline_color, array=[]):
        self.spot_size = spot_size
        self.canvas = tk.Canvas(
            master=master,
            bg='#75bbfd',
            width=col * spot_size + 2,
            height=row * spot_size + 2
        )
        self.canvas.focus_set()
        self.canvas.pack(side=tk.LEFT)
        self.row = row
        self.col = col
        self.w = w
        self.field_color = field_color
        self.outline_color = outline_color
        self.array = array
        self.create_field()

    def create_field(self):
        for r in range(self.row):
            self.array.append([])
            for c in range(self.col):
                self.array[r].append(self.canvas.create_rectangle
                    (
                    2 + c * self.spot_size,
                    2 + r * self.spot_size,
                    2 + c * self.spot_size + self.spot_size,
                    2 + r * self.spot_size + self.spot_size,
                    fill=self.field_color,
                    outline=self.outline_color,
                    width=self.w)
                )


class Snake:
    def __init__(self, field, snake_color, food_color):
        self.root = root
        self.canvas = field.canvas
        self.field = field
        self.snake_color = snake_color
        self.food_color = food_color
        self.score = 0
        self.x_head = random.randint(0, field.col - 1)
        self.y_head = random.randint(0, field.row - 1)
        self.head = field.array[self.y_head][self.x_head]

        self.snake = [self.head]

        self.set_defaults()

    def set_defaults(self):
        self.canvas.bind('<a>', self.moveleft)
        self.canvas.bind('<d>', self.moveright)
        self.canvas.bind('<s>', self.movedown)
        self.canvas.bind('<w>', self.moveup)

        self.field.canvas.itemconfig(self.head, fill=self.snake_color)

        self.craete_food()

    def moveleft(self, event):
        if self.x_head:
            self.delete_tail()
            self.x_head -= 1
            self.update_head()
            self.check_for_lose()
            self.check_food()

    def moveright(self, event):
        if self.x_head < self.field.col - 1:
            self.delete_tail()
            self.x_head += 1
            self.update_head()
            self.check_for_lose()
            self.check_food()

    def movedown(self, event):
        if self.y_head < self.field.row - 1:
            self.delete_tail()
            self.y_head += 1
            self.update_head()
            self.check_for_lose()
            self.check_food()

    def moveup(self, event):
        if self.y_head:
            self.delete_tail()
            self.y_head -= 1
            self.update_head()
            self.check_for_lose()
            self.check_food()

    def check_food(self):
        if self.food == self.head:
            self.score += 1
            print(self.score)
            self.snake.insert(0, 0)
            self.craete_food()
        print(self.snake)

    def check_for_lose(self):
        if self.head in self.snake[:-1]:
            self.root.quit()

    def update_head(self):
        self.head = self.field.array[self.y_head][self.x_head]
        self.snake.append(self.head)
        self.canvas.itemconfig(self.head, fill=self.snake_color)

    def delete_tail(self):
        self.canvas.itemconfig(self.snake[0], fill=self.field.field_color)
        del self.snake[0]

    def craete_food(self):
        self.x_food = random.randint(0, self.field.col - 1)
        self.y_food = random.randint(0, self.field.row - 1)
        self.food = self.field.array[self.y_food][self.x_food]
        for el in self.snake:
            if self.food == el:
                self.craete_food()
        else:
            self.canvas.itemconfig(self.food, fill=self.food_color)


root = tk.Tk()
root.geometry('1500x1000')
f2 = Field(root, 20, 15, 20, 1, 'white', 'black')
s2 = Snake(f2, 'yellow', 'purple')
root.mainloop()
