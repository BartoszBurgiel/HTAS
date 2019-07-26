class Table:
    def __innit(self, canvas, value, _x, _y):
        print("hehe")

    def create_cell(self, x, y, sizeX, sizeY, text):
        self.canvas.create_rectangle(x, y, x+sizeX, y+sizeY)
        self.canvas.create_text(x, y, text=text)