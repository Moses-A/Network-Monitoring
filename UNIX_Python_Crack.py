#!/usr/bin/env python2
# written by Moses Arocha
# Created in Python, with the help of TJ O'Connor's book "Violent Python"
# used for UNIX system passwords, with a two character Salt

import crypt

def testHash(cryptPass):
    salt = cryptPass[0:2] 				# Accounts for the salt hash: 2 characters.
    dictFile = open('mostcommonpasswords.txt', 'r') 
    for word in dictFile.readlines(): 		
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt) 		# Attempts to match a password with one from the password list along with the salted hash.
        if (cryptWord == cryptPass):
	    print ("\n\t[Success] The Has Been Found Password: "+word+"\n")
	    return
    print ("\n\t[Failure] The Password Has Not Been Found.\n")
    return

def main(): 
    usersName = raw_input("\n\n\t Please Insert A Name of a User : ") 
    Users = open('userslist.txt', 'w')      
    Users.write(usersName+':')		    #Note: Must add ":" after every entrance so the input can be readable.
    Users.close() 			   
    # The beginning of the second opening of the document, required for function, previous just adds ":"
    PassText = open('userslist.txt')
    for line in PassText.readlines():
        if ":" in line: 	     	    # Note: Only reads lines with ":", so it must be present.
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print ("\n\t[Attempt] Cracking Password For: "+user)
            testHash(cryptPass)  # Must reference the testHash function last, so all error handling could have occurred.

if __name__ == "__main__":
    main()
