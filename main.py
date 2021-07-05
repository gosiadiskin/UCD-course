import pandas as pd
pd.set_option('display.expand_frame_repr', False)

debt=pd.read_csv('MunicipalDebtAnalysis.csv')

print(debt.info())

print(debt.head())

print(debt.shape)

print(debt.describe())

print(debt.isnull().sum())

print(debt.sort_values(['propertyvalue','totalbilling'], ascending=[False, False]))

