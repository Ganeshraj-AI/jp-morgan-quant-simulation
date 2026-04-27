from src.storage_model import contract_value_multiple

result = contract_value_multiple(
    ["2025-06-01", "2025-07-01"],
    ["2025-12-01", "2026-01-01"],
    100000,
    200000,
    1,
    1000,
    1000
)

print("Final Contract Value:", result)