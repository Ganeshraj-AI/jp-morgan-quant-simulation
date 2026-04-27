from datetime import datetime
import math

def contract_value(injection_dates, injection_prices, withdrawal_dates, withdrawal_prices,
                   rate, max_storage, storage_cost, injection_withdrawal_cost):

    injection_dates = [datetime.strptime(d, "%Y-%m-%d") for d in injection_dates]
    withdrawal_dates = [datetime.strptime(d, "%Y-%m-%d") for d in withdrawal_dates]

    all_dates = sorted(set(injection_dates + withdrawal_dates))

    volume = 0
    buy_cost = 0
    cash_in = 0

    for d in all_dates:
        if d in injection_dates:
            if volume <= max_storage - rate:
                volume += rate
                price = injection_prices[injection_dates.index(d)]
                buy_cost += rate * price
                buy_cost += rate * injection_withdrawal_cost

        elif d in withdrawal_dates:
            if volume >= rate:
                volume -= rate
                price = withdrawal_prices[withdrawal_dates.index(d)]
                cash_in += rate * price
                cash_in -= rate * injection_withdrawal_cost

    duration = (max(withdrawal_dates) - min(injection_dates)).days
    storage_total = math.ceil(duration / 30) * storage_cost

    return cash_in - buy_cost - storage_total


print(contract_value(
    ["2025-01-01", "2025-02-01"],
    [20, 21],
    ["2025-03-01", "2025-04-01"],
    [25, 26],
    100000,
    200000,
    10000,
    0.0005
))