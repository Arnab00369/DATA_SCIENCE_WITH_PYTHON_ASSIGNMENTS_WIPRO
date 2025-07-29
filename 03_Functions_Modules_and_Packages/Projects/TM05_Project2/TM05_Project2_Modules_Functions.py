# mymodule.py

def ispalindrome(name):
    if name == name[::-1]:
        return True
    else:
        return False

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
