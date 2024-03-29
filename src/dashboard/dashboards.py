import streamlit as st
import pandas as pd
import plotly.express as px

from runner import CSV_FILE

st.set_page_config(
    page_title="Analize de gastos do cartao nubank",
    page_icon=":bar_chart:",
    layout="wide",
)
df = pd.read_csv(CSV_FILE)
df = df[~df["Purchase"].str.contains("Pagamento recebido")]

df["Date"] = df["Date"].apply(lambda x: x.split(" ")[0])
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d").dt.strftime("%d/%m/%Y")

df.sort_values("Date", ascending=False, inplace=True)

st.title("Analize de gastos do cartao nubank")

st.sidebar.title("Filtros")
st.sidebar.write("Filtre os valores da tabela")
st.sidebar.write("Qual o valor de corte?")
cut_value = st.sidebar.number_input("Valor de corte", min_value=0, value=1)
apply_cut = st.sidebar.checkbox("Aplicar cortes")

if apply_cut:
    df = df[df["Value"] <= cut_value]

range_selection = st.sidebar.slider(
    "Select a range", 0.0, df["Value"].min(), (df["Value"].min(), df["Value"].max())
)

col1, col2 = st.columns(2)

df = df[(df["Value"] >= range_selection[0]) & (df["Value"] <= range_selection[1])]
st.write("Total de gastos: ", round(df["Value"].sum(), 2))
col1.write(df)

fig = px.bar(df, x="Date", y="Value", color="Purchase", title="Compras por dia")
col2.plotly_chart(fig)

col3, col4 = st.columns(2)

fig = px.pie(df, names="Tag", title="Compras por tipo")
col3.plotly_chart(fig)
fig = px.pie(df, names="Group", values="Value", title="Compras por grupo de gastos")
col4.plotly_chart(fig)
