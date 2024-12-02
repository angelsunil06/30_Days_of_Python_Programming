'''
author:Angel
date:2-12-24
program to find the sum of digits of a number
'''
number=int(input('enter number:'))
sum=0
while number>0:
	rem=number%10
	sum+=rem
	number=number//10
print('the sum of the digits of the number entered is:',sum)