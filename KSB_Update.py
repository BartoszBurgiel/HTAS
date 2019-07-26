class KSB_Update:
    def __innit__(self, element, attributes):
        self.element = element
        self.attributes = attributes

    def get_functions(self):
        j = 1
        k = 1
        tempStrA=""
        tempStrV=""
        self.functions = [[]]
        
        for i in range(self.count_semicolons()):
            if i > 0:
                j = k+1
            else: 
                j=0
            while self.attributes[j] != ":":
                tempStrA+=self.attributes[j]
                j+=1
            k=j+2
            while self.attributes[k] != ";":
                tempStrV+=self.attributes[k]
                k+=1
            self.functions.insert(i, [tempStrA, tempStrV])
            tempStrA,tempStrV="",""

    def count_semicolons(self):
        num=0
        for i in range(len(self.attributes)):
            if self.attributes[i] == ";":
                num+=1
        return num
        
#instead of creating 13543 dimentional arrays ill make just an object storing 
#all the needed parameters:
#the element (body, h1, p)
#the attributes (background=red)

