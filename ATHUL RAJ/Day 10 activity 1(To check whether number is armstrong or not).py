#created by athul raj
#date:21-11-2024
#To check whether number is armstrong or not
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
    