#HSSSC1PCL03466\BLUE
#HARVEYNASH\khangmaid
#%%
import pyodbc

cnxn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=HSSSC1PCL03466\BLUE;"
            "Database=AdventureWorks2016;"
            "Trusted_Connection=yes;"
            "UID=HARVEYNASH\khangmaid;")

cnxn = pyodbc.connect(cnxn_str) 
cursor = cnxn.cursor()
cursor.execute('SELECT addressline1 FROM person.Address where addressId = 1')

for row in cursor:
    print(row)
# %%
