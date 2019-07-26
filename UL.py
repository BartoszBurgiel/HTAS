class UL:
    def __init__(self, canvas, value, _x, _y):
        self.value = value
        self.canvas = canvas
        self.type = "<ul>"

        self.elements = [] # all elements (for size)
        
        self.li_val = [] # values of all lis

        self.x = _x+30
        self.y = _y+30

        self.font_color = "#000000"

        self.font_size = 12

        self.float_pos = 'nw'

        self.justify = "left"

        self.size = 0

        self.pos_num = 0

    def create_lis(self):
        x=0
        tempVal=""
        while x < len(self.value):
            if self.value[x] != "\n":
                tempVal+=self.value[x]
            #print("bitch")
            x+=1
        x=0
        self.value=tempVal

        tempVal=""
        while x < len(self.value):
            if self.value[x:x+4] == "<li>":
                x+=4
                while self.value[x:x+5] != "</li>":
                    tempVal+=self.value[x] 
                    x+=1
                self.li_val.append(tempVal)
                tempVal=""
            else:
                x+=1

    def display(self):
        self.size = 0
        space=0
        self.create_lis()
        for x in range(len(self.li_val)):
            if self.justify == 'right':
                self.elements.append(self.canvas.create_oval(self.x, self.y+space*x,
                                    self.x+5, self.y+space*x+5, fill=self.font_color))

                self.elements.append(self.canvas.create_text(self.x-15, self.y+space*x-7,
                                    text=self.li_val[x], anchor=self.float_pos, font=("Times", 
                                    self.font_size), fill=self.font_color, justify=self.justify))
            else:
                self.elements.append(self.canvas.create_oval(self.x, self.y+space*x,
                                    self.x+5, self.y+space*x+5, fill=self.font_color))

                self.elements.append(self.canvas.create_text(self.x+15, self.y+space*x-7,
                                    text=self.li_val[x], anchor=self.float_pos, font=("Times", 
                                    self.font_size), fill=self.font_color, justify=self.justify))
            tempSize = self.canvas.bbox(self.elements[x*2+1])
            space = (tempSize[3]-tempSize[1])
            self.size+=space
        self.size-=len(self.li_val)*5