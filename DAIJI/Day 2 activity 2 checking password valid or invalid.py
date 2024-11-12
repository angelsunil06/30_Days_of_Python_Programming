"""
Author: Daiji Kuriakose
Date  :12-11-2024
Title :Python program to print if a password is valid or not
"""
password=(input("Enter the password"))
if(len(password)<6):
    print("The password is invalid")
else:
    print("The password is valid")