import tkinter as tk
import math
from random import randint


def arduino_map(val, in_min, in_max, out_min, out_max):
    return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def restart_button():
    global is_left_mouse_button_pressed
    global is_restart_pressed
    is_restart_pressed = True
    root.bind('<Motion>', get_mouse_coordinates)
    is_left_mouse_button_pressed = False
    coord_text.set('x=0, y=0')
    speed_text.set('speed=0')
    start_speed_text.set('start_speed=0')
    canvas.delete('trajectory_line')
    canvas.delete('timer')
    canvas.delete('oval')
    canvas.delete('acceleration_vector')
    canvas.delete('speed_vector')
    canvas.create_oval(x_0_0, y_0_0 - height_scale.get(), x_0_0 + diameter, y_0_0 - height_scale.get() + diameter,
                       width=oval_width, tag='oval')


def movement():
    global is_moving
    if is_left_mouse_button_pressed:
        is_moving = True
        canvas.delete('trajectory_line')
        root.unbind('<Motion>')
        time = time_scale.get()
        x = x_0_0
        y = y_0_0
        g = g_scale.get()
        y_height = y - height_scale.get()
        while True:
            if not 0 <= y <= y_0_0 or not 0 <= x <= 1780 or is_restart_pressed:
                is_moving = False
                break
            x = x_0_0 + start_speed * time * math.cos(math.radians(throw_angle))
            y = y_height + start_speed * -math.sin(math.radians(throw_angle)) * time + g * time ** 2 // 2
            current_speed = start_speed - g * time
            speed_text.set('speed=' + str(abs(current_speed)))
            coord_text.set('x=' + str(round(x - x_0_0)) + ', y=' + str(abs(round(y - y_0_0))))
            canvas.delete('oval')
            canvas.delete('acceleration_vector')
            canvas.delete('speed_vector')
            canvas.create_oval(x, y, x + diameter, y + diameter, width=oval_width, tag='oval')
            canvas.create_line(x + radius, y + radius, x + radius, y + radius + 30, tag='acceleration_vector')
            canvas.create_line(x + radius,
                               y + radius + 30,
                               x + radius - 7,
                               y + radius + 30 - 7,
                               tag='acceleration_vector')
            canvas.create_line(x + radius,
                               y + radius + 30,
                               x + radius + 7,
                               y + radius + 30 - 7,
                               tag='acceleration_vector')
            canvas.create_line(x + radius, y + radius, x + radius + int(float(speed_text.get()[6:])), y + radius,
                               tag='speed_vector')
            canvas.create_line(x + radius + int(float(speed_text.get()[6:])),
                               y + radius,
                               x + radius + int(float(speed_text.get()[6:])) - 7,
                               y + radius - 7,
                               tag='speed_vector')
            canvas.create_line(x + radius + int(float(speed_text.get()[6:])),
                               y + radius,
                               x + radius + int(float(speed_text.get()[6:])) - 7,
                               y + radius + 7,
                               tag='speed_vector')
            time += time_scale.get()
            if round(time) == 0:
                canvas.delete('timer')
                A = canvas.create_line(1600, 20, 1620, 20, width=2, tag='timer')
                B = canvas.create_line(1622, 22, 1622, 42, width=2, tag='timer')
                C = canvas.create_line(1622, 46, 1622, 66, width=2, tag='timer')
                D = canvas.create_line(1620, 68, 1600, 68, width=2, tag='timer')
                E = canvas.create_line(1598, 66, 1598, 46, width=2, tag='timer')
                F = canvas.create_line(1598, 42, 1598, 22, width=2, tag='timer')
            elif round(time) == 1:
                canvas.delete('timer')
                B = canvas.create_line(1622, 22, 1622, 42, width=2, tag='timer')
                C = canvas.create_line(1622, 46, 1622, 66, width=2, tag='timer')
            elif round(time) == 2:
                canvas.delete('timer')
                A = canvas.create_line(1600, 20, 1620, 20, width=2, tag='timer')
                B = canvas.create_line(1622, 22, 1622, 42, width=2, tag='timer')
                D = canvas.create_line(1620, 68, 1600, 68, width=2, tag='timer')
                E = canvas.create_line(1598, 66, 1598, 46, width=2, tag='timer')
                G = canvas.create_line(1600, 44, 1620, 44, width=2, tag='timer')
            elif round(time) == 3:
                canvas.delete('timer')
                A = canvas.create_line(1600, 20, 1620, 20, width=2, tag='timer')
                B = canvas.create_line(1622, 22, 1622, 42, width=2, tag='timer')
                C = canvas.create_line(1622, 46, 1622, 66, width=2, tag='timer')
                D = canvas.create_line(1620, 68, 1600, 68, width=2, tag='timer')
                G = canvas.create_line(1600, 44, 1620, 44, width=2, tag='timer')
            elif round(time) == 4:
                canvas.delete('timer')
                B = canvas.create_line(1622, 22, 1622, 42, width=2, tag='timer')
                C = canvas.create_line(1622, 46, 1622, 66, width=2, tag='timer')
                F = canvas.create_line(1598, 42, 1598, 22, width=2, tag='timer')
                G = canvas.create_line(1600, 44, 1620, 44, width=2, tag='timer')
            elif round(time) == 5:
                canvas.delete('timer')
                A = canvas.create_line(1600, 20, 1620, 20, width=2, tag='timer')
                C = canvas.create_line(1622, 46, 1622, 66, width=2, tag='timer')
                D = canvas.create_line(1620, 68, 1600, 68, width=2, tag='timer')
                F = canvas.create_line(1598, 42, 1598, 22, width=2, tag='timer')
                G = canvas.create_line(1600, 44, 1620, 44, width=2, tag='timer')
            elif round(time) == 6:
                canvas.delete('timer')
                A = canvas.create_line(1600, 20, 1620, 20, width=2, tag='timer')
                C = canvas.create_line(1622, 46, 1622, 66, width=2, tag='timer')
                D = canvas.create_line(1620, 68, 1600, 68, width=2, tag='timer')
                E = canvas.create_line(1598, 66, 1598, 46, width=2, tag='timer')
                F = canvas.create_line(1598, 42, 1598, 22, width=2, tag='timer')
                G = canvas.create_line(1600, 44, 1620, 44, width=2, tag='timer')
            elif round(time) == 7:
                canvas.delete('timer')
                A = canvas.create_line(1600, 20, 1620, 20, width=2, tag='timer')
                B = canvas.create_line(1622, 22, 1622, 42, width=2, tag='timer')
                C = canvas.create_line(1622, 46, 1622, 66, width=2, tag='timer')
            elif round(time) == 8:
                canvas.delete('timer')
                A = canvas.create_line(1600, 20, 1620, 20, width=2, tag='timer')
                B = canvas.create_line(1622, 22, 1622, 42, width=2, tag='timer')
                C = canvas.create_line(1622, 46, 1622, 66, width=2, tag='timer')
                D = canvas.create_line(1620, 68, 1600, 68, width=2, tag='timer')
                E = canvas.create_line(1598, 66, 1598, 46, width=2, tag='timer')
                F = canvas.create_line(1598, 42, 1598, 22, width=2, tag='timer')
                G = canvas.create_line(1600, 44, 1620, 44, width=2, tag='timer')
            elif round(time) == 9:
                canvas.delete('timer')
                A = canvas.create_line(1600, 20, 1620, 20, width=2, tag='timer')
                B = canvas.create_line(1622, 22, 1622, 42, width=2, tag='timer')
                C = canvas.create_line(1622, 46, 1622, 66, width=2, tag='timer')
                F = canvas.create_line(1598, 42, 1598, 22, width=2, tag='timer')
                G = canvas.create_line(1600, 44, 1620, 44, width=2, tag='timer')
            canvas.after(frame_scale.get())
            canvas.update()


