import pandas as pd


def read_file():
    return pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")


def check_missing_values(dataset):

    return dataset.isnull().sum()

def looping_missing_values(number_of_missing_values):
     for index in range(len(number_of_missing_values)):
         if number_of_missing_values[index] > 0:
              print(number_of_missing_values.keys()[index], number_of_missing_values[index])

def drop_column(dataset):
     dataset.drop(['OnlineSecurity', 'PhoneService', 'PaperlessBilling', 'OnlineBackup', 'DeviceProtection', 'SeniorCitizen'], axis = 1)

def change_variable(dataset):
    dataset["Churn"].eq('Yes').mul(1)

def grouping_columns(dataset):
    dataset.groupby('gender')['Churn'].sum()


if __name__ == '__main__':

    data = read_file()
    number_of_missing_values = check_missing_values(data)
    looping_missing_values(number_of_missing_values)
    change_variable(data)
    drop_column(data)
    grouping_columns(data)
    print(data)


    

