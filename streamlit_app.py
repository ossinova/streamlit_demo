import streamlit as st
import pandas as pd


st.title('My first app')
df = pd.DataFrame({"Name": ["Bob", "John", "Jane"], "Age": [20, 21, 19]})
st.bar_chart(df)

                   