
# 📂 ETL Pipeline: MySQL Customer & Order Data

A robust Python-based Extract, Transform, Load (ETL) pipeline designed to fetch customer and order data from a source MySQL database, apply necessary transformations (cleaning, formatting), and efficiently load the cleaned data into a target MySQL table (`Transformed_customers1`).

---

## 🚀 Getting Started

Follow these steps to set up and run the ETL pipeline locally.

### Prerequisites

You need **Python 3.8+** installed. The project relies on the following Python libraries:

```bash
pip install pandas
pip install mysql-connector-python
pip install configparser 
````

### Project Structure

The project is logically structured to separate the core ETL components (E, T, L) and configuration:

```
etl_project/
├── config/
│   └── config.ini         # Database credentials and configuration
├── src/
│   ├── extract.py         # Handles Extraction (data fetching via Pandas/SQL)
│   ├── transform.py       # Handles Transformation (cleaning, date formatting)
│   ├── load.py            # Handles Loading (table creation, bulk insertion)
│   └── main.py            # The primary execution orchestrator
└── README.md
```

### Configuration

Before running the pipeline, update your database connection details in **`config/config.ini`**. These credentials are used for both extracting (source) and loading (target/reporting layer):



-----

## ⚙️ How to Run the Pipeline

Execute the pipeline from the root directory of the project:

```bash
python src/main.py
```

### Expected Flow and Output

The script executes the stages sequentially, managed by the `main.py` orchestrator:

1.  **Connection:** `Connected to MySQL`
2.  **Extraction (E):** Data is fetched for customers and orders.
3.  **Transformation (T):** Data is cleaned, duplicates are dropped, and **datetime values are converted** to a MySQL-compatible string format (`YYYY-MM-DD HH:MM:SS`) to prevent insertion errors.
4.  **Loading (L):**
      * Table creation: `Table 'Transformed_customers1' created or already exists.`
      * **Bulk Insertion:** `insertion_success: Successfully inserted X rows.`
5.  **Cleanup:** `Closed connection successfully!`

-----

## 🔑 Key Implementation Details

### Data Integrity

  * **Duplicate Handling:** The `transform.py` functions use `dataframe.drop_duplicates()` to ensure unique records.
  * **Missing Data:** Null values for `phone` are handled by filling them with a default value.
  * **IDEMPOTENCY:** The `load.py` uses `CREATE TABLE IF NOT EXISTS` so the pipeline can be run repeatedly without error.

### High Performance Loading

The `insert_customer_data` function uses the high-performance **`cursor.executemany()`** method combined with Pandas' `.to_records()` to insert data in a single, optimized batch operation. This method ensures **fast insertion** and prevents the execution flow 