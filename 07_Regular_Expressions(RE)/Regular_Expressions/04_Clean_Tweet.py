import re  # Import regular expression module

# Raw tweet with unwanted elements
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwejpxod cc: @garybernhardt #rstats'''

# Step-by-step cleaning using regex
tweet = re.sub(r'RT\s*@\w+:?', '', tweet)       # Remove retweet and mentions
tweet = re.sub(r'http\S+', '', tweet)           # Remove URLs
tweet = re.sub(r'@\w+', '', tweet)              # Remove mentions
tweet = re.sub(r'#\w+', '', tweet)              # Remove hashtags
tweet = re.sub(r'[^\w\s]', '', tweet)           # Remove punctuation
tweet = re.sub(r'\s+', ' ', tweet).strip()      # Normalize multiple spaces

print("Cleaned tweet:", tweet)
