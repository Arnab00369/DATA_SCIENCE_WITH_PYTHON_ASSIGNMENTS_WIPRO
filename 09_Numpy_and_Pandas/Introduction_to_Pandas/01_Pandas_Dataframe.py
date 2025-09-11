import pandas as pd

# URL of the raw data file
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"

# Read the data into a DataFrame. Note: there is no header row, and some horsepower values are '?'
cars = pd.read_csv(
   url,
   delim_whitespace=True,  # the file is space-delimited (or whitespace separated)
   header=None,             # no header row in the data file
   na_values='?'            # treat '?' as NaN for missing values
)

# Now assign column names based on dataset description
cars.columns = [
   "mpg", "cylinders", "displacement", "horsepower",
   "weight", "acceleration", "model_year", "origin", "car_name"
]

# Inspect first 10 rows
print("First 10 rows:")
print(cars.head(10))

# Inspect last 5 rows
print("\nLast 5 rows:")
print(cars.tail())

# Get metadata: data types, missing values, shape
print("\nInfo about dataset:")
print(cars.info())

print("\nShape of dataset:", cars.shape)

# Get summary statistics
print("\nStatistical summary:")
print(cars.describe())
