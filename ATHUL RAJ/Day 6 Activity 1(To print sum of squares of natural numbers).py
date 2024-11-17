#created by athul raj
#date:16-11-2024
#To print sum of squares od n natural numbers
limit=int(input("Enter a natural number:"))
sum=0
for i in range(limit+1): 
    sum+=i*i
print(f"The sum of squares of {limit} natural numbers is {sum}")


    