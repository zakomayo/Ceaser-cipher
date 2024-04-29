# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:18:07 2024

@author: MGundagi
"""

def cipher():
    
    message = input("Enter word to be encrypted:")
    cipher_key = int(input("Enter key for cipher:"))
    result = ""
    LAST_CHAR_CODE = 90
    CHAR_RANGE = 26
    
    for char in message.upper():
        if char.isalpha():
            char_code = ord(char)
            encrypted_code = char_code + cipher_key
            
            if encrypted_code > LAST_CHAR_CODE :
                encrypted_code -= CHAR_RANGE
                
            encrypted_message = chr(encrypted_code)
            
            result += encrypted_message
        else:
            result += char
            
    print(result)

cipher()