def get_mouse_coordinates(event):
    global throw_angle
    global start_speed
    global is_restart_pressed
    is_restart_pressed = False
    A = (y_0_0 - height_scale.get() + radius) - event.y
    B = event.x - (x + radius)
    C = (A ** 2 + B ** 2) ** 0.5
    if not is_left_mouse_button_pressed and B * C != 0 and not is_moving:
        start_speed = arduino_map(C, 0, 1000, 0, 60)
        start_speed_text.set('start_speed=' + str(start_speed))
        throw_angle = math.degrees(math.acos((B ** 2 + C ** 2 - A ** 2) / (2.0 * B * C)))
        canvas.delete('line')
        canvas.create_line((x_0_0 + radius), (y_0_0 - height_scale.get() + radius), event.x, event.y, tag='line')
        canvas.create_line(event.x,
                           event.y,
                           event.x + arrow_line_length * math.sin(
                               math.radians(90 - throw_angle - 135)),
                           event.y - arrow_line_length * math.sin(math.radians(throw_angle + 135)),
                           tag='line')
        canvas.create_line(event.x,
                           event.y,
                           event.x - arrow_line_length * math.sin(
                               math.radians(90 - throw_angle - 45)),
                           event.y + arrow_line_length * math.sin(math.radians(throw_angle + 45)),
                           tag='line')


