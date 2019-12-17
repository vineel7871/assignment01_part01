# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# importing required modules
import re
import xlrd
import pandas as pd
import mysql.connector
from mysql.connector import Error

# reading data from excel file to pandas dataframe
book = pd.read_excel("beginner_assignment01.xlsx", sheet_name=None)

# renaming column names to be compatible with mysql database
for sheet_name in book:
    sheet = book[sheet_name]
    identifier = re.compile(r"[\d\w_\s]",re.I)

    col_names = sheet.columns
    dict_names = {}
    for i in range(len(col_names)):
        column_name = col_names[i]
        column_name = "".join(filter(lambda x:identifier.match(x),column_name))
        column_name = "_".join(column_name.split())
        dict_names[col_names[i]] = column_name
    sheet.columns = dict_names.values()


# %%

def connect():
    """ Function to Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='assignment01_part01',
                                       user='root',
                                       password='Kvineel@7871')
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        if conn is not None and conn.is_connected():
            return conn


# %%

def create_database_schema():
    conn = connect()
    cur = conn.cursor()

    for sheet_name in book:
        sheet = book[sheet_name]

        # Drop table if exists
        cur.execute("DROP TABLE IF EXISTS %s;"%(sheet_name))

        # creating table
        cur.execute("CREATE TABLE %s (%s_id INT PRIMARY KEY AUTO_INCREMENT);"%(sheet_name, sheet_name))
        # cur.execute("CREATE TABLE %s;"%(sheet_name))

        # adding columns to table
        col_names = sheet.columns
        for i in range(len(col_names)):
            column_name = col_names[i]
            if sheet[col_names[i]].dtype == 'object':
                cur.execute("ALTER TABLE %s ADD %s varchar(255);"%(sheet_name, column_name))
            elif sheet[col_names[i]].dtype == 'int64':
                if not -2147483648 <= sheet[col_names[i]].max() <= 2147483647:
                    cur.execute("ALTER TABLE %s ADD %s BIGINT;"%(sheet_name, column_name))
                else:
                    cur.execute("ALTER TABLE %s ADD %s INT;"%(sheet_name, column_name))
            elif sheet[col_names[i]].dtype == 'float64':
                cur.execute("ALTER TABLE %s ADD %s DECIMAL(16,4);"%(sheet_name, column_name))
    conn.commit()
    conn.close()
    print("Created Database Schema")


# %%

def insert_data():
    conn = connect()
    cur = conn.cursor()

    print("inserting data")
    for sheet_name in book:
        sheet = book[sheet_name]

        col_names = list(sheet.columns)
        cols_name = ", ".join(col_names)

        rows, cols = sheet.shape
        for i in range(rows):
            vals = []
            for j in range(cols):
                vals.append(str(sheet.iat[i, j]))
            query = "INSERT INTO %s (%s) VALUES ("%(sheet_name, cols_name)
            query += "%s, "*(cols-1)
            query += "%s "
            query += ");"
            cur.execute(query, vals)
    
    print("commiting changes")
    conn.commit()
    conn.close()


# %%
if __name__ =="__main__":
    create_database_schema()
    insert_data()


# %%


