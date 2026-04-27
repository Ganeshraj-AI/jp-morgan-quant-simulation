import pandas as pd
from src.price_model import predict_price

def contract_value_multiple(
    injection_dates,
    withdrawal_dates,
    volume_per_trade,
    max_storage,
    storage_cost_per_day,
    injection_cost,
    withdrawal_cost
):

    storage = 0
    total_cost = 0
    total_revenue = 0

    # Injection
    for d in injection_dates:
        d = pd.to_datetime(d)
        price = predict_price(d)

        if storage + volume_per_trade <= max_storage:
            storage += volume_per_trade
            total_cost += price * volume_per_trade
            total_cost += injection_cost

    # Withdrawal
    for d in withdrawal_dates:
        d = pd.to_datetime(d)
        price = predict_price(d)

        if storage >= volume_per_trade:
            storage -= volume_per_trade
            total_revenue += price * volume_per_trade
            total_cost += withdrawal_cost

    # Storage cost
    all_dates = pd.to_datetime(injection_dates + withdrawal_dates)
    duration = (max(all_dates) - min(all_dates)).days

    total_cost += duration * storage_cost_per_day

    return total_revenue - total_cost