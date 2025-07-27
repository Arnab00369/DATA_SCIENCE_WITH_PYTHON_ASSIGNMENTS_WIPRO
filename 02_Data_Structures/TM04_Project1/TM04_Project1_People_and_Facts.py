# Project 1:
# Create a dictionary that contains a list of people and one interesting fact about each of them.
# Display each person and his or her interesting fact to the screen. Next, change a fact about one of
# the people. Also add an additional person and corresponding fact. Display the new list of people
# and facts. Run the program multiple times and notice if the order changes.

# Sample output:

# Jeff: Is afraid of Dogs.

# David: Plays the piano.

# Jason: Can fly an airplane.

# Jeff: Is afraid of heights.
# David: Plays the piano.
# Jason: Can fly an airplane.

# Jill: Can hula dance.


# Step 1: Create a dictionary of people and facts
people_facts = {
   "Jeff": "Is afraid of Dogs.",
   "David": "Plays the piano.",
   "Jason": "Can fly an airplane."
}

# Step 2: Display the current dictionary
print("Initial List:")
for person in people_facts:
   print(person + ": " + people_facts[person])

# Step 3: Modify a fact
people_facts["Jeff"] = "Is afraid of heights."

# Step 4: Add a new person
people_facts["Jill"] = "Can hula dance."

# Step 5: Display the updated dictionary
print("\nUpdated List:")
for person in people_facts:
   print(person + ": " + people_facts[person])
