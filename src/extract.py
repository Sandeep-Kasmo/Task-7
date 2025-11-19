import pandas as pd
import mysql.connector
from mysql.connector import Error
conn=None
def establish_connection():
    try:
        global conn
        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='********',
            database='PythonLearningDB'
        )
        if conn.is_connected():
            print('Connected to MySQL')
            return conn
    except Error as e:
        print(f"Error{e}")
        return None

def get_customers(query):
    try:
        if conn is None or conn.is_connected()==False:
            try:
                establish_connection()
            except Error as e:
                print('Error:{e}')
                return None
        customer_df=pd.read_sql(query,conn)
        print('Extracted customers table')
        return customer_df
    except Error as e:
        print(f"Error:{e}")
        return None
    
def get_orders(query):
    try:
        if conn is None or conn.is_connected==False:
            try:
                establish_connection()
            except Error as e:
                print(f"Error:{e}")
                return None
        orders_df=pd.read_sql(query,conn)
        print('Extracted orders table')
        return orders_df
    except Error as e:
        print(f"Error extracting orders {e}")
        return None

def close_connection():
    global conn
    try:
        if conn and conn.is_connected():
            conn.close()
            print('Closed connection successfully!')
    except Error as e:
        print(f"Error closing connection {e}")


