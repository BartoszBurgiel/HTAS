class P:
    def __init__(self, canvas, value, _x, _y):
        self.value = value
        self.canvas = canvas
        self.val_len = len(self.value)
        self.type = "<a>"
        
        self.x = _x+30
        self.y = _y+30

        self.font_color = "#000000"

        self.font_size = 12

        self.float_pos = 'nw'

        self.justify = "left"

        self.style = ""

        self.pos_num = 0

    def display(self):
        self.p = self.canvas.create_text(self.x, self.y, text=self.value, 
        width=400, anchor=self.float_pos, font=("Times", self.font_size, self.style), fill=self.font_color, 
        justify=self.justify)

        self.size = self.canvas.bbox(self.p)
        self.size = self.size[3]-self.size[1]




