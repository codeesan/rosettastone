eng = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",","]
hyro = ["N","D","E","F","S","I","W","V","O","P","X","T","Y","A","C","G","K","M","U","H","J","L","Z","Q","B","R"," ",".",","]


#function for translating english to hyro
def eng2hyro(mystring):
    mystring = mystring.upper()
    #set decoded_value to blank
    decoded_value = ""
    #go through every letter in 'mystring'
    for myletter in mystring:
        #find the value of each letter in eng
        index = eng.index(myletter)
        #find the matching letter in hyro
        hyroletter = hyro[index]
        decoded_value += hyroletter
    print(decoded_value)


#function to translate hyro to english
def hyro2english(mystring):
    #make sure it is uppercase
    mystring = mystring.upper()
    #set decoded_value to blank
    decoded_value = ""
    #go through every letter in mystring
    for myletter in mystring:
        #find the value of each letter in hyro
        index = hyro.index(myletter)
        #find the matching letter in english
        engletter = eng[index]
        decoded_value += engletter
    print(decoded_value)