def left_mouse_button(event):
    if not is_moving:
        global is_left_mouse_button_pressed
        is_left_mouse_button_pressed = True
        time = 0
        x = x_0_0
        trajectory_x = x
        y = y_0_0
        trajectory_y = y - height_scale.get()
        g = g_scale.get()
        y_height = y - height_scale.get()
        while True:
            if not 0 <= y <= y_0_0 or is_restart_pressed:
                break
            x = x_0_0 + start_speed * time * math.cos(math.radians(throw_angle))
            y = y_height + start_speed * -math.sin(math.radians(throw_angle)) * time + g * time ** 2 // 2
            canvas.create_line(trajectory_x + radius, trajectory_y + radius, x + radius, y + radius,
                               tag='trajectory_line', fill='red')
            trajectory_x = x
            trajectory_y = y
            time += 0.05


def set_height():
    if not is_left_mouse_button_pressed:
        canvas.delete('oval')
        canvas.create_oval(x_0_0, y_0_0 - height_scale.get(), x_0_0 + diameter, y_0_0 - height_scale.get() + diameter,
                           tag='oval', width=oval_width)
    else:
        height_scale.set(0)


is_moving = False
x = 5  # текущее положение тела x
y = 775  # текущее положение тела y
y_0_0 = y  # начало координат const y
x_0_0 = x  # начало координат const x
diameter = 20  # диаметер тела
radius = diameter // 2  # радиус тела
is_restart_pressed = False  # был ли нажат пробел(фикс бага)
is_left_mouse_button_pressed = False  # был ли нажат лкм(фикс бага)
arrow_line_length = 25  # длина линий стрелки
oval_width = 2  # толщина тела
root = tk.Tk()
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
root.title('well hello')
top_frame = tk.Frame(master=root, width=1800, height=200)  # верхняя часть с ползунками
bot_frame = tk.Frame(master=root, width=1800, height=800)  # нижняя часть холст
top_frame.pack(fill=tk.X)
bot_frame.pack(side=tk.BOTTOM)
canvas = tk.Canvas(master=bot_frame, width=1800, height=800)
canvas.pack()
canvas.create_rectangle(2, 2, 1801, 800)
tk.Button(master=top_frame, text="start", command=movement).place(x=0, y=0)
tk.Button(master=top_frame, text="restart", command=restart_button).place(x=0, y=30)
tk.Button(master=top_frame, text='exit', command=exit).place(x=0, y=60)
coord_text = tk.StringVar()
coord_text.set('x=0, y=0')
speed_text = tk.StringVar()
speed_text.set('speed=0')
start_speed_text = tk.StringVar()
start_speed_text.set('start_speed=0')
coord_label = tk.Label(master=top_frame, textvariable=coord_text)
coord_label.place(x=50, y=70)
speed_label = tk.Label(master=top_frame, textvariable=speed_text)
speed_label.place(x=50, y=100)
start_speed_label = tk.Label(master=top_frame, textvariable=start_speed_text)
start_speed_label.place(x=50, y=130)
g_scale = tk.Scale(master=top_frame, label='g', from_=0, to=10, orient='h')
g_scale.set(1)
g_scale.place(x=50, y=0)
height_scale = tk.Scale(master=top_frame, label='height', command=lambda event: set_height(), from_=0, to=500,
                        orient='h', length=400)
height_scale.place(x=160, y=0)
frame_scale = tk.Scale(master=top_frame, label='frame', from_=0, to=10,
                       orient='h')
frame_scale.set(1)
frame_scale.place(x=570, y=0)
time_scale = tk.Scale(master=top_frame, label='time', from_=0.01, to=3, orient='h', digits=3, resolution=0.01,
                      length=400)
time_scale.set(0.1)
time_scale.place(x=680, y=0)
throw_angle_line, left_arrow_line, right_arrow_line = \
    canvas.create_line(0, 0, 0, 0), canvas.create_line(0, 0, 0, 0), canvas.create_line(0, 0, 0, 0)  # угловая стрелка
oval = canvas.create_oval(x_0_0, y_0_0, x_0_0 + diameter, y_0_0 + diameter, width=oval_width, tag='oval')
'''A = canvas.create_line(1600, 20, 1620, 20, width=2,tag='timer')
B = canvas.create_line(1622, 22, 1622, 42, width=2,tag='timer')
C = canvas.create_line(1622, 46, 1622, 66, width=2,tag='timer')
D = canvas.create_line(1620, 68, 1600, 68, width=2,tag='timer')
E = canvas.create_line(1598, 66, 1598, 46, width=2,tag='timer')
F = canvas.create_line(1598, 42, 1598, 22, width=2,tag='timer')
G = canvas.create_line(1600, 44, 1620, 44, width=2,tag='timer')'''
root.bind('<S>', lambda event: movement())
root.bind('<s>', lambda event: movement())
root.bind('<Motion>', get_mouse_coordinates)
canvas.bind('<Button-1>', left_mouse_button)
tk.mainloop()
