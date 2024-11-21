"""
Author: Daiji Kuriakose
Date:21-11-2024
Title:Python Program to check whether a number is armstrong or not
"""
number=int(input("Enter a number:"))
armstrong=number
sum=0
while number>0:
    remainder=number%10
    sum+=remainder*remainder*remainder
    number=number//10
if sum==armstrong:
    print("The number is armstrong")
else:
    print("The number is not armstrong")