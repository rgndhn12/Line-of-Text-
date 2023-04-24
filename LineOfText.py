#Dahan,Regine Fae M. BSCPE 1-5 File Handling No. 3

def multiple():

    #open mylife.txt
    with open ("mylife.txt", "w") as user_input_line:
            
    #user's input line
        line_content = input ("Enter line: ")

    #   write in mylife.txt
        user_input_line.write(line_content)

    while True:  

    #asking another for a possible user's input line
        want_another = input ("Are there more lines y/n? ") 

    #   if yes
        if (want_another.lower() == "y"):
            multiple()
    #   if no
    
    #display the output

multiple()