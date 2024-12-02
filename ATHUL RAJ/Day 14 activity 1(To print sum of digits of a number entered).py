#created by athul raj
#date:2-12-2024
#python program to find sum of digits of a number entered by user
number=int(input("Enter the number:"))
sum=0
while number>0:
    rem=number%10
    sum+=rem
    number=number//10
print("The sum of digits of entered number is:",sum)
    
