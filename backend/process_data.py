import pandas as pd

data = {
    "category": ["Food", "Travel", "Shopping"],
    "amount": [120, 300, 200]
}

df = pd.DataFrame(data)

# Aggregate data
summary = df.groupby("category").sum()

print(summary)
