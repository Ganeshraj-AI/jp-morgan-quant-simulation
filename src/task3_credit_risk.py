import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

df['payment_to_income'] = df['loan_amt_outstanding'] / df['income']
df['debt_to_income'] = df['total_debt_outstanding'] / df['income']

features = [
    'credit_lines_outstanding',
    'debt_to_income',
    'payment_to_income',
    'years_employed',
    'fico_score'
]

X = df[features]
y = df['default']

model = LogisticRegression(max_iter=10000)
model.fit(X, y)

def expected_loss(input_data):
    loan_amount = input_data["loan_amt_outstanding"]

    input_features = {
        "credit_lines_outstanding": input_data["credit_lines_outstanding"],
        "debt_to_income": input_data["total_debt_outstanding"] / input_data["income"],
        "payment_to_income": input_data["loan_amt_outstanding"] / input_data["income"],
        "years_employed": input_data["years_employed"],
        "fico_score": input_data["fico_score"]
    }

    input_df = pd.DataFrame([input_features])

    pd_prob = model.predict_proba(input_df)[0][1]

    return pd_prob * loan_amount * 0.9


print(expected_loss({
    "credit_lines_outstanding": 5,
    "loan_amt_outstanding": 20000,
    "total_debt_outstanding": 15000,
    "income": 50000,
    "years_employed": 5,
    "fico_score": 650
}))