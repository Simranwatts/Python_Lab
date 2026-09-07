import pandas as pd

data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 25, 22, 30],
    "Marks": [85, 72, 90, 65]
})

data.to_csv("data.csv", index=False)

df = pd.read_csv("data.csv")

print("Dataset Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)

filtered = df[df["Marks"] >= 80]

print("\nFiltered Data:")
print(filtered)

filtered.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data exported successfully.")
