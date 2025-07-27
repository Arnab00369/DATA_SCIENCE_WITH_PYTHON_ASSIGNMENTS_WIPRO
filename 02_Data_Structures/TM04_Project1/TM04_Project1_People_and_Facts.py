# Step 1: Create a dictionary of people and facts
people_facts = {
   "Jeff": "Is afraid of Dogs.",
   "David": "Plays the piano.",
   "Jason": "Can fly an airplane."
}

# Step 2: Display the current dictionary
print("Initial List:\n")
for person in people_facts:
   print(person + ": " + people_facts[person])

# Step 3: Modify a fact
people_facts["Jeff"] = "Is afraid of heights."

# Step 4: Add a new person
people_facts["Jill"] = "Can hula dance."

# Step 5: Display the updated dictionary
print("\nUpdated List:\n")
for person in people_facts:
   print(person + ": " + people_facts[person])
