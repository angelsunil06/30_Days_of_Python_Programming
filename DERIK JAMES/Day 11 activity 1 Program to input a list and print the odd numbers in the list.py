


numbers = []


n = int(input('How many numbers do you want to enter? '))


for i in range(n):
    number = int(input(f'Enter number {i+1}: '))
    numbers.append(number)


print('Odd numbers in the list are:')
for number in numbers:
    if number % 2 != 0:
        print(number)