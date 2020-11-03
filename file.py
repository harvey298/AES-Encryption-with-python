# Start | Made by harvey298
import os
os.system("title Installing needed packages to be able to run (pyAesCrypt)")
os.system("pip install pyAesCrypt") # Installs pyAesCrypt
os.system("cls") # Clears terminal (windows only command)
import time
import string
from datetime import datetime
import pyAesCrypt
from random import *
characters = string.ascii_letters +  string.digits 
os.system("title Harvey Encrypt - HarCrypt")
okay = ".pyAesCrypt"

# Encrypts files
def encryptor(encryptpass, filename):
    print("Encrypting, File: " + filename + " | Password: " + encryptpass)
    pyAesCrypt.encryptFile(filename, (filename+okay), encryptpass, 256)

# Decrypts files
def decryptor(encryptpass, filename):
    print("Decrypting, File: " + filename + " | Password: " + encryptpass)
    pyAesCrypt.decryptFile(filename, (filename+'Decrypted.txt'), encryptpass, 256)

# Sets up for file encryption
def encryptsetup():
    filename = input("Welcome! what would you like to encrypt? ")
    os.system("cls")
    passtype = input("Would you like to make your own password? (y/n) ")
    os.system("cls")
    if passtype == "y":
        encryptpass = input("Password: ")
        os.system("cls")
        encryptor(encryptpass)
    else:
        encryptpass = "".join(choice(characters) for x in range(randint(16, 16)))
        try:
            with open('pass.txt','a+') as txt:              
                 txt.write("\n Pass: " + encryptpass)
        except ValueError:
            print("Cannot write to file")
        encryptor(encryptpass, filename)

# Sets up for file decryption
def decryptsetup():
    filename = input("Welcome! what would you like to decrypt? ")
    os.system("cls")
    encryptpass = input("Password: ")
    os.system("cls")
    decryptor(encryptpass, filename)

action = input("Welcome! would you like to Encrypt? (y/n) ")
if action == "y":
    os.system("cls")
    print("ok Encryption")
    encryptsetup()
else:
    os.system("cls")
    print("ok Decryption")
    decryptsetup()
