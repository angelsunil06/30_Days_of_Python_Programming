'''
author:Angel
date:17-11-24
program to calculate simple interest

'''
principle=int(input('enter principle:'))
rate=int(input('enter rate:'))
years=int(input('enter no of years:'))
simpleinterest=(principle*rate*years)/100
print('The simple interest is:',simpleinterest)