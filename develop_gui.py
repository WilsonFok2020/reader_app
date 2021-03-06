# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello Tkinter')
        
        self.label = tk.Label(self, text='Choose One')
        self.label.pack(fill = tk.BOTH, expand=1, padx=100, pady=30)
        
        hello_button = tk.Button(self, text='Say Hello',
                                 command= self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20,0), pady=(0,20))
        
        goodbye_button = tk.Button(self, text='Say goodbye',
                                   command=self.say_goodbye)
        
        goodbye_button.pack(side=tk.RIGHT, padx=(0,20), pady=(0,20))
        
    def say_hello(self):
        self.label.configure(text = 'Hello World')
    def say_goodbye(self):
        if msgbox.askyesno("close window?", "would you like to close this window?"):
            self.label.configure(text = 'Goodbye ! \n (Closing in 2 seconds)')
            self.after(2000, self.destroy)
        else:
            self.label.configure(text = 'stay open')
            
        
        # # window's title bar, content
        # msgbox.showinfo('Goodbye !', "Goodbye it's been fun") # double quotation undo effect of ' 
        # # script is paused here..... like waiting for user's input = dismiss the message --> continue
        # self.after(2000, self.destroy)
        
        
        
if __name__ == "__main__":
    window = Window()
    window.mainloop()
