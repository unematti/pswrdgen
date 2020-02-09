#Create passwords using uppercase, lowercase, number and symbol characters
#The User is capable of choosing what kinds of characters to be included in
#the generated password, and how long the password will be.
#
from random import randint

def charlist(options): 
    #returns a list of characters based on chosen option
    #options should come in the format of 0 or 1, however
    #anything thats not 0 means include, and only 0 means exclude
    returnlist = ""
    lwrcase = "abcdefghijklmnopqrstuvwxyz" 
    uprcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!\"#$%&'()*+,-./:;<=>?@^[]^_`{|}~"
    returnlist += lwrcase if options[0] != 0 else "" # going through each set 
    returnlist += uprcase if options[1] != 0 else "" # adding the set to the
    returnlist += numbers if options[2] != 0 else "" # list of available characters
    returnlist += symbols if options[3] != 0 else "" # yay.
    return returnlist

def randomchar(chl):
    x = len(chl) - 1
    return chl[randint(1,x)]

def inquiry():
    options = [0,0,0,0,15] 
    options[0] = 1 if input("Should there be any lowercase letters? Y/N\n") != 'N' else 0
    options[1] = 1 if input("Uppercase ones? Y/N\n") != 'N' else 0
    options[2] = 1 if input("Any numbers? Y/N\n") != 'N' else 0
    options[3] = 1 if input("Finally, how about symbols? Y/N\n") != 'N' else 0
    options[4] = int(input("How long of a password do you need?\n"))
    return options

def pswrdgen():
    print("This is a strong password generator\nUse capital N for no, otherwise any answer means yes")
    pword = ""
    options = inquiry()
    available = charlist(options)
    for i in range(options[4]):
        pword += randomchar(available)
    return pword

print(pswrdgen())

