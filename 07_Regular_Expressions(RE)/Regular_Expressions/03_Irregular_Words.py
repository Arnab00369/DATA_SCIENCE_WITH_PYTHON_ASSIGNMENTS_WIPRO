import re  # Regex helps in removing special characters and extra spaces

# Irregular sentence
sentence = """A, very    very; irregular_sentence"""

# Replace non-word characters (like , ; _) with space
cleaned = re.sub(r'\W+', ' ', sentence)

# Remove extra spaces from beginning and end
cleaned = cleaned.strip()

print("Cleaned sentence:", cleaned)