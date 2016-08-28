#!/usr/bin/env python2
# written by Moses Arocha
# Created in Python, with the help of TJ O'Connor's book "Violent Python"
# used for UNIX system passwords, with a two character Salt

import crypt

def testHash(cryptPass):
    salt = cryptPass[0:2] # accounts for the salt hash, 2 is the character
    dictFile = open('mostcommonpasswords.txt', 'r') # imports and opens the most common passwords
    for word in dictFile.readlines(): # this reads the lines of the document
         word = word.strip('\n')
         cryptWord = crypt.crypt(word,salt) # states that the password is the most common password list along with the salted hash
	 if (cryptWord == cryptPass):
		print ("\n\t[Success] The Has Been Found Password: "+word+"\n")
		return
    print ("\n\t[Failure] The Password Has Not Been Found.\n")
    return

def main(): 
    usersName = raw_input("\n\n\t Please Insert A Name of a User : ") 
    Users = open('userslist.txt', 'w')  # opens up the text file userslist.txt
    Users.write(usersName+':')	    # adds : after every entrance so the input can be readable
    Users.close() 			    # most close the file after editing
    # the beginning of the second opening of the document for reading lines
    PassText = open('userslist.txt')
    for line in PassText.readlines():
	if ":" in line: 	     # searchs in the text file for word followed by :
	       user = line.split(':')[0]
	       cryptPass = line.split(':')[1].strip(' ')
	       print ("\n\t[Attempt] Cracking Password For: "+user)
	       testHash(cryptPass)  # references the testHash function

if __name__ == "__main__":
	main()
