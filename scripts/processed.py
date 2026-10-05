import pandas as pd
 
df = pd.read_json("raw_data/comments.json")
 
result = df[
    [
        "id",
        "name",
        "email"
    ]
]
 
result.to_csv(
    "processed_data/feedback_summary.csv",
    index=False
)
 
print(result.head())
print("CSV Created Successfully")