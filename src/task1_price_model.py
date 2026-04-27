import pandas as pd

df = pd.read_csv("Nat_Gas.csv")
print(df.head())

print(df.info())
print(df.describe())

df['Dates'] = pd.to_datetime(df["Dates"])
df = df.sort_values('Dates')
df['Month'] = df['Dates'].dt.month
print(df.head())

monthly_avg = df.groupby('Month')['Prices'].mean()
print(monthly_avg)

import matplotlib.pyplot as plt
plt.plot(df["Dates"],df["Prices"])
plt.title("Average price per month")
plt.xlabel("Month")
plt.ylabel("Prices")
plt.show()

def predict_price(date):
    date = pd.to_datetime(date)
    month = date.month
    return monthly_avg[month]

print(predict_price("2025-01-15"))
print(predict_price("2025-06-10"))

