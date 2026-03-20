import pandas as pd

# Load the data
df = pd.read_csv('superstore_sales.csv', encoding='latin-1')

# Convert dates from text to proper date format
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Clean column names (remove spaces, lowercase)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Remove duplicate rows (just in case)
df = df.drop_duplicates()

# Save the cleaned file
df.to_csv('clean_sales.csv', index=False)

print("Done! Clean file saved.")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
