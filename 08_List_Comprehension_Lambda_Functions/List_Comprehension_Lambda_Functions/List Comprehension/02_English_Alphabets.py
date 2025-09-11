import string

# get all lowercase alphabets
alphabets = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

# dictionary comprehension
alphabet_dict = {letter: index+1 for index, letter in enumerate(alphabets)}

print("Alphabet mapping:", alphabet_dict)
