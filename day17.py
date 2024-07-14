import streamlit as st
import pandas as pd


def release_the_balloons():
    st.button("Tabriklayman!")
    st.balloons()

st.write("# Streamlitdagi birinchi loyiham !")
# release_the_balloons()

df = pd.read_csv("world_smoking_history_1924_2023.csv")


# st.write("## Tanlang:")
# country = st.radio(
#     label = "Chekish bo'yicha:",
#     options = ["Eng ko'p chekadigan davlat", 'Eng kam chekadigan davlat'],
#     index=None,
# )
# max= df[df.groupby('Country')['Smoking_Population_Percentage'].max().sort_values().max()==df["Smoking_Population_Percentage"]]["Country"].values[0]
# if st.button("ko'rsat"):
#     st.write("Eng ko'p chekadiganlar:", max)
#     # st.dataframe(max)
# with st.sidebar:
#     add_radio = st.radio(
#         "Tanlang:",
#         ("FataFrame", "Rasmlar")
#     )

# Sidebar with radio buttons
add_radio = st.sidebar.radio(
    "Tanlang:",
    ("DataFrame", "Statistika")
)

if add_radio == "DataFrame":
    st.title("DataFrame Sahifasi")
    if st.button("'DataFrame'ni ko'rish"):
        st.write("## DataFrame")
        st.dataframe(df)
        st.button("Yopish", type="primary")
    st.write("## Qaysi davlat bo'yicha ko'rmoqchisiz:")
    country = st.radio(
        label = "Countries",
        options = df['Country'].unique().tolist(),
        index=None,
    )
    if st.button("Jadvalni ko'rsat"):
        st.write("Siz tanlagan davlat:", country)
        st.dataframe(df[df["Country"]==country])
        st.button("Yopish", type="primary")
        
        
        
        
elif add_radio == "Statistika":
    st.title("Statistikaga aloqador rasmlar:")
    st.write("## Z-table")
    st.image("https://z-table.com/uploads/2/1/7/9/21795380/1426878678.png?ezimgfmt=rs:279x130/rscb1/ng:webp/ngcb1", caption='Z-table')
    st.write("## Z-table (manfiy qiymatlarga)")
    st.image("https://z-table.com/uploads/2/1/7/9/21795380/9340559_orig.png?ezimgfmt=rs%3Adevice%2Frscb1-10", caption='Z-table (manfiy)')

    st.write("## Z-table")
    st.image("/Users/macbookair/Desktop/IMAGE 2024-07-14 11:08:42.jpg", caption='Z-table')
    