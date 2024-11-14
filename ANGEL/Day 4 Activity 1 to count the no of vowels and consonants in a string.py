'''
author:angel
date:14-11-24
program to count the no of vowels and consonants in a string

'''
string=input('enter a string:')
vowelcount=0
consonantcount=0
vowels='aeiouAEIOU'
for i in string:
    if i in vowels:
       vowelcount+=1
    else:
        consonantcount+=1
print('the no of vowels is',vowelcount)
print('the no of consonants is:',consonantcount)
