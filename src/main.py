import pandas as pd
from transform import *
from extract import *
from load import *
def main():

    # Establish connection
    establish_connection()

    # Load customers and orders data
    customers_df=get_customers('select * from customer')
    orders_df=get_orders('select * from orders')

    if customers_df is not None:
        print(f"Customers Data frame:\n{customers_df}\n")
    if orders_df is not None:
        print(f"Orders data:\n{orders_df}\n")

    # Apply transformations
    transformed_customers=customers_transformation(customers_df)
    transformed_orders=orders_transformation(orders_df)

    #Show transformed data
    if transformed_customers is not None:
        print(f"Transformed customers:\n{transformed_customers}\n")
    
    if transformed_orders is not None:
        print(f"Transformed Orders:\n{transformed_orders}\n")
    
    #create tables and load transformed data
    if transformed_customers is not None:
        create_customer_table()
        insert_customer_data(transformed_customers)
    
        



    # Close conmnection
    close_connection()

if __name__=='__main__':
    main()