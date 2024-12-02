
numbers = []


n = int(input('How many numbers do you want to enter? '))


for i in range(n):
    number = int(input(f'Enter number {i+1}: '))
    numbers.append(number)




product = 1


for number in numbers:
    product *= number


print(f'The product of all elements in the list is: {product}')