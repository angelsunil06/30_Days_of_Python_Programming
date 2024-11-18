#Program to input the list [10,20,30,40] and interchange the first and last elememts of the list and  print the modified list.

a=[10,20,30,40]

temp=a[0]
a[0]=a[3]
a[3]=temp
print(a)