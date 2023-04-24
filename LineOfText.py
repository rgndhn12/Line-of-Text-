#Dahan,Regine Fae M. BSCPE 1-5 File Handling No. 3


#open mylife.txt
with open ("mylife.txt", "w") as user_input_line:
        
#user's input line
    line_content = input ("Enter line: ")

#   write in mylife.txt
    user_input_line.write(line_content)

#asking another for a possible user's input line
want_another = input ("Are there more lines y/n? ")
    
    #   if yes
    #   if no
    #display the output

