import streamlit as st
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.write("# My First App")
st.write("## Second Header")

df = pd.read_csv("11_dars.csv")
st.line_chart(df["lat"])
bin = st.select_slider(
    "select bin number",
    options=list(range(10, 46)))
st.write("My favorite color is", bin)

fig, ax = plt.subplots()
sns.histplot(df['lat'], bins=bin, ax=ax)
st.pyplot(fig)
with st.sidebar:
    
    st.line_chart(df["lat"])
    
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

tab1, tab2, tab3 = st.tabs(["Footballer", "Car", "Iphone"])

with tab1:
   st.header("Futbolchi")
   st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTShVFRwhXQyMM6wYsUIgABQiRA_rVfWvFC0w&s", width=200)
   

with tab2:
   st.header("Avtomobil")
   st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv0wenMCK_VsbZfQGFOGu1gkCK7G1K-MOIDw&s", width=200)

with tab3:
   st.header("Telifon")
   st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTraEUjqCXgRfxBHlVi6yfyfw27pgWBU6w3gw&s", width=200)

df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
my_data_element = st.line_chart(df)

for tick in range(10):
    time.sleep(.5)
    add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
    my_data_element.add_rows(add_df)

st.button("Regenerate")