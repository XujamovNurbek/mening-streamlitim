import streamlit as st
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime
st.write("# Texnika va unga bog'liq talablarning umumiy jadvali")
with st.sidebar:
    st.write("# Bu yerda streamlitning qiziqarli funksiyalarini ko'rishingiz mumkin:")
df=pd.read_csv("15_variant.csv")
st.dataframe(df)
st.divider()

with st.sidebar:
    activated=st.toggle("Streamlit funksiyalari bilan tanishib chiqish")
    if activated:
        data_df = pd.DataFrame(
            {
                "appointment": [
                    datetime(2024, 7, 20, 12, 0),
                    datetime(2024, 12, 19, 18, 0),
                
                ]
            }
        )

        st.data_editor(
            data_df,
            column_config={
                "appointment": st.column_config.DatetimeColumn(
                    "Appointment",
                    min_value=datetime(2023, 6, 1),
                    max_value=datetime(2025, 1, 1),
                    format="D MMM YYYY, h:mm a",
                    step=60,
                ),
            },
            hide_index=True,
        )

        text = st.text_area("Maydon matn kiritish uchun yaratilgan 👇")

        rang=st.color_picker("Ranglarni tanlang va ulardan foydalanib ko'ring:")

        ism=st.text_input("Ismingizni kiriting: 👇")

        date=st.date_input("Bugungi sana 👇")
        time=st.time_input("Hozirgi vaqt 👇")

        time=st.file_uploader("Mening faylim")
        choices=st.multiselect("Buy 👉", ["milk", "apples", "potatoes"])
        
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", "70 °F", "1.2 °F")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "86%", "4%")
        
        st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

        st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")
        
        prompt = st.chat_input("Xabar yuborish  📩")

        if prompt:
            st.text(f"Foydalanuvchi yuboradigan xabar 📃: {prompt}    ")
        
E=df[(df["CustomerGender"]==1.0)]
A=df[(df["CustomerGender"]==0.0)]


O=df[(df["PurchaseIntent"]==1.0)]
M=df[(df["PurchaseIntent"]==0.0)]



QismE = E["ProductBrand"].value_counts()
QismA = A["ProductBrand"].value_counts()
Qism1E = E["ProductCategory"].value_counts()
Qism1A = A["ProductCategory"].value_counts()




