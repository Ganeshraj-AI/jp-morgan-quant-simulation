import pandas as pd
import numpy as np

df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

n_buckets = 5

df = df.sort_values("fico_score")

df['bucket'] = pd.qcut(df['fico_score'], q=n_buckets, labels=False)

bucket_summary = df.groupby('bucket').agg({
    'fico_score': ['min', 'max'],
    'default': ['mean', 'count']
})

bucket_summary.columns = ['min_score', 'max_score', 'pd', 'count']
bucket_summary = bucket_summary.sort_values('min_score')

def get_rating(fico_score):
    for i, row in bucket_summary.iterrows():
        if row['min_score'] <= fico_score <= row['max_score']:
            return i
    return None

print(bucket_summary)
print(get_rating(750))
print(get_rating(600))