# This file is used to generate two "joinable" datasets to demonstrate IBM CP4D tools auto-join capabilities.


import pandas as pd


df = pd.read_csv('./credit_data.csv')


# Generate an ID column
df['ID'] = df.index + 100000

df_register = df[['ID', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'LIMIT_BAL', 'default']]
df_payments = df[['ID', 'PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6']]

df_register.to_csv('credit_info.csv', index=False)
df_payments.to_csv('payment_info.csv', index=False)
