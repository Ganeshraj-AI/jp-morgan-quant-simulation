# 📊 JP Morgan Quantitative Research Simulation

## 🚀 Overview
This project is based on the JP Morgan Quantitative Research Virtual Experience, where real-world financial problems were solved using data analysis, modeling, and machine learning.

The project covers commodity pricing, contract valuation, credit risk modeling, and risk segmentation.

---

## 🧠 Tasks Completed

### 🔹 Task 1: Natural Gas Price Modeling
- Built a time-series model using trend and seasonality
- Predicted future gas prices for any given date

---

### 🔹 Task 2: Commodity Storage Contract Pricing
- Modeled profit/loss from storing natural gas
- Handled multiple injection and withdrawal dates
- Included storage constraints and costs

---

### 🔹 Task 3: Credit Risk Analysis
- Built a Logistic Regression model to estimate Probability of Default (PD)
- Performed feature engineering using financial ratios:
  - Debt-to-Income
  - Payment-to-Income
- Calculated Expected Loss using recovery rate assumptions

---

### 🔹 Task 4: FICO Score Bucketing
- Segmented borrowers into risk buckets based on FICO score
- Used quantile-based discretization
- Analyzed default probability across buckets

---

## ⚙️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn

---

## 📂 Project Structure


jp-morgan-quant-simulation/
│
├── data/
│ ├── Nat_Gas.csv
│ └── Loan_Data.csv
│
├── src/
│ ├── task1_price_model.py
│ ├── task2_storage_pricing.py
│ ├── task3_credit_risk.py
│ └── task4_fico_bucketing.py
│
├── requirements.txt
├── README.md
└── certificate.pdf


---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
Run individual tasks:
python src/task1_price_model.py
python src/task2_storage_pricing.py
python src/task3_credit_risk.py
python src/task4_fico_bucketing.py
##📈 Key Learnings
Time-series analysis for price forecasting
Financial contract valuation logic
Machine learning for credit risk prediction
Risk segmentation using data-driven methods
##📜 Certificate

The certificate of completion is included in this repository.

##💡 Summary

This project demonstrates practical applications of quantitative research in finance, combining data analysis, modeling, and decision-making.
