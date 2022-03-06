import tkinter as tk


class App:
    def __init__(self, master, bg_color, vertex_color, active_vertex_color, vertex_radius):
        self.vertex_radius = vertex_radius
        self.vertex_color = vertex_color
        self.active_vertex_color = active_vertex_color
        self.master = master
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{0}x{1}".format(self.width, self.height))
        self.canvas = tk.Canvas(master=master, width=self.width, height=self.height - 100, bg=bg_color)
        self.canvas.pack()
        self.canvas.bind('<Button-3>', self.create_vertex)
        self.vertexes = {}
        self.active = None
        self.button = tk.Button(master=self.master, text='create graph file', command=self.create_file)
        self.button.pack()

    def collision(self, event_x, event_y):
        for i in self.vertexes:
            if event_x in range(self.vertexes[i]['cords'][0] - self.vertex_radius * 2,
                                self.vertexes[i]['cords'][0] + self.vertex_radius * 2) and event_y in range(
                self.vertexes[i]['cords'][1] - self.vertex_radius * 2,
                self.vertexes[i]['cords'][1] + self.vertex_radius * 2):
                return True, i  # collision
        return False, None

    def create_file(self):
        open('graph.txt', 'w').close()
        for i, e in enumerate(self.vertexes):
            string = []
            for k in range(len(self.vertexes)):
                if k + 1 in self.vertexes[e]['neighbors']:
                    string.append('1')
                else:
                    string.append('0')
            with open('graph.txt', 'a') as file:
                file.write(' '.join(string) + '\n')
                file.close()

    def activation(self, event_x, event_y):
        for i in self.vertexes:
            if event_x in range(self.vertexes[i]['cords'][0] - self.vertex_radius,
                                self.vertexes[i]['cords'][0] + self.vertex_radius) and event_y in range(
                self.vertexes[i]['cords'][1] - self.vertex_radius, self.vertexes[i]['cords'][1] + self.vertex_radius):
                return True, i  # collision
        return False, None

    def create_vertex(self, event):
        collision_ = self.collision(event.x, event.y)
        activation_ = self.activation(event.x, event.y)
        if collision_[0] == False:  # make active/unactive
            vertex = self.canvas.create_oval(event.x - self.vertex_radius, event.y - self.vertex_radius,
                                             event.x + self.vertex_radius, event.y + self.vertex_radius,
                                             fill=self.vertex_color)
            self.vertexes[vertex] = {
                'cords': (event.x, event.y), 'isactive': False, 'neighbors': [], 'num': len(self.vertexes) + 1}
            self.canvas.create_text(event.x, event.y, text=len(self.vertexes))
        print(self.vertexes)
        if activation_[0]:
            if self.vertexes[activation_[1]]['isactive']:  # if current vertex is active
                self.vertexes[activation_[1]]['isactive'] = False  # make unactive
                self.canvas.itemconfig(activation_[1], fill=self.vertex_color)
                self.active = None
            else:
                if self.active is not None:
                    line = self.canvas.create_line(self.vertexes[self.active]['cords'][0],
                                                   self.vertexes[self.active]['cords'][1],
                                                   self.vertexes[activation_[1]]['cords'][0],
                                                   self.vertexes[activation_[1]]['cords'][1])
                    self.vertexes[activation_[1]]['neighbors'].append(self.vertexes[self.active]['num'])
                    self.vertexes[self.active]['neighbors'].append(self.vertexes[activation_[1]]['num'])
                    self.canvas.itemconfig(self.active, fill=self.vertex_color)
                    self.canvas.tag_lower(line)
                    self.vertexes[self.active]['isactive'] = False
                    self.active = None
                    return

                self.canvas.itemconfig(activation_[1], fill=self.active_vertex_color)
                self.vertexes[activation_[1]]['isactive'] = True
                self.active = activation_[1]


root = tk.Tk()
app = App(master=root, bg_color='white', vertex_color='red', active_vertex_color='blue', vertex_radius=10)
root.mainloop()
