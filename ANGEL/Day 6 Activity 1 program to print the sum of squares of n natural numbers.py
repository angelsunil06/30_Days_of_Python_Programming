''' 
author:Angel
date:16-11-24
program to print the sum of squares of n natural numbers

'''
limit=int(input('enter no of terms:'))
sum=0
for i in range(1,limit+1):
	sum+=i*i
print (sum)