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

# import matplotlib.pyplot as plt
# plt.plot(df["Dates"],df["Prices"])
# plt.title("Average price per month")
# plt.xlabel("Month")
# plt.ylabel("Prices")
# plt.show()

def predict_price(date):
    date = pd.to_datetime(date)
    month = date.month
    return monthly_avg[month]

print(predict_price("2025-01-15"))
print(predict_price("2025-06-10"))

def contract_value(injection_date,withdrawal_date,volume):
    buy_price = predict_price(injection_date)
    sell_price = predict_price(withdrawal_date)
    profit = (sell_price - buy_price) * volume
    return profit

print(contract_value("2025-06-01", "2025-12-01", 100000))

def contract_value(injection_date, withdrawal_date, volume,
                   storage_cost, injection_cost, withdrawal_cost):

    injection_date = pd.to_datetime(injection_date)
    withdrawal_date = pd.to_datetime(withdrawal_date)

    buy_price = predict_price(injection_date)
    sell_price = predict_price(withdrawal_date)

    profit = (sell_price - buy_price) * volume

    days = (withdrawal_date - injection_date).days
    storage_total = days * storage_cost

    final = profit - storage_total - injection_cost - withdrawal_cost

    return final

print(contract_value(
    "2025-06-01",   # injection date
    "2025-12-01",   # withdrawal date
    1000,           # volume
    5,              # storage cost per day
    100,            # injection cost
    100             # withdrawal cost
))

print(contract_value(
    "2025-06-01",
    "2025-12-01",
    100000,   # bigger volume
    1,        # lower storage cost
    100,
    100
))

def contract_value_multiple(injection_dates,withdrawal_dates,volume_per_trade,max_storage,storage_cost_per_day,injection_cost,withdrawal_cost):
    storage = 0
    total_cost = 0
    total_revenue = 0
    
    for d in injection_dates:
        d = pd.to_datetime(d)
        price = predict_price(d)

    if storage + volume_per_trade <= max_storage:
        storage += volume_per_trade
        total_cost += price * volume_per_trade
        total_cost += injection_cost
    
    for d in withdrawal_dates:
        d = pd.to_datetime(d)
        price = predict_price(d)

    if storage >= volume_per_trade:
        storage -= volume_per_trade
        total_revenue += price * volume_per_trade
        total_cost += withdrawal_cost
    
    all_dates = pd.to_datetime(injection_dates + withdrawal_dates)
    duration = (max(all_dates) - min(all_dates)).days

    total_cost += duration * storage_cost_per_day
    return total_revenue - total_cost

print(contract_value_multiple(["2025-06-01", "2025-07-01"],["2025-12-01", "2026-01-01"],100000,200000,1,1000,1000))

