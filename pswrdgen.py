from random import randint
#from sys import argv
import argparse

parser = argparse.ArgumentParser(description="Simple python script to generate passwords")
parser.add_argument("-l", help="Use of lowercase letters", action="store_true")
parser.add_argument("-u", help="Use of uppercase letters", action="store_true")
parser.add_argument("-n", help="Use of numbers", action="store_true")
parser.add_argument("-s", help="Use of symbols", action="store_true")
parser.add_argument('length', type=int, help='Length of the password, default to 15', nargs='*')
args = parser.parse_args()
#print(args)
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!\"#$%&'()*+,-./:;<=>?@^[]^_`{|}~"

character_list = lowercase if args.l else ""
character_list += uppercase if args.u else ""
character_list += numbers if args.n else ""
character_list += symbols if args.s else ""


length_of_list = len(character_list)

for i in range(len(args.length)):
    length_of_pwrd  = args.length[i]
    pwrd = ""
    for _ in range(length_of_pwrd):
         pwrd += character_list[randint(0,length_of_list - 1)]
    print(pwrd)  



