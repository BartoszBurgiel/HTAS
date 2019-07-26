import assembler
import ksb_compiler


class Compiler:
    def __init__(self, canvas, input, input_ksb):
        self.input = input
        self.input_ksb = input_ksb
        self.canvas = canvas

        self.commands = ["<ue1>", "<ue2>","<a>", "<titel>", "<ul>", "<gl>", "<tabelle>"]

    def scan(self):
        #seperate tags from value
        self.tags = []

        self.values = []
        self.posValues = [[]]  #where a value starts and ends
        self.elements = [[]] #tags + values

        self.UL_values = []  # all of the values of all ULs
        self.OL_values = []  # all of the values of all OLs
        self.TAB_values = [] # all of the values of all tables

        iter = 0       
        self.x_scan_index=0
        while self.x_scan_index < len(self.input):
            cnt = 0
            # get mulitdimentional tags
            if self.input[self.x_scan_index:self.x_scan_index+4] == "<ul>":
                self.scan_multidim_elements("<ul>", "</ul>")
            elif self.input[self.x_scan_index:self.x_scan_index+4] == "<gl>":
                self.scan_multidim_elements("<gl>", "</gl>")
            elif self.input[self.x_scan_index:self.x_scan_index+9] == "<tabelle>":
                self.scan_multidim_elements("<tabelle>", "</tabelle>")
            #get normal tags
            elif self.input[self.x_scan_index] == '<':
                strTag = ""
                while self.input[self.x_scan_index+cnt-1] != '>':
                    strTag+=self.input[self.x_scan_index+cnt]
                    cnt+=1
                self.tags.append(strTag)
                self.posValues.insert(iter, [self.x_scan_index, self.x_scan_index+cnt])
                iter+=1
            self.x_scan_index+=1
        self.x_scan_index=0

        print(self.tags)

        for x in range(len(self.posValues)-2):
            bor1 = self.posValues[x][1]
            bor2 = self.posValues[x+1][0]
            
            # get the end of the last and the beginning of the next
            if self.input[bor1:bor2] != "\n":
                self.values.append(self.input[bor1:bor2])
        
        index=0
        temp_ul_count = 0  #count of the values assigned to element of ul
        temp_ol_count = 0  #count of the values assigned to element of ol
        # division to body and head 

        for x in range(len(self.tags)-1):
            for y in range(len(self.commands)):
                if self.tags[x] == self.commands[y]:
                    if self.tags[x] == "<ul>":
                        self.elements.insert(index, [self.tags[x], self.UL_values[temp_ul_count]])
                        temp_ul_count+=1
                        index+=1
                    elif self.tags[x] == "<gl>":
                        self.elements.insert(index, [self.tags[x], self.OL_values[temp_ol_count]])
                        temp_ol_count+=1
                        index+=1
                    else:
                        self.elements.insert(index, [self.tags[x], self.values[index]])
                        index+=1

        # precheck if code is valid and run

        if len(self.tags) <=2: 
            self.check_code()
        elif self.tags[0]!= "<!DOCTYPE htas>" or self.tags[1] != "<htas>" or self.tags[len(self.tags)-2] != "</koerper>" or self.tags[len(self.tags)-1] != "</htas>" or not "<koerper>" in self.tags:
            self.check_code()
        elif "<titel>" in self.tags:
            if "</kopf>" in self.tags and "<kopf>" in self.tags:
                if "<anknuepfen bez='Stilbogen' typ='text/ksb' hbez='index.ksb'>" in self.tags:
                    htas = ksb_compiler.Compiler(self.canvas, self.input_ksb)
                    assembler.Assembler(self.canvas, self.elements, htas.changes)
                else:
                    assembler.Assembler(self.canvas, self.elements, self.input_ksb)
            else:
                self.check_code()
        else:
            assembler.Assembler(self.canvas, self.elements, self.input_ksb)

    def check_code(self):
        self.canvas.create_text(250, 350, text="!Überprüfe deine Kodierung!", font=(50), fill="#ff0000")

    def scan_multidim_elements(self, element, close_element):
        # to clean up the input
        temp = ""
        temptemp = ""
        k=0
        temp_k=0
        self.tags.append(element)
        while self.input[self.x_scan_index+k:self.x_scan_index+k+len(close_element)] != close_element:
            temp+=self.input[self.x_scan_index+k]
            k+=1
        while temp_k < len(temp):
            temptemp+=temp[temp_k]
            temp_k+=1
        temp = temptemp
        self.x_scan_index+=k
        if element == "<ul>":
            self.UL_values.append(temp)
        elif element == "<gl>":
            self.OL_values.append(temp)
        elif element == "<tabelle>":
            self.TAB_values.append(temp)