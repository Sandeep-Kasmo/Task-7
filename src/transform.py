import pandas as pd
import mysql.connector
from mysql.connector import Error

def customers_transformation(dataframe):
    dataframe=dataframe.drop_duplicates()
    dataframe['registration_date']=pd.to_datetime(dataframe['registration_date'],format='mixed',errors='coerce').dt.strftime('%Y-%m-%d %H:%M:%S')
    dataframe=dataframe.fillna({'phone':'000-000-0000'})
    return dataframe

def orders_transformation(dataframe):
    dataframe=dataframe.drop_duplicates()
    dataframe=dataframe.dropna()
    dataframe['order_date']=pd.to_datetime(dataframe['order_date'],format='mixed',errors='coerce')
    dataframe=dataframe.sort_values(by='customer_id')
    return dataframe


