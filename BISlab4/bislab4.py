
import pyodbc as odbc
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd

# These are the parameters we pass to make connection to the database
DRIVER = 'ODBC Driver 17 for SQL Server'  #Check your driver by typing python in windows search and put the following command
#import pyodbc
#print(pyodbc.drivers())
# from above code output see for odbc driver for sql server

SERVER = 'DESKTOP-3DP3BNF'  #check you server name in sql server management studio
# type the following querry to know the server name: SELECT @@SERVERNAME

DATABASE = 'BIS'  #ENTER Your database name here so to check the available database in sql server management studio
# type the following querry: SELECT * FROM sys.databases

# IN THIS IS WE WHERE WE MADE MISTAKE IN lab we put the wrong driver that is why it showed error of database connection timeout

connection_string = f"DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"

try:
    conn = odbc.connect(connection_string)
    print("Connection Successful")
except Exception as err:
    print("Connection Failed")
    print(err)

# Load Excel file
df = pd.read_excel(r"C:\Users\Dell\Downloads\BIS\Monthly_Statistics.xlsx")

# Create SQLAlchemy engine
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url, module=odbc)

# Load into SQL Server
try:
    df.to_sql("nrb_monthly_statistics", con=engine, schema="dbo", index=False, if_exists="append")
    print("Successful")

    #IF THE ABOVE CODE GETS EXECUTED IT SHOULD INSERT YOUR EXCEL FILE DATA INTO DATABASE WITHOUT HAVING TO CREATE TABLE
    # NOTE: nrb_monthly_statistics is the table name that i want to create in my database, you can put any name you like.
except Exception as error:
    print("Failed")
    print(error)


