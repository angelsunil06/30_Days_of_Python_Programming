"""
Author: Daiji Kuriakose
Date:2-12-2024
Title:Python Program to find the sum of digits of a number entered by the user
"""
number=int(input("enter the number:"))
sum=0
while number>0:
   remainder=number%10
   sum+=remainder
   number=number//10
print("the sum of the digits of the numberentered is:",sum)