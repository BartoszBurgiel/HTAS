import H1
import H2
import P
import UL
import OL
import head

class Assembler:
    def __init__(self, canvas, elements, changes):
        self.canvas = canvas

        self.head_commands = ["<titel>"]

        self.head_tags = [[]]


        # changes = all elements and their attributes seperated
        if not isinstance(changes, str):
            self.changes = changes
            self.chan_ex = True
        else:
            self.changes = 0
            self.chan_ex = False
        
        #strings of tags+values
        self.elements = elements
        
        #list of objects 
        self.objects = []

        # seperate head tags
        index = 0
        for x in range(len(self.elements)-1):
            for y in range(len(self.head_commands)):
                if self.elements[x][0] == self.head_commands[y]:
                    self.head_tags.insert(index, [self.head_commands[y], self.elements[x][1]])
                    index+=1
        
        #number of objects 
        self.count = len(self.elements)-1
        
        for x in range(self.count):
            if self.elements[x][0] == "<ue1>":
                self.objects.append(H1.H1(self.canvas, self.elements[x][1], 0, 0))
            elif self.elements[x][0] == "<ue2>":
                self.objects.append(H2.H2(self.canvas, self.elements[x][1], 0, 0))
            elif self.elements[x][0] == "<a>":
                self.objects.append(P.P(self.canvas, self.elements[x][1], 0, 0))
            elif self.elements[x][0] == "<ul>":
                self.objects.append(UL.UL(self.canvas, self.elements[x][1],0,0))
            elif self.elements[x][0] == "<gl>":
                self.objects.append(OL.OL(self.canvas, self.elements[x][1],0,0))

        self.obj_num = len(self.objects)


        #show all the stuff and run ksb
        if self.chan_ex:
            for x in range(len(self.changes)):
                if self.changes[x].element == "koerper":
                    for i in range(len(self.changes[x].functions)-1):  #go though all attributes 
                        if self.changes[x].functions[i][0] == "hintergrundfarbe":
                            self.change_background_body(self.changes[x].functions[i][1])
                
                # get <a>s done
                if self.changes[x].element == "a":
                    self.scan_element("<a>", x)

                # get ue1 done
                if self.changes[x].element == "ue1":
                    self.scan_element("<ue1>", x)

                # get ue2 done
                if self.changes[x].element == "ue2":
                    self.scan_element("<ue2>", x)
                
                # get uls done
                if self.changes[x].element == "ul":
                    self.scan_element("<ul>", x)

                # get ols done
                if self.changes[x].element == "gl":
                    self.scan_element("<gl>", x)

        # execute head
        if len(self.head_tags) != 0:
            head.Head(self.canvas, self.head_tags, self.objects)

        overallSize=0
        for x in range(self.obj_num):
            if x != 0:
                overallSize+=self.objects[x-1].size
                self.objects[x].y+=15*x+overallSize
            self.objects[x].display()

    def change_background_body(self, col):
        self.canvas.create_rectangle(0,0,500,750, fill=col, outline=col)
    
    def change_font_color(self, col, element):
        element.font_color = col

    def change_font_size(self, size, element):
        sizeN = ""
        for x in range(len(size)-2):
            sizeN+=size[x]
        element.font_size = sizeN
    
    def change_float(self, pos, element):
        if pos == "links":
            element.float_pos = 'nw'
            element.x = 30
            element.justify = 'left'
        elif pos == "mitte":
            element.justify = 'center'
            element.x = 500/2
            if element.type != "<a>":
                element.float_pos = 'center'
            else:
                element.float_pos = 'n'
        elif pos == "rechts":
            element.float_pos = 'ne'
            element.x = 500-30
            element.justify = 'right'

    def change_font_style(self, style, element):
        if style == "italienisch":
            element.style = "italic"
        elif style == "fett":
            element.style = "bold"

    def scan_element(self, element, x):
        #go though all attributes
        for i in range(len(self.changes[x].functions)-1):   
            if self.changes[x].functions[i][0] == "schriftfarbe":
                temp = []
                # pick all elements
                for y in range(len(self.objects)):
                    if self.objects[y].type == element:
                        temp.append(self.objects[y])
                # change every element
                for y in range(len(temp)):
                    self.change_font_color(self.changes[x].functions[i][1], temp[y])
                temp=[]

            # alignment; center left or right
            if self.changes[x].functions[i][0] == "schwebe":
                temp = []
                # pick all elements
                for y in range(len(self.objects)):
                    if self.objects[y].type == element:
                        temp.append(self.objects[y])
                # change every element
                for y in range(len(temp)):
                    self.change_float(self.changes[x].functions[i][1], temp[y])
                temp=[]

            # font-size
            if self.changes[x].functions[i][0] == "schriftgroesse":
                temp = []
                # pick all elements
                for y in range(len(self.objects)):
                    if self.objects[y].type == element:
                        temp.append(self.objects[y])
                # change every element
                for y in range(len(temp)):
                    self.change_font_size(self.changes[x].functions[i][1], temp[y])
                temp=[]

            # font-size
            if self.changes[x].functions[i][0] == "schriftstil":
                temp = []
                # pick all elements
                for y in range(len(self.objects)):
                    if self.objects[y].type == element:
                        temp.append(self.objects[y])
                # change every element
                for y in range(len(temp)):
                    self.change_font_style(self.changes[x].functions[i][1], temp[y])
                temp=[]



