from collections import Counter
import re

# Ask user for the filename
filename = input("Enter the filename: ")

try:
   with open(filename, 'r') as file:
      lines = file.readlines()
   
   # Count number of lines
   num_lines = len(lines)

   # Determine meeting time (12-hour format)
   if num_lines > 12:
      meeting_time = num_lines - 12
      time_period = "PM"
   else:
      meeting_time = num_lines
      time_period = "AM"

   # Join all lines into a single string and normalize words
   text = ' '.join(lines)

   # Extract words (only alphabets, ignore case)
   words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    # Count word frequency
    word_freq = Counter(words)
    
    # Get the most common word
    most_common_word, _ = word_freq.most_common(1)[0]

    # Capitalize first letter for proper street name format
    meeting_place = most_common_word.capitalize() + " Street"

    # Print the result
    print("\nMeeting time: {} {}".format(meeting_time, time_period))
    print("Meeting place:", meeting_place)

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
