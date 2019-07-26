class H1: 
    def __init__(self, canvas, value, _x, _y):
        self.value = value
        self.x = _x+30
        self.y = _y+30
        self.canvas = canvas
        self.type = "<ue1>"

        self.size = 30

        self.font_color = "#000000"

        self.float_pos = 'nw'

        self.font_size = 25

        self.justify = "left"

        self.pos_num = 0
    
    def display(self):
        self.widget = self.canvas.create_text(self.x, self.y, text=self.value, font=("Times",self.font_size,"bold"),
        width=300, anchor=self.float_pos, fill=self.font_color, justify=self.justify)
        
        self.size = self.canvas.bbox(self.widget)
        self.size = self.size[3]-self.size[1]
