# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:40:24 2021

@author: Muhammad
"""
keyMatrix = [[0]*3 for i in range(3)]

messageMatrix  = [[0] for i in range(3)]

cipherMatrix = [[0] for i in range(3)]

#Function for creating matrix for key
def keymat(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k])%65
            k += 1
            
#Encrypting the key 
def encrypt(keyMatrix,messageMatrix):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for k in range(3):
                cipherMatrix[i][j] += keyMatrix[i][k]*messageMatrix[k][j]
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def hillcipher(message,key):
   #calling this function for creating keymatrix
    keymat(key)
    
    for i in range(3):
        messageMatrix[i][0] = ord(message[i]) % 65
    encrypt(keyMatrix, messageMatrix)  
    cipherText = []
    
    for i in range(3):
        cipherText.append(chr(cipherMatrix[i][0]+65))

    print("Cipher Text is: ","".join(cipherText))
    

def main():
    message = input("Enter the message : ").upper()
    key = input("Enter the key : ").upper()
    hillcipher(message,key)
    
    
    
if __name__ == "__main__":
    main()
    
