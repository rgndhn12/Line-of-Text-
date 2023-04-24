#Dahan,Regine Fae M. BSCPE 1-5 File Handling No. 3

#introduction
import pyfiglet
import time
import colorama
from colorama import Fore
colorama.init()
print(Fore.GREEN+pyfiglet.figlet_format(" HI ",font="isometric1"))
time.sleep(1)
border = "—" * 115
print(border)
print(Fore.CYAN+' This Program is entitled Line Of Text. The input lines by the user will go to a file named "mylife.txt".')
print(border)
time.sleep(2)

def multiple():

    #open mylife.txt
    with open ("mylife.txt", "a") as user_input_line:
            
    #user's input line
        line_content = input ("Enter line:")

    #   write in mylife.txt
        user_input_line.write(line_content +"\n")

    while True: 

    #asking another for a possible user's input line
        want_another = input ("Are there more lines y/n? ")
 
    #   if yes
        if (want_another.lower() == "y"):
            multiple()
    #   if no
        elif (want_another.lower() == "n"):
            print(border)
            time.sleep(2)
            print(Fore.YELLOW+pyfiglet.figlet_format("YEY",font="isometric1"))
            print("You can now view your input line in mylife.txt!")
            exit()
        else:
            print ("Invalid.")
            break
    
multiple()