import pandas as pd

import numpy as np

import matplotlib.pyplot as plt


def read_file():
    return pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")


def check_missing_values(dataset):
    return dataset.isnull().sum()

def looping_missing_values(number_of_missing_values):
     for index in range(len(number_of_missing_values)):
         if number_of_missing_values[index] > 0:
              print(number_of_missing_values.keys()[index], number_of_missing_values[index])

def drop_column(dataset):
     return dataset.drop(['OnlineSecurity', 'PhoneService', 'PaperlessBilling', 'OnlineBackup', 'DeviceProtection', 'SeniorCitizen'], axis = 1)

def change_variable(dataset):
    dataset["Churn"] = dataset["Churn"].eq('Yes').mul(1)


def grouping_columns(dataset):
    return dataset.groupby('gender')['Churn'].sum()

def median(dataset):
    median_monthly_charges = dataset['MonthlyCharges'].median()

    dataset['TotalCharges'].replace(' ',np.nan, inplace = True)
    dataset.dropna(subset=['TotalCharges'], inplace = True)
    dataset.reset_index(drop = True, inplace = True)
    dataset['TotalCharges'] = dataset['TotalCharges'].astype(float)
    median_total_charges = dataset['TotalCharges'].median()
    return(median_total_charges, median_monthly_charges)

def gender_vizualization(groups):
    gender = [groups.keys()[0],groups.keys()[1]]
    values = [groups['Female'],groups['Male']]
    plt.figure(figsize = (8, 5))
    plt.bar(gender,values,color = 'maroon',width =0.1)
    plt.xlabel("Gender")
    plt.ylabel("Churn")
    plt.title("Churn by gender")
    plt.show()

def median_vizualization(median_total_charges, median_monthly_charges):
    charges = ['Total charges', 'Monthly charges']
    values = [median_total_charges,median_monthly_charges]
    plt.figure(figsize = (8, 5))
    plt.bar(charges,values,color = 'maroon',width = 0.1)
    plt.xlabel("Median charges")
    plt.ylabel("Value")
    plt.title("Median total vs median monthly")
    plt.show()

def payment_vizualization(data):
    methods = list(data.keys())
    values = list(data.values())
    plt.figure(figsize = (8, 5))
    plt.bar(methods,values, color = 'maroon',width = 0.1)
    plt.xlabel("Payment method")
    plt.ylabel("Value")
    plt.title("Payment methods")
    plt.show()

def payment_methods(data):
    payments = data['PaymentMethod'].unique()
    pay = {}
    for method in payments:
        pay[method] = data['PaymentMethod'].str.count(method).sum()
    return pay



if __name__ == '__main__':

    data = read_file()
    median_total_charges, median_monthly_charges = median(data)Snip20210420_1.png
    data = drop_column(data)
    change_variable(data)
    number_of_missing_values = check_missing_values(data)
    looping_missing_values(number_of_missing_values)
    group = grouping_columns(data)
    pay = payment_methods(data)
    gender_vizualization(group)
    median_vizualization(median_total_charges,median_monthly_charges)
    payment_vizualization(pay)



    

