import pandas as pd

df = pd.read_csv("artifacts\\data.csv")
print("====Column names======\n", df.columns)
# df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('/', '_')
)

print("====updated Column names======\n", df.columns)
df.to_csv("artifacts\\data.csv", index=False)

