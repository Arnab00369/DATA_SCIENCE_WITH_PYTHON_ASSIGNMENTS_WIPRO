import re       # For regex pattern matching
import requests # To download HTML content from a URL

# URL of the HTML file
url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"

# Download the HTML content from the URL
response = requests.get(url)

# Use regex to extract text that appears between > and < (inside tags)
matches = re.findall(r'>([^<]+)<', response.text)

# Remove empty items and strip extra spaces
cleaned_text = [text.strip() for text in matches if text.strip()]

# Print the extracted content
print("Extracted Text Content:")
print(cleaned_text)