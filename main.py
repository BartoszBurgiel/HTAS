from tkinter import *
import htas_compiler
import reference
import os

class main:
    def __init__(self, root):
        # file = open("liesmich.txt", "w+")
        # # file.write("> in der Regel werden alle Dateien im Ordner 'out' gespeichert\n"+
        # #             "> achte darauf, dass die Bilddateien im selben Ordner wie die main.exe Datei\n" +
        # #             "> du kannst gerne eine Verknpfung zur main.exe machen und diese an beliebigen Ort einfgen")
        # file.close()
        self.root = root
        self.root.title("Hypertext-Auszeichnungssprache")
        self.root.configure(background='#F9C1A9')

        self.ksb_state = FALSE

        self.htasImg_small = PhotoImage(file="HTAS_small.png")

        self.canvas_frame = Frame(self.root)

        self.canvas = Canvas(self.canvas_frame, width=500, height=700, bg="#ffffff")

        self.scrollbar = Scrollbar(self.canvas_frame, orient="vertical")
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar)

        self.tem_frame = Frame(self.root)
        self.text = Text(self.tem_frame, width=60, height=40)
        self.text_ksb = Text(self.tem_frame, width=60, height=40)
        self.menubar = Menu(self.root)

        self.submit = Button(self.tem_frame, text="EINREICHEN", width=50, bg="#a9e1f9", fg="#000000", command = lambda : self.get_input(), relief='flat')
        self.example_butt = Button(self.tem_frame, text="BEISPIEL", width=25, bg="#a9e1f9", fg="#000000", command = lambda : self.example(), relief='flat')
        self.example_ksb_butt = Button(self.tem_frame, text="KASKADIERENDER STILBOGEN", width=25, bg="#a9e1f9", fg="#000000", command = lambda : self.example_ksb(), relief='flat')

        self.info = Button(self.tem_frame, text="index.ksb", bg="#a9e1f9", relief='flat')

        self.canvas.create_image(250, 350, image=self.htasImg_small)

        self.tem_frame.configure(background='#F9C1A9')

        self.canvas.grid(row=0, column=0)
        self.scrollbar.grid(row=0, column=1)
        self.canvas_frame.grid(row=0, column=0, padx=15)
        self.tem_frame.grid(row=0, column=1, sticky=N, padx=15, pady=15)
        self.text.grid(row=0, column=0, sticky=N, columnspan=2)

        self.submit.grid(row=2, column=0, pady=5, columnspan=2)
        self.example_butt.grid(row=4, column=0, pady=5)
        self.example_ksb_butt.grid(row=4, column=1, pady=5)

        self.win_width = self.root.winfo_width()
        self.win_height = self.root.winfo_height()

        self.config_menu()
        self.root.config(menu=self.menubar)


    def get_input(self):
        self.canvas.delete('all')
        self.canvas.create_image(250, 350, image=self.htasImg_small)

        self.input = self.text.get("1.0",END)
        comp = htas_compiler.Compiler(self.canvas, self.input, self.text_ksb.get("1.0", END))
        comp.scan()

    def example(self):
        self.canvas.delete('all')
        self.canvas.create_image(250, 350, image=self.htasImg_small)

        string =    ("<!DOCTYPE htas>\n" + 
                    "<htas>\n"+
                    "<kopf>\n"+
                    "<titel>Meine Webseite</titel>\n"+
                    "</kopf>\n<koerper>\n"+
                    "<ue1>Hallo Welt</ue1>\n"+
                    "<ue2>Lorem ipsum dolor</ue2>\n"+
                    "<a>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor "+
                    "invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et"+
                    "justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum"+
                    "dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod "+
                    "tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et"+
                    "accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus"+
                    "est Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam "+
                    "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero "+
                    "eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata "+
                    "sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "+
                    "sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.</a>\n"+
                    "<ul>\n"+
                    "<li>Hallo Welt</li>\n"+
                    "<li>Es ist eine ungeordnete Liste</li>\n"+
                    "</ul>\n"+
                    "<gl>\n"+
                    "<li>Hallo Welt</li>\n"+
                    "<li>Es ist eine geordnete Liste</li>\n"+
                    "</gl>\n"+
                    "</koerper>\n"+
                    "</htas>")

        self.text.delete('1.0', END)
        self.text.insert(END, string)

        self.input = self.text.get("1.0",END)
        comp = htas_compiler.Compiler(self.canvas, self.input, self.text_ksb.get("1.0", END))
        comp.scan()

    def example_ksb(self):
        self.root.state('zoomed')
        self.canvas.delete('all')

        self.info.grid(row=0, column=3, sticky=W, padx=15)
        self.text.grid(row=1, column=0, sticky=N, columnspan=2)
        self.text_ksb.grid(row=1, column=3, sticky=N, padx=15)

        string =    ("<!DOCTYPE htas>\n" + 
                    "<htas>\n"+
                    "<kopf>\n"+
                    "<titel>Meine Webseite</titel>\n"+
                    "<anknuepfen bez='Stilbogen' typ='text/ksb' hbez='index.ksb'>\n"+
                    "</kopf>\n<koerper>\n"+
                    "<ue1>Hallo Welt</ue1>\n"+
                    "<ue2>Lorem ipsum dolor</ue2>\n"+
                    "<a>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor "+
                    "invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et"+
                    "justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum"+
                    "dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod "+
                    "tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et"+
                    "accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus"+
                    "est Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam "+
                    "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero "+
                    "eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata "+
                    "sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "+
                    "sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.</a>\n"+
                    "<ul>\n"+
                    "<li>Hallo Welt</li>\n"+
                    "<li>Es ist eine ungeordnete Liste</li>\n"+
                    "</ul>\n"+
                    "<gl>\n"+
                    "<li>Hallo Welt</li>\n"+
                    "<li>Es ist eine geordnete Liste</li>\n"+
                    "</gl>\n"+
                    "</koerper>\n"+
                    "</htas>")

        self.text.delete('1.0', END)
        self.text.insert(END, string)

        string_ksb =    ("koerper {\n"+
                        "hintergrundfarbe: #a9e1f9;\n"+
                        "}\n\n"+
                        "ue1 {\n"+
                        "schwebe: rechts;\n"+"schriftfarbe: #ff00ff;\n"
                        +"}")

        self.text_ksb.delete("1.0", END)
        self.text_ksb.insert(END, string_ksb)
        
        self.input = self.text.get("1.0",END)
        comp = htas_compiler.Compiler(self.canvas, self.input, self.text_ksb.get("1.0", END))
        comp.scan()

    def config_menu(self):
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Oeffnen", command=lambda:self.open())
        filemenu.add_command(label="Speichern", command=lambda:self.save())
        filemenu.add_command(label="Referenz", command=lambda:self.reference())
        filemenu.add_command(label="Hilfe", command=lambda:self.help())
        filemenu.add_command(label="Einstellungen", command=lambda:self.settings())
        filemenu.add_separator()
        filemenu.add_command(label="Beenden", command =self.root.quit())
        self.menubar.add_cascade(label="Datei", menu=filemenu)

    def reference(self):
        self.ref_window = Toplevel(self.root)
        self.ref_window.title("Hypertext-Auszeichnungssprache - Referenz")

        self.ref_text = Text(self.ref_window)
        self.ref_text.grid()

        reference_str = "balnl"
        self.ref_text.insert(END, reference_str)

    def open(self):
        self.open_interface = Toplevel(self.root)
        self.open_interface.title("Oeffnen...")
        self.open_interface.configure(background="#F9C1A9")

        label_open_interface = Label(self.open_interface, text="Dateipfad eingeben: ", bg="#F9C1A9")
        entry_open_interface = Entry(self.open_interface)
        butt_open_interface = Button(self.open_interface, text="Oeffnen", bg="#a9e1f9", relief='flat', command=lambda:self.open_file(entry_open_interface))

        #logo
        logo_open_interface = Label(self.open_interface, image=self.htasImg_small, bg="#F9C1A9")

        logo_open_interface.grid(row=0, column=0, columnspan=3, sticky=W+E, pady=15)
        label_open_interface.grid(row=1, column=0, pady=15, padx=5)    
        entry_open_interface.grid(row=1, column=1, pady=15, padx=5)    
        butt_open_interface.grid(row=1, column=2, pady=15, padx=5)    

    def open_file(self, entry):
        file_name = entry.get()
        file = open(file_name, "r")
        
        content = file.read()

        self.text.insert(END, content)
        comp = htas_compiler.Compiler(self.canvas, self.text.get("1.0",END), self.text_ksb.get("1.0", END))
        comp.scan()

        file.close()
        self.open_interface.destroy()

    def save(self):
        self.save_interface = Toplevel(self.root)
        self.save_interface.title("Speichern...")
        self.save_interface.configure(background="#F9C1A9")

        label_save_interface = Label(self.save_interface, text="Dateiname eingeben: ", bg="#F9C1A9")
        entry_save_interface = Entry(self.save_interface)
        label_save_interface_end = Label(self.save_interface, text=".htas", bg="#F9C1A9", anchor='w')
        butt_save_interface = Button(self.save_interface, text="Speichern", bg="#a9e1f9", relief='flat', command=lambda:self.save_file(entry_save_interface))

        #logo
        logo_save_interface = Label(self.save_interface, image=self.htasImg_small, bg="#F9C1A9")

        logo_save_interface.grid(row=0, column=0, columnspan=4, sticky=W+E, pady=15)
        label_save_interface.grid(row=1, column=0, pady=15, padx=5)
        entry_save_interface.grid(row=1, column=1, pady=15, padx=5)
        label_save_interface_end.grid(row=1, column=2, pady=15, padx=5)
        butt_save_interface.grid(row=1, column=3, pady=15, padx=5)
  
    def save_file(self, entry):
        if not os.path.exists('out'):
            os.mkdir("out")
        file_name = "out/" + entry.get() + ".htas"
        file = open(file_name, "w+")
        file.write(self.input)
        file.close()
        self.save_interface.destroy()

    def help(self):
        root = Toplevel(self.root)
        root.configure(background="#F9C1A9")
        h1_label = Label(root, text="Anfange", font=("Arial", 20), anchor='nw', justify='left')
        p_label = Label(root, text="> in der Regel werden alle Dateien im Ordner 'out' gespeichert\n"+
                                    "> achte darauf, dass die Bilddateien im selben Ordner wie die main.exe Datei\n" +
                                    "> du kannst gerne eine Verknuepfung zur main.exe machen und diese an beliebigen Ort einfuegen", anchor='nw', justify='left')

        email = Label(root, text="Wenn du einen bug findest, mache ein Screenshot/beschreibe die Stiuation\n und sende es mir ueber E-Mail", anchor='nw', justify='left')
        email_text = Text(root, height=0, width=30)
        email_text.insert(END, "bartek.burgiel@hotmail.com")
        h1_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='W')
        p_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='W')    
        email.grid(row=2, column=0, padx=15, pady=10)        
        email_text.grid(row=2, column=1, padx=15, pady=10)    

    def settings(self):
        root = Toplevel(self.root)
        root.configure(background="#F9C1A9")
        root.title("Einstellungen")  

        dark_button = Button(root, text="Dunkelmodus", bg="#a9e1f9", fg="#000000", relief='flat', command = lambda : self.set_darkmode())
        dark_button.grid(row=0, column=0,pady=15, padx=15)

        light_button = Button(root, text="Hellmodus", bg="#a9e1f9", fg="#000000", relief='flat', command = lambda : self.set_lightmode())
        light_button.grid(row=1, column=0,pady=15, padx=15)

        logo_settings_interface = Label(root, image=self.htasImg_small, bg="#F9C1A9")
        logo_settings_interface.grid(row=0,column=1, rowspan=9, pady=10, padx=10)



    def set_darkmode(self):
        self.root.configure(background="#49242F")
        self.tem_frame.configure(background="#49242F")

        self.text.configure(background="#5b3943")
        self.text_ksb.configure(background="#5b3943")

        self.text.configure(foreground="#bdafb3")
        self.text_ksb.configure(foreground="#bdafb3")

        self.submit.configure(background="#24493e")
        self.submit.configure(foreground="#ffffff")

        self.example_butt.configure(background="#24493e")
        self.example_butt.configure(foreground="#ffffff")

        self.example_ksb_butt.configure(background="#24493e")
        self.example_ksb_butt.configure(foreground="#ffffff")

        self.info.configure(background="#24493e")
        self.info.configure(foreground="#ffffff")

    def set_lightmode(self):
        self.root.configure(background="#F9C1A9")
        self.tem_frame.configure(background="#F9C1A9")

        self.text.configure(background="#ffffff")
        self.text_ksb.configure(background="#ffffff")

        self.text.configure(foreground="#000000")
        self.text_ksb.configure(foreground="#000000")

        self.submit.configure(background="#a9e1f9")
        self.submit.configure(foreground="#000000")

        self.example_butt.configure(background="#a9e1f9")
        self.example_butt.configure(foreground="#000000")

        self.example_ksb_butt.configure(background="#a9e1f9")
        self.example_ksb_butt.configure(foreground="#000000")

        self.info.configure(background="#a9e1f9")
        self.info.configure(foreground="#000000")


root = Tk()
main(root)
root.mainloop()
