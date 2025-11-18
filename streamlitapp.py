import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# -----------------------------
# MySQL configuration
# -----------------------------
MYSQL_USER = "VITTU"
MYSQL_PASSWORD = "Moimoi33-"
MYSQL_HOST = "127.0.0.1"
MYSQL_DB = "Ecard"

# -----------------------------
# Get SQLAlchemy connection
# -----------------------------
@st.cache_resource
def get_connection():
    engine = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DB}")
    return engine

# -----------------------------
# Fetch data from MySQL
# -----------------------------
@st.cache_data(ttl=600)
def mySql():
    conn = get_connection()
    query = "SELECT TransactionDate, Transactions FROM Ecard LIMIT 100;"
    df = pd.read_sql(query, conn)
    
    # Muutetaan TransactionDate datetime-muotoon
    df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
    df['Year'] = df['TransactionDate'].dt.year  # otetaan vuosi
    
    return df

# -----------------------------
# Streamlit App
# -----------------------------
def main():
    st.title("Electronic Card Transactions")
    st.write("Visualization of card transaction data from MySQL.")

    # Fetch data
    data = mySql()
    
    st.write("Data preview:")
    st.dataframe(data.head())  # Näytetään muutama rivi

    # Plot data
    fig = px.line(
        data,
        x='Year',
        y='Transactions',
        title="Electronic Card Transactions per Year",
        labels={'Year': 'Vuosi', 'Transactions': 'Transactions'}
    )
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()

