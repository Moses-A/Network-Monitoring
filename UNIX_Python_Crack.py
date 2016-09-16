#!/usr/bin/env python2
# written by Moses Arocha
# Created in Python, with the help of TJ O'Connor's book "Violent Python"
# used for UNIX system passwords, with a two character Salt

import crypt

def testHash(crypt_Pass):
    salt = crypt_Pass[0:2] 				# Accounts for the salt hash: 2 characters.
    dict_File = open('mostcommonpasswords.txt', 'r') 
    for word in dict_File.readlines(): 		
        word = word.strip('\n')
        crypt_Word = crypt.crypt(word,salt) 		# Attempts to match a password with one from the password list along with the salted hash.
        if (crypt_Word == crypt_Pass):
	    print ("\n\t[Success] The Has Been Found Password: "+word+"\n")
	    return
    print ("\n\t[Failure] The Password Has Not Been Found.\n")
    return

def main(): 
    users_Name = raw_input("\n\n\t Please Insert A Name of a User : ") 
    Users = open('userslist.txt', 'w')      
    Users.write(users_Name+':')		    #Note: Must add ":" after every entrance so the input can be readable.
    Users.close() 			   
    # The beginning of the second opening of the document, required for function, previous just adds ":"
    Pass_Text = open('userslist.txt')
    for line in Pass_Text.readlines():
        if ":" in line: 	     	    # Note: Only reads lines with ":", so it must be present.
            user = line.split(':')[0]
            crypt_Pass = line.split(':')[1].strip(' ')
            print ("\n\t[Attempt] Cracking Password For: "+user)
            testHash(crypt_Pass)  # Must reference the testHash function last, so all error handling could have occurred.

if __name__ == "__main__":
    main()
