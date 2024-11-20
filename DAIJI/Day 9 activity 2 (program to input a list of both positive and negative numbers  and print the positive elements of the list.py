"""
Author: Daiji Kuriakose
Date:20-11-2024
Title:Python program to input a list of both positive and negative numbers  and print the positive elements of the list
"""
list=[-1,-5,3,8,20,-40,-20]
print(f"The positive elements are :")
for num in list:
    if num>0:
     print(num)