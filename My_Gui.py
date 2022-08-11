#My Gui.py
#Personalized Time and Date appliaction 
    #Prompts for your name and returns the current time and date
#Nick Garascia - 8/11/22

import time
import PySimpleGUI as sg
sg.theme('DarkTeal')
font = "Helvitica 11"

values = ""

#setup buttons, text, and input as a layout
layout = [[sg.Text("This app will tell you the time and date!")],
          [sg.Text("Please enter your name."), sg.InputText(size = (20), key = '-INPUT-'), sg.Button("Nevermind")],
          [sg.Button("Whats the Time?",), sg.Text("", visible = False, key = '-TIME-')]]

#initalize window with the above layout
window = sg.Window("Time and Date", layout, return_keyboard_events = True, finalize = True)
window['-INPUT-'].bind("<Return>", "_Enter:13")

#read the name input
while True:
    event, values = window.read()
    time_entered = time.asctime()
    if event == sg.WIN_CLOSED or event == "Nevermind" or event == 'Escape:27':
        break
    
    elif event == "Whats the Time?" or event == '-INPUT-' + '_Enter:13':
        #return the name entered and the current time
        print("You entered: ", values['-INPUT-'])
        print("Hello {}, it is currently: {}.".format(values['-INPUT-'], time.asctime()))
        
        if values['-INPUT-'] == '': 
            print("Please enter your name first!")
            window['-TIME-'].Update("Please enter your name first!", font = "Helvitica 11 bold", visible = True, text_color = '#EE0000')
        
        else:
            window['-TIME-'].Update("Hello {}, it is {}".format(values['-INPUT-'], time.asctime()), font = "Helvitica 11", visible = True, text_color = '#fb5b5a')
window.close()