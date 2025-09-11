import pandas as pd

# Direct URL (works like UCI dataset)
url = "https://raw.githubusercontent.com/selva86/datasets/master/50_Startups.csv"

# Load dataset from URL
startups = pd.read_csv(url,
   delim_whitespace=True,  # the file is space-delimited (or whitespace separated)
   header=None,             # no header row in the data file
   na_values='?')

print("First 5 Rows:\n", startups.head())
print("\nStatistical Summary:\n", startups.describe())
print("\nCorrelation Matrix:\n", startups.corr())