QismO = O["ProductBrand"].value_counts()
QismM = M["ProductBrand"].value_counts()
Qism1O = O["ProductCategory"].value_counts()
Qism1M = M["ProductCategory"].value_counts()
rostlik=st.toggle("Tovorlar haqida")
if rostlik:    
        Qism = df["ProductBrand"].value_counts()
        Qism1 = df["ProductCategory"].value_counts()

        plt.figure(figsize=(3, 4))
        plt.pie(Qism, labels=Qism.index, autopct='%1.1f%%', startangle=100)
        plt.title("Texnikaga bo'lgan talablarning taqsimlanilishi")
        plt.axis('equal')
        st.pyplot(plt)

        st.divider()
        plt.figure(figsize=(3, 4))
        plt.pie(Qism1, labels=Qism1.index, autopct='%1.1f%%', startangle=100)
        plt.title("Texnikaga turlari va uning ishlatilishi", loc="center")
        plt.axis('equal')
        st.pyplot(plt)

        st.divider()

        st.write("### Erkaklar va ayollarning texnika vositalarga qiziqishi")
        st.divider()

        plt.figure(figsize=(3, 4))
        plt.pie(QismE, labels=QismE.index, autopct='%1.1f%%', startangle=100)
        plt.title("Texnikaga bo'lgan talablarning taqsimlanilishi {Erkaklarda}")
        plt.axis('equal')
        st.pyplot(plt)
        plt.figure(figsize=(3, 4))
        plt.pie(QismA, labels=QismA.index, autopct='%1.1f%%', startangle=100)
        plt.title("Texnikaga bo'lgan talablarning taqsimlanilishi {Ayollarda}")
        plt.axis('equal')
        st.pyplot(plt)
        st.divider()

        st.write("### Erkaklar va ayollarning texnika brandlarga qiziqishi")

        st.divider()
        plt.figure(figsize=(3, 4))
        plt.pie(Qism1E, labels=Qism1E.index, autopct='%1.1f%%', startangle=100)
        plt.title("Texnikaga turlari va uning ishlatilishi  {Erkaklarda}", loc="center")
        plt.axis('equal')
        st.pyplot(plt)
        plt.figure(figsize=(3, 4))
        plt.pie(Qism1A, labels=Qism1A.index, autopct='%1.1f%%', startangle=100)
        plt.title("Texnikaga turlari va uning ishlatilishi  {Ayollarda}", loc="center")
        plt.axis('equal')
        st.pyplot(plt)
        st.divider()



        st.divider()

        st.write("### ")
        st.divider()
        st.write("### Insonlar orasida olmoqchi bo'lgan qandaydir brandga tegishli bo'lgan texnika vositalari % da")

        plt.figure(figsize=(3, 4))
        plt.pie(QismO, labels=QismO.index, autopct='%1.1f%%', startangle=100)
        plt.title("Texnikaga bo'lgan talablarning taqsimlanilishi {Olmoqchi}")
        plt.axis('equal')
        st.pyplot(plt)
        plt.figure(figsize=(3, 4))
        plt.pie(Qism1O, labels=Qism1.index, autopct='%1.1f%%', startangle=100)
        plt.title("Texnikaga turlari va uning ishlatilishi  {Olmoqchi}", loc="center")
        plt.axis('equal')
        st.pyplot(plt)
        st.divider()

        st.write("### Insonlar orasida olmoqchi bo'lmagan qandaydir brandga tegishli bo'lgan texnika vositalari % da")

        st.divider()
        plt.figure(figsize=(3, 4))
        plt.pie(QismM, labels=QismM.index, autopct='%1.1f%%', startangle=100)
        plt.title("Texnikaga turlari va uning ishlatilishi  {Olmoqchi emas}", loc="center")
        plt.axis('equal')
        st.pyplot(plt)
        plt.figure(figsize=(3, 4))
        plt.pie(Qism1M, labels=Qism1M.index, autopct='%1.1f%%', startangle=100)
        plt.title("Texnikaga bo'lgan talablarning taqsimlanilishi {Olmoqchi emas}")
        plt.axis('equal')
        st.pyplot(plt)
        st.divider()



# st.divider()
 
fig, ax = plt.subplots()
sns.histplot(df["CustomerSatisfaction"], ax=ax)
st.pyplot(fig)
st.divider()

fig, ax = plt.subplots()
sns.histplot(E["CustomerSatisfaction"], ax=ax)
st.pyplot(fig)
st.divider()

fig, ax = plt.subplots()
sns.histplot(A["CustomerSatisfaction"], ax=ax)
st.pyplot(fig)
st.divider()
st.area_chart(["CustomerSatisfaction"])
st.divider()


g = sns.catplot(x="ProductPrice", data=df, kind="box")
st.pyplot(g)
st.divider()


g=sns.catplot(x="CustomerAge", data=df, kind="box")
st.pyplot(g)
st.divider()

k=df[df["ProductID"]<5890]
fig, ax=plt.subplots()
ax.plot(k["CustomerAge"], k["ProductPrice"])
st.pyplot(fig)
st.divider()
fig, ax=plt.subplots()
ax.plot(df["CustomerAge"], df["ProductPrice"])
st.pyplot(fig)
st.divider()


st.text("Erkaklarlar olmoqchi bo'lgan tovorlar narxlari")
fig, ax=plt.subplots()
ax.plot(E["ProductPrice"])
st.pyplot(fig)
st.text("Ayollar olmoqchi bo'lgan tovorlar narxlari")
fig, ax=plt.subplots()
ax.plot(A["ProductPrice"])
st.pyplot(fig)
st.divider()

st.text("Erkaklar sotib olmoqchi bo'lgan tovarlar narxlari haqida1")

g=sns.catplot(x="ProductPrice", data=E, kind="box")
st.pyplot(g)
st.text("Ayollar sotib olmoqchi bo'lgan tovarlar narxlari haqida")
g=sns.catplot(x="ProductPrice", data=A, kind="box")
st.pyplot(g)
st.divider()


T=df[df["ProductID"]<5974]
fig, ax=plt.subplots()
ax.plot(T["PurchaseFrequency"], T["ProductPrice"])
st.pyplot(fig)
st.divider()

olishlik=st.toggle("Tovorlarni sotib olinilishi yoki olinmasligi haqidagi ma'lumotlarni ko'rish")
if olishlik:

    sns.relplot(data=T, x="PurchaseFrequency", y="ProductPrice", hue="PurchaseIntent", kind="scatter")
    st.pyplot(plt.gcf())

    st.divider()

    ET=E[E["ProductID"]<6074]
    sns.relplot(data=E, x="PurchaseFrequency", y="ProductPrice", hue="PurchaseIntent", kind="scatter")
    st.pyplot(plt.gcf())

    st.divider()

    sns.relplot(data=A, x="PurchaseFrequency", y="ProductPrice", hue="PurchaseIntent", kind="scatter")
    st.pyplot(plt.gcf())
    HP=df[(df["ProductBrand"]=="HP")]
    Samsung=df[(df["ProductBrand"]=="Samsung")]
    Sony=df[(df["ProductBrand"]=="Sony")]
    Apple=df[(df["ProductBrand"]=="HP")]
    OtherBrands=df[(df["ProductBrand"]=="HP")]
    Qism2 = HP["PurchaseIntent"].value_counts()
    Qism3 = Samsung["PurchaseIntent"].value_counts()
    Qism4 = Sony["PurchaseIntent"].value_counts()
    Qism5 = Apple["PurchaseIntent"].value_counts()
    Qism6 = OtherBrands["PurchaseIntent"].value_counts()
    plt.figure(figsize=(3, 4))
    plt.pie(Qism2, labels=Qism2.index, autopct='%1.1f%%', startangle=100)
    plt.title("HP brandi mahsulotlarining olinishi yoki olinmasligi", loc="center")
    plt.axis('equal')
    st.pyplot(plt)

    st.divider()
    plt.figure(figsize=(3, 4))
    plt.pie(Qism3, labels=Qism3.index, autopct='%1.1f%%', startangle=100)
    plt.title("Samsung brandi mahsulotlarining olinishi yoki olinmasligi", loc="center")
    plt.axis('equal')
    st.pyplot(plt)


    plt.figure(figsize=(3, 4))
    plt.pie(Qism4, labels=Qism4.index, autopct='%1.1f%%', startangle=100)
    plt.title("Sony brandi mahsulotlarining olinishi yoki olinmasligi", loc="center")
    plt.axis('equal')
    st.pyplot(plt)

    st.divider()
    plt.figure(figsize=(3, 4))
    plt.pie(Qism5, labels=Qism5.index, autopct='%1.1f%%', startangle=100)
    plt.title("Apple brandi mahsulotlarining olinishi yoki olinmasligi", loc="center")
    plt.axis('equal')
    st.pyplot(plt)

    plt.figure(figsize=(3, 4))
    plt.pie(Qism6, labels=Qism6.index, autopct='%1.1f%%', startangle=100)
    plt.title("Boshqa brandlar mahsulotlarining olinishi yoki olinmasligi", loc="center")
    plt.axis('equal')
    st.pyplot(plt)

    st.divider()
    EO=E[(E["ProductBrand"]=="HP")]
    AO=A[(A["ProductBrand"]=="Samsung")]
    Qism7 = EO["PurchaseIntent"].value_counts()
    Qism8 = AO["PurchaseIntent"].value_counts()
    plt.figure(figsize=(3, 4))
    plt.pie(Qism7, labels=Qism7.index, autopct='%1.1f%%', startangle=100)
    plt.title("Erkaklar mahsulotlarni sotib olishi yoki olmasligi", loc="center")
    plt.axis('equal')
    st.pyplot(plt)

    plt.figure(figsize=(3, 4))
    plt.pie(Qism8, labels=Qism8.index, autopct='%1.1f%%', startangle=100)
    plt.title("Ayollar mahsulotlarni sotib olishi yoki olmasligi", loc="center")
    plt.axis('equal')
    st.pyplot(plt)

    st.divider()