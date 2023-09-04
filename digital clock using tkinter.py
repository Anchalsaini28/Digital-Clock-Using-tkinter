#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing whole module
from tkinter import *
from tkinter.ttk import *
 
# importing strftime function to
# retrieve system's time
from time import strftime
 
# creating tkinter window
root = Tk()
root.title('Clock')
 
# This function is used to
# display time on the label
def time():
    string = strftime('%I:%M:%S %p')
    digi_clock.config(text = string)
    digi_clock.after(1000, time)
 
# Styling the label widget so that clock
# will look more attractive
digi_clock = Label(root, font = ('calibri', 40, 'bold'),
            background = 'pink',
            foreground = 'white')
 
# Placing clock at the centre
# of the tkinter window
digi_clock.pack(anchor = 'center')
time()
 
mainloop()


# In[ ]:





# In[ ]:




