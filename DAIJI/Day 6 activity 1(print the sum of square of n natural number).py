"""
Author: Daiji Kuriakose
Date:16-11-2024
Title:Python program to print sum of square of n natural numbers
"""
limit=int(input("Enter the last term: "))
sum=0
for i in range(limit+1):
    sum+=i*i
print(f"The sum of square of {limit} natural number is {sum}")