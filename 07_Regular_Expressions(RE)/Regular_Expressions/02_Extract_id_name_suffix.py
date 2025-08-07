import re  # Import regex module

# Sample emails
emails = """
zuck@facebook.com
sunder23@google.com
jeff42@amazon.com
"""

# Use regex to extract parts of the email
matches = re.findall(r'([\w\d]+)@([\w\d]+)\.(\w+)', emails)

# Loop through the results and print them clearly
counter = 0
for user, domain, suffix in matches:
   counter += 1
   print("User ID ",counter,":",user,"\t,Domain:",domain,"\tand, Suffix:",suffix)
