from tkinter import *


def create_field():
    global square_size
    for i in range(row):
        array.append([])
        for j in range(col):
            array[i].append(
                canvas.create_rectangle(square_size + j * square_size, square_size + i * square_size,
                                        square_size + (j + 1) * square_size,
                                        square_size + (i + 1) * square_size, fill=canvas_color))
            tk.update()
    return array


def click(event):
    global click_count
    global click_coordinates
    if click_count > 1:
        print('воспользуйтесь пкм для очистки')
    else:
        click_count += 1
        click_coordinates.append(event.x)
        click_coordinates.append(event.y)
        print('клик, x =', event.x, 'y =', event.y)
        canvas.itemconfig(array[event.y // square_size - 1][event.x // square_size - 1], fill=line_color)
        if click_count == 2:
            temp = 0
            current_position_x = click_coordinates[0] // square_size - 1
            current_position_y = click_coordinates[1] // square_size - 1
            if click_coordinates[0] // square_size - 1 > click_coordinates[2] // square_size - 1:
                current_position_x = click_coordinates[2] // square_size - 1
                current_position_y = click_coordinates[3] // square_size - 1
                click_coordinates.append(click_coordinates[0])
                click_coordinates.append(click_coordinates[1])
                click_coordinates.pop(0)
                click_coordinates.pop(0)
            if (click_coordinates[1] // square_size - 1) > (click_coordinates[3] // square_size - 1) and\
                    (click_coordinates[0] // square_size - 1) == (click_coordinates[2] // square_size - 1):
                for i in range((click_coordinates[3] // square_size - 1 - click_coordinates[1] // square_size - 1 + 2)
                               * -1):
                    current_position_y -= 1
                    canvas.itemconfig(array[current_position_y][current_position_x], fill=line_color)
            if (click_coordinates[2] // square_size - 1) - (click_coordinates[0] // square_size - 1) == 0:
                error = 0 / 5
                for i in range(click_coordinates[3] // square_size - 1 - click_coordinates[1] // square_size - 1 + 1):
                    current_position_y += 1
                    canvas.itemconfig(array[current_position_y][current_position_x], fill=line_color)
            else:
                error = ((click_coordinates[3] // square_size - 1) - (click_coordinates[1] // square_size - 1)) / (
                    (click_coordinates[2] // square_size - 1) - (click_coordinates[0] // square_size - 1))
            print('error', error)
            if error > 1:
                error = ((click_coordinates[2] // square_size - 1) - (click_coordinates[0] // square_size - 1)) / (
                        (click_coordinates[3] // square_size - 1) - (click_coordinates[1] // square_size - 1))
                print('error fix', error)
                for i in range(click_coordinates[3] // square_size - 1 - click_coordinates[1] // square_size - 1 + 1):
                    temp += error
                    if temp >= 0.5:
                        temp -= 1
                        current_position_x += 1
                        current_position_y += 1
                        canvas.itemconfig(array[current_position_y][current_position_x], fill=line_color)
                    else:
                        current_position_y += 1
                        canvas.itemconfig(array[current_position_y][current_position_x], fill=line_color)
            elif 0 >= error >= - 1:
                for i in range(click_coordinates[2] // square_size - 1 - click_coordinates[0] // square_size - 1 + 1):
                    temp += error
                    if temp <= -0.5:
                        temp += 1
                        current_position_x += 1
                        current_position_y -= 1
                        canvas.itemconfig(array[current_position_y][current_position_x], fill=line_color)
                    else:
                        current_position_x += 1
                        canvas.itemconfig(array[current_position_y][current_position_x], fill=line_color)
            elif 0 < error <= 1:
                for i in range(click_coordinates[2] // square_size - 1 - click_coordinates[0] // square_size - 1 + 1):
                    temp += error
                    if temp >= 0.5:
                        temp -= 1
                        current_position_x += 1
                        current_position_y += 1
                        canvas.itemconfig(array[current_position_y][current_position_x], fill=line_color)
                    else:
                        current_position_x += 1
                        canvas.itemconfig(array[current_position_y][current_position_x], fill=line_color)
            elif error < -1:
                error = ((click_coordinates[2] // square_size - 1) - (click_coordinates[0] // square_size - 1)) / (
                        (click_coordinates[3] // square_size - 1) - (click_coordinates[1] // square_size - 1))
                print('error fix', error)
                for i in range((click_coordinates[3] // square_size - 1 - click_coordinates[1] // square_size - 1 + 2)
                               * -1):
                    temp += error
                    if temp <= -0.5:
                        temp += 1
                        current_position_x += 1
                        current_position_y -= 1
                        canvas.itemconfig(array[current_position_y][current_position_x], fill=line_color)
                    else:
                        current_position_y -= 1
                        canvas.itemconfig(array[current_position_y][current_position_x], fill=line_color)


def clear(event):
    global click_count
    click_count = 0
    click_coordinates.clear()
    array.clear()
    create_field()


print('лкм - 1 точка, лкм - 2 точка, пкм - очистить')

tk = Tk()
tk.title('ДубровскихНикита_Прог_ДЗ_Брезенхем')
tk.resizable(False, False)
array = []
click_coordinates = []
square_size = 20
click_count = 0
row = 25  # пример, работает с любыми значениями
col = 21  # пример, работает с любыми значениями
canvas_color = 'white'
line_color = 'black'
canvas = Canvas(tk, width=(col+2) * square_size, height=(row+2) * square_size)
canvas.pack()

tk.bind("<Button-1>", click)
tk.bind("<Button-3>", clear)

create_field()

tk.mainloop()
