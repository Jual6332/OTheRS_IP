#!/usr/bin/python3
import tkinter as tk
import subprocess
import math
#import tkMessageBox

# Define Constants
SMALL_FONT = "Helvetica 10"
NORMAL_FONT = "Helvetica 12"
LARGE_FONT = "Verdana 18"

# Application Class, Frame object acts as a container for other widgets
class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs) # Initializing Application object
        tk.Tk.wm_title(self,"OTheRS Image Processing Test GUI") # Title
        self.container = tk.Frame(self) # Frame object
        self.container.pack(side="top",fill="both",expand=True) # Set container
        self.container.grid_rowconfigure(0,weight=1) # Define Rows of container
        self.container.grid_columnfigure(0,weight=1) # Define Columns of container
        self.frames = {} # Frame for each pageo
        frame = HomePage

## Individual Pages
# Homepage to start IP, image capture and settings
class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        initialize_class(self,parent,controller)
    def set_page(self,controller):
        label = tk.Label(self, font = LARGE_FONT, text = "OTheRS Image Processing Test GUI\n").grid(row=0,column=1,columnspan=3)
        pad_children(self) # Assign padding to child widgets (aesthetic)

## Global Functions
# Every page object will need initializing, simple function to do so.
# Every page needs the same three objects to initialize: self, parent, controller
# but not every page is built differently. Some pages will require different widgets.
# This is why there is an initialize_class() function but not set_page(). Each
# page for the GUI is "set" differently. Important distinction.
def initialize_class(self,parent,controller):
    tk.Frame.__init__(self,parent)
    self.controller = controller
    self.set_page(controller)

def pad_children(self):
    for child in self.winfo_children(): child.grid_configure(padx=5,pady=5)

def main():
    gui = App() # Instantiate GUI object
    gui.mainloop() # Keep open until user closes

if __name__ == '__main__':
    main()
