import pandas as pd
from sqlalchemy import create_engine

# CSV-polku VPS:llä
csv_file = "/home/ubuntu/myapp/Ecard.csv"

# Lue CSV
df = pd.read_csv(csv_file)

# MySQL-yhteys
MYSQL_USER = "VITTU"
MYSQL_PASSWORD = "Moimoi33-"
MYSQL_HOST = "127.0.0.1"
MYSQL_DB = "Ecard"

engine = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DB}")

# Tuo data tauluun
# Oletetaan, että halutaan vain nämä sarakkeet: Transactions, CustomerName, TransactionDate
df_mysql = df[['Data_value', 'Series_title_2', 'Period']].copy()
df_mysql.rename(columns={
    'Data_value': 'Transactions',
    'Series_title_2': 'CustomerName',
    'Period': 'TransactionDate'
}, inplace=True)

# Muuta TransactionDate oikeaan muotoon: YYYY-MM-DD
df_mysql['TransactionDate'] = pd.to_datetime(df_mysql['TransactionDate'].astype(str).str[:4] + '-01-01')

df_mysql.to_sql('Ecard', con=engine, if_exists='append', index=False)

print("CSV data uploaded to MySQL successfully!")

