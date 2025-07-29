import modules_functions 

# Taking user input (in lowercase or uppercase)
name = input("Enter a name (all letters either lowercase or uppercase): ")

# Palindrome check
if modules_functions.ispalindrome(name):
   print("Yes, it is a palindrome.")
else:
   print("No, it is not a palindrome.")

# Count vowels
vowel_count = modules_functions.count_the_vowels(name)
print("No of vowels:", vowel_count)

# Frequency of letters
freq = modules_functions.frequency_of_letters(name)
freq_output = ', '.join([f"{char}-{count}" for char, count in freq.items()])
print("Frequency of letters:", freq_output)
