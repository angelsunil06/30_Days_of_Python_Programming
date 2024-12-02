my_list = [10, 20, 30, 40]
element = int(input('Enter the element: '))  

if element in my_list:
    print(f"{element} exists in the list")
else:
    print(f"{element} does not exist in the list")