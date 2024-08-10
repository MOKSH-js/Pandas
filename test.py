import pandas as pd
dic1 = {
    "name": ("moksh", "harry"),
    "marks": (78, 98),
    "city": ("surat", "ahemdabad")
}
df = pd.DataFrame(dic1)
print(df)
dic2 = pd.Series([12, 23, 34.45])
print(dic2)
df.to_csv("friend.csv", index=False)