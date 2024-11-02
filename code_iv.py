import pandas as pd
import numpy as np
import streamlit as st

df_viales = pd.read_csv("incidentes_viales.csv")

st.write(df_viales)
st.write(df_viales.columns)
st.write(len(df_viales))

columnas = ["LOCATION", "CLASE_ACCIDENTE", "GRAVEDAD_ACCIDENTE"]
df_mapa = df_viales[columnas]
df_mapa["LATITUD"] = df_mapa["LOCATION"].str[1:15].astype(float)
df_mapa["LONGITUD"] = df_mapa["LOCATION"].str[17:-1].astype(float)

st.write(df_mapa)

st.map(df_mapa, latitude="LATITUD", longitude="LONGITUD")