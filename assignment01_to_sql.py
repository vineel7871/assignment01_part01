# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
from sqlalchemy import create_engine

# reading data from excel file to pandas dataframe
book = pd.read_excel("beginner_assignment01.xlsx", sheet_name=None)

# creating sqlalchemy engine connection
engine = create_engine("mysql+mysqlconnector://root:Kvineel@7871@localhost:3306/assignment01_part02")


# %%

# simpliest method for converting data between different formats is using pandas
for sheet_name in book:
    sheet = book.get(sheet_name)
    sheet.to_sql(sheet_name, con=engine, if_exists="replace", chunksize=50)

