"""
Author: Daiji Kuriakose
Date:1-12-2024
Title:Python Program to count the number of even and odd  numbers in a list
"""
empty_list=[]
limit=int(input('enter limit:'))
for i in range(limit):
	a=int(input('enter element:'))
	empty_list.append(a)
even_count=0
odd_count=0
print(empty_list)
for i in empty_list:
	if i%2==0:
		even_count+=1
	else:
		odd_count+=1
print('the number of even numbers in the list is:',even_count)
print('the number of odd numbers in the list is:',odd_count)