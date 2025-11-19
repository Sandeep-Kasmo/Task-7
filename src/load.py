import mysql.connector
import pandas as pd
from extract import *
from transform import *
from mysql.connector import Error

def create_customer_table():
    global conn
    cursor=None
    if conn is None or conn.is_connected==False:
        try:
            conn=establish_connection()
        except Error as e:
            print('Error connecting to sql:{e}')
            return False
    cursor=conn.cursor()

    try:
        cursor.execute(
            '''create table if not exists Transformed_customers1(
            customer_id int,
            name varchar(100),
            email varchar(100),
            phone varchar(100),
            address varchar(255),
            registration_date datetime,
            loyalty_status varchar(100)
            )
'''

        )
        conn.commit()
        return True
    except Error as e:
        print(f"Error creating table:{e}")
        return False
    finally:
        if cursor:
            cursor.close()

def insert_customer_data(dataframe):
    global conn
    cursor=None
    
    # 1. Connection Check (Corrected for proper function call)
    if conn is None or not conn.is_connected():
        try:
            # establish_connection MUST return the connection object
            conn = establish_connection() 
        except Error as e:
            print(f"Error establishing connection: {e}")
            return False
            
    if conn is None:
        print("Data insertion failed: Connection is None.")
        return False
        
    cursor=conn.cursor()

    # CRITICAL FIX 1: Use executemany for bulk insertion
    INSERT_QUERY = '''
        INSERT INTO Transformed_customers1
        (customer_id, name, email, phone, address, registration_date, loyalty_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''

    try:
        # 2. Prepare Data: Convert the DataFrame into a list of tuples 
        #    (excluding the DataFrame index) for efficient bulk execution.
        data_to_insert = dataframe.to_records(index=False).tolist()
        
        # 3. Execute Bulk Insertion
        cursor.executemany(INSERT_QUERY, data_to_insert)
        
        conn.commit()
        print(f'insertion_success: Successfully inserted {cursor.rowcount} rows.')
        return True
    
    except Error as e:
        print(f"Error inserting data: {e}")
        if conn:
            conn.rollback() # Rollback changes if any error occurs
        return False
        
    finally:
        if cursor:
            cursor.close()
