from tkinter import *
import pymem
import re
import os
import webbrowser
from itertools import cycle
import threading
import time
import sys
import subprocess
import requests
import time
import sys
import os
import time
######################################################################################################################
# HWID "Hardware id lock"    This portion of the code locks the user out of the program if they dont have the right HWID.

# There HWID can be put into the pastebin below and will then work

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://pastebin.com/cxU0VUsm")


def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.11)


def Main_Program():
    if hwid in r.text:
        print("---------------------------")
        printSlow("Access granted")
        print("\n")
        print("---------------------------")
        print("\nHWID: " + hwid)
        print("\n")
        print("---------------------------")
        print("\n")
        time.sleep(.02)
    else:
        print("Error! HWID Not In Database!")
        print("Please contact https://discord.gg/Z9MxmBmKDP for help. HWID: " + hwid)
        os.system('pause >NUL')


if __name__ == "__main__":
    Main_Program()
######################################################################################################################
#Login panel
def anything(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


anything("Welcome to sleepy's hacks \n")
print("---------Welcome---------")
username = input("Username:")
if username == "sleepy" :
    print ("________________________")
    print("\n")
else :
    print ("please try another user name. This user name is incorrect")


password = input ("Password:")
if password  == "1234" :
    print ("ACCESS  GRANTED")
    print ("Welcome User ")
    #continue for thins like opening webpages or hidden files for access

else :
      print("Username or Password is incorrect")
      time.sleep(5)   # Delays for 5 seconds. You can also use a float value.
      exit()

######################################################################################################################
#Injection

print("Injecting Sleepy's hacks")

def updt(total, progress):
    """
    Displays or updates a console progress bar.

    Original source: https://stackoverflow.com/a/15860757/1391441
    """
    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()

runs = 400
for run_num in range(runs):
    time.sleep(0.01)
    updt(runs, run_num + 1)

print("Sleepy's Hacks have been injected")

import time
time.sleep(5)   # Delays for 5 seconds. You can also use a float value.
######################################################################################################################
#Banner
print("""
        ~+

                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .


 ______     __         ______     ______     ______   __  __    _    ______     __  __     ______     ______     __  __     ______    
/\  ___\   /\ \       /\  ___\   /\  ___\   /\  == \ /\ \_\ \  /_/\ /\  ___\   /\ \_\ \   /\  __ \   /\  ___\   /\ \/ /    /\  ___\   
\ \___  \  \ \ \____  \ \  __\   \ \  __\   \ \  _-/ \ \____ \ \_\/ \ \___  \  \ \  __ \  \ \  __ \  \ \ \____  \ \  _"-.  \ \___  \  
 \/\_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\    \/\_____\      \/\_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \/\_____\ 
  \/_____/   \/_____/   \/_____/   \/_____/   \/_/     \/_____/       \/_____/   \/_/\/_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/ 
     (FREE CSGO HACKS JOIN MY DISCORD)
""")

######################################################################################################################
# defs
def callback(url):
    webbrowser.open_new(url)
######################################################################################################################
# The main hack that perfoms the wallhack
def button_action():
    if(change_button["text"]=="Start Wallhack"):
        change_button.configure(text="Stop Wallhack")
        print("\n")
        print("SCRIPT IS RUNNING")
        print("\n")
    else:
        change_button.configure(text="Start Wallhack")
        print("\n")
        print("SCRIPT IS STOPPED")
        print("\n")
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle, 'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F', clientModule).start() + 2

        pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
        pm.close_process()
    except:
        change_button.configure(text="Start Wallhack")
        print("error: please read the README file If you're having trouble join my discord")
        print("\n")
######################################################################################################################
# GUI
gui = Tk()
gui.title("Sleepy's hacks")
gui.geometry("500x400")

# Button
change_button = Button(gui, text="Start Wallhack", fg="black" , command=button_action)
change_button.place(x = 100, y = 50, width=300, height=100)

# Hyperlink
link = Label(gui, text="Github", fg="blue", cursor="hand2")
link.place(x = 100, y = 275, width=300, height=100)
link.bind("<Button-1>", lambda e: callback("https://github.com/c0dingcafe"))

# Hyperlink
link = Label(gui, text="DISCORD", fg="blue", cursor="hand2")
link.place(x = 100, y = 175, width=300, height=100)
link.bind("<Button-1>", lambda e: callback("https://discord.gg/Z9MxmBmKDP"))

mainloop()
