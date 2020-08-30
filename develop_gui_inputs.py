# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello Tkinter')
        
        self.label_text = tk.StringVar()
        self.label_text.set("my name is : ")
        
        # declare variables
        self.label = tk.Label(self, textvar=self.label_text)
        # show the variable python object name
        # self.label = tk.Label(self, text=self.label_text)
        self.label.pack(fill = tk.BOTH, expand=1, padx=100, pady=30)
        
        self.name_text = tk.StringVar()
        self.name_entry = tk.Entry(self, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)
        
        hello_button = tk.Button(self, text='Say Hello',
                                  command= self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20,0), pady=(0,20))
        
        goodbye_button = tk.Button(self, text='Say goodbye',
                                    command=self.say_goodbye)
        
        goodbye_button.pack(side=tk.RIGHT, padx=(0,20), pady=(0,20))
        
    def say_hello(self):
        # self.label.configure(text = 'Hello World')
        message = "hello there" + self.name_entry.get()
        msgbox.showinfo("hello", message)
    def say_goodbye(self):
        if msgbox.askyesno("close window?", "would you like to close this window?"):
            # self.label.configure(text = 'Goodbye ! \n (Closing in 2 seconds)')
            message = 'goodbye ' + self.name_entry.get()
            self.label_text.set(message)
            self.after(2000, self.destroy)
        else:
            # self.label.configure(text = 'stay open')
            msgbox.showinfo('not closing', 'stay open')
            
        
        # # window's title bar, content
        # msgbox.showinfo('Goodbye !', "Goodbye it's been fun") # double quotation undo effect of ' 
        # # script is paused here..... like waiting for user's input = dismiss the message --> continue
        # self.after(2000, self.destroy)
        
        
        
if __name__ == "__main__":
    window = Window()
    window.mainloop()