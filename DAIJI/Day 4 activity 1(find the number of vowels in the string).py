"""
Author: Daiji Kuriakose
Date:14-11-2024
Title:Python program to find the number of vowels in a string
"""
string_input=input("Enter a string")
vowels="aeiouAEIOU"
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
print(f"No of vowels in the given string {string_input}={vowels_count}")