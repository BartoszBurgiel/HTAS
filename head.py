class Head:
    def __init__(self, canvas, tags, objects):
        self.canvas = canvas
        self.tags = tags
        self.objects = objects

        for x in range(len(self.tags)-1):
            if self.tags[x][0] == '<titel>':
                for i in range(len(objects)):
                    self.header(self.tags[x][1])
                    self.objects[i].y=+90

    def header(self, titel):
        self.canvas.create_rectangle(0, 0, 520, 50, fill='#c1c1c1', outline="#c1c1c1")
        self.canvas.create_rectangle(10, 50, 200, 20, fill='#ededed', outline="#ededed")
        self.canvas.create_text(20, 35, text=titel, anchor='w', font=("Arial"))
