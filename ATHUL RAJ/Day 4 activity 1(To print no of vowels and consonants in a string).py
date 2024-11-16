#created by athul raj
#date:14-11-2024
#To print no of vowels and consonants in string
string_input=input("Enter a string:")
vowels="aeiouAEIOU"
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count +=1
print(f"The no of vowels in a string{string_input}={vowels_count}")
    
