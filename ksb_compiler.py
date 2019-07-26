import KSB_Update

class Compiler:
    def __init__(self, canvas, input):
        self.input = input
        self.canvas = canvas
        
        #all the attributes (background = red)
        self.attributes = []

        #all the mentioned elements 
        self.elements = []

        #stores starts and ends of elements
        posEl = []

        #array of KSB_Updates
        self.changes = []


        #define elements 
        strAttr = ""
        posEl.append(0)
        for x in range(len(self.input)):
            if self.input[x] == '{':
                posEl.append(x-1)
                ind=1
                while self.input[x+ind+1] != '}':
                    if self.input[x+ind] != "\n":
                        if not (self.input[x+ind] == " " and self.input[x+ind+1] == " "):
                            strAttr+=self.input[x+ind]
                    ind+=1
                posEl.append(x+ind+4)
                self.attributes.append(strAttr)
                strAttr=""            

        for x in range(int(len(posEl)/2)):
            bor1=posEl[x*2]
            bor2=posEl[x*2+1]
            self.elements.append(self.input[bor1:bor2])

        for x in range(len(self.elements)):
            self.changes.append(KSB_Update.KSB_Update())
            self.changes[x].element = self.elements[x]
            self.changes[x].attributes = self.attributes[x]
            self.changes[x].get_functions()