#Sean Rooney
#7/12/2022
#This program creates a GUI and prompts the use to select field which add up values, displaying the total in a pop up message box.






from tkinter import *
from tkinter import messagebox
import tkinter

SERVICES = [('Oil Change', 30.00),                  # Creating a list for the labels and values associated.
            ('Lube Job', 20.00),
            ('Radiator Flush', 40.00),
            ('Transmission Flush', 100.00),
            ('Inspection', 35.00),
            ('Muffler Replacement', 200.00),
            ('Tire Rotation', 20.00)]




class Automotive_add:
    def __init__(self) :                                            #defining a GUI object called Automotive_add
        self.main_window = Tk()
        
        #Creating frames to group widgets
        
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        #Creating int var to use with the Checkbuttons
        self.check_var = [IntVar() for i in range(len(SERVICES))]                               # creating a list of int variables of size len(services) to get to checked condition of each button.
        
        #Set the int var to a default value
        
        
        self.CHECKBOXES = [tkinter.Checkbutton(                                                 # creating a new list to store the checkbuttons
                self.top_frame,
                text='{}-${:.2f}'.format(SERVICES[i][0], SERVICES[i][1]),                       # using the services list to create lables for the buttons
                variable=self.check_var[i])                                                     # assigning the variables for each button to the list of int variables.
            for i in range(len(self.check_var))]                                                
        #creating widgets for mid frame        
        
        
        #pack the buttons
        for i in range (len(self.CHECKBOXES)):                                                  #looping through the list of checkbuttons and packing each button.
            self.CHECKBOXES[i].pack()
            
        # Create an OK button and a Quit button.
        self.charge_button = Button(self.bottom_frame,
                                        text='Display Charges',
                                        command=self.total_charge)
        self.quit_button = Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        # Pack the Buttons.
        self.charge_button.pack(side='left')
        self.quit_button.pack(side='left')
    
        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        #start the main loop
        mainloop()
    
    def total_charge(self):
        total = 0
        for i in range (len(self.CHECKBOXES)):                                              #looping through each checkbutton var to see if the button is press, if true we take the value associated with that button and add it to total.
            if self.check_var[i].get():
                total = total + SERVICES[i][1]
        messagebox.showinfo('Selection', 'Your total charges = ${:.2f}'.format(total))      #print the total to a message box with a formated string to fit the US Dollar.
        
my_gui = Automotive_add()