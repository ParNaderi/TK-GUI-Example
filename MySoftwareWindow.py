####Note: this is the first version in which menu bar was added to the software from this version
from tkinter import *
from tkinter import ttk
from tkinter import font
import os
import matplotlib.pyplot as plt;plt.rcdefaults()
from math import *
from math import ceil, fabs, atan, degrees, pi,exp,log
import numpy as np
from numpy.linalg import inv
import random
from tkinter.filedialog import askopenfilename
import pandas as pd
import subprocess
import webbrowser
import sys
##
import openpyxl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter import simpledialog
from tkinter import messagebox
import xlsxwriter 
###
import FLife

import matplotlib.pyplot as plt

import math
from subprocess import call
import csv
from csv import reader
from csv import DictReader
import re
from scipy import special
from scipy.integrate import quad
################

def rawInput(myString):
        i = 0
        raw = ''
        while i < len(myString):
            if myString[i] == '\\':
                raw = raw + '/'
            else:
                raw = raw + myString[i]
            i = i + 1
        return raw

class MySoftwareWindow:    
    def __init__(self):               
        self.workDir = rawInput( os.getcwd() )
        print('Directory of the file:',self.workDir)
        self.root = Tk() #Makes the window        
        self.root.frame = Frame(self.root.wm_title("TK GUI Example")) #Makes the title that will appear         
        self.root.menubar = Menu(self.root)
        self.root.filemenu = Menu(self.root.menubar, tearoff=0)
        self.root.filemenu.add_command(label="Open", command=lambda:self.donothing())        
        self.root.filemenu.add_separator()
        self.root.filemenu.add_command(label="Exit", command=lambda:self.close_window())
        self.root.menubar.add_cascade(label="File", menu=self.root.filemenu)
        self.root.runmenu = Menu(self.root.menubar, tearoff=0)
        self.root.runmenu.add_command(label="SubMenu1", command=lambda:self.Window1())
        self.root.runmenu.add_command(label="SubMenu2", command=lambda:self.Window2())        
        self.root.menubar.add_cascade(label="Menu 1", menu=self.root.runmenu)
        ####
        ####
        self.root.helpmenu = Menu(self.root.menubar, tearoff=0)
        self.root.helpmenu.add_command(label="Release Notes", command=lambda:self.release())
        self.root.helpmenu.add_separator()
        self.root.helpmenu.add_command(label="Version 1.0", command=lambda:self.version())
        self.root.helpmenu.add_separator()
        self.root.helpmenu.add_command(label="About GUI...", command=lambda:self.AboutSimp())
        self.root.helpmenu.add_command(label="About Licensing...", command=lambda:self.AboutLic())
        self.root.menubar.add_cascade(label="Help", menu=self.root.helpmenu)
        #######
        self.root.config(menu=self.root.menubar)       
        self.root.p1 = PhotoImage(file = self.workDir+'/icon1.png')       
        self.root.iconphoto(False, self.root.p1)       
        self.root.configure(background="black")
        self.photol = PhotoImage(file = self.workDir+'/mainlogo.gif')
        Label (self.root, image=self.photol, bg="black") .grid(row=0,column=0,sticky=N)
        Label(self.root, text="\n TK GUI Example \n"
              ,bg="black",fg="white",font="none 12 bold") .grid(row=1, column=0, sticky=N)      
       
# ###########################################################
        
    #####
    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI
    ###########
    def AboutSimp(self):       
       messagebox.showinfo("About GUI", " This is just a demo example of TK GUI Toolkit and just for educational purpose. ")      
    ###########
    def AboutLic(self):
       messagebox.showinfo("Licensing", "------------.") 
    #####
    def close_window(self):
         if messagebox.askokcancel("Quit", "Do you want to quit?"):
             self.root.destroy()     
    #####
    def donothing(self):
       print("This button will be activated later.")   
       #####   
    def Window2(self):        
        self.frame = Toplevel(self.root) 
        self.root.check2 ="True"      
      ################
        self.frame1=LabelFrame(self.frame,text="Sub Window2",fg="green")
        self.frame1.grid(row=0,column=0,padx=100,sticky=W)
        ##
        Label(self.frame1, text="Select model:").grid(row=1,column=0,sticky=W)
        self.scm=StringVar()
        self.data1 = ttk.Combobox(self.frame1,width=18,textvariable =self.scm)
        self.data1['values']=("Model1","Model2")
        self.data1.current(0)        
        self.data1.grid(row=1,column=1)
        ##
        #########################
        self.frame.iconbitmap(self.workDir+'/icon1.ico')
        #########################
        self.frame.iconbitmap(self.workDir+'/icon1.ico')
        self.Btn =Button(self.frame, text="OK",width=6, command=lambda:self.close_subwindow2()).grid(row=20, column=0, padx=100, sticky=W)   
    ######
    def Window1(self):        
        self.frame = Toplevel(self.root)         
        ##########
        self.frame1=LabelFrame(self.frame,text=" Sub Window1 ",fg="red")
        self.frame1.grid(row=0,column=0,padx=100,sticky=W)
        ##########        
        Label(self.frame1, text="exponent:").grid(row=1,column=0, sticky=W)
        self.b0=DoubleVar()       
        self.data1 = Entry(self.frame1,text=self.b0)      
        self.b0.set(0.5)
        self.data1.grid(row=1,column=1, sticky=W)        
        #########################
        self.frame.iconbitmap(self.workDir+'/icon1.ico')             
        self.Btn =Button(self.frame, text="OK",width=6, command=lambda:self.close_subwindow()).grid(row=20, column=0,padx=100, sticky=W)        
        #####  
    def show_entry_fields(self):
       print(self.data1.get())   
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
    def close_subwindow(self):            
            self.frame.destroy()                    
   ####
    def close_subwindow2(self):
            self.frame.destroy()
   ####
    def version(self):       
        messagebox.showinfo("Version Notification", "This is Version 0")   
     #####
    def release(self):        
        messagebox.showinfo("Release Note", "Just a demo example---.")      
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
   

