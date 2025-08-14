import pandas as pd
import streamlit as st

st.title("Test caricamento dati")

@st.cache_data
def load_data():
    try:
        df = pd.read_excel("Ubicazione ricambi.xlsx")
        st.write("✅ File Excel caricato con successo")
        return df
    except Exception as e:
        st.error(f"❌ Errore caricamento dati: {e}")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.warning("⚠️ Il DataFrame è vuoto o il file non è stato caricato correttamente")
    st.stop()
else:
    st.write(f"📊 Il DataFrame contiene {len(df)} righe")
    st.dataframe(df.head())
