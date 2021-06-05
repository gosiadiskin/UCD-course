import pandas as pd

data=pd.read_csv("BankChurners.csv")

print(data)
print(data["CLIENTNUM"])
print(data.shape)
print(data.info())
print(data.describe())
print(data.describe().transpose())
print(data.head(5))

python.exe -m pip install --upgrade pip

ggg
kkkk
