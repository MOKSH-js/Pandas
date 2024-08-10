import pandas as pd
dict1={
    "Name": ("Moksh","Harry","Nigga","Zeus"),
    "City": ("Surat","Delhi","Nigeria","Asgard"),
    "Age": (17,28,69,51)
}
df = pd.DataFrame(dict1)
print(df)
#print(df)
#df.to_csv("Yoohoohoo.csv",index=False)
#df2=pd.read_csv("Yoohoohoo.csv")
#print(df2,"Name=="Moksh")
#print(df2)