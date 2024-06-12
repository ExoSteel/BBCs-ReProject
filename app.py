import streamlit as st
import numpy as np
import pandas as pd

if 'history' not in st.session_state:
    st.session_state['history'] = []

st.set_page_config(page_title="Coock", page_icon="pp.png", layout="wide",)

st.markdown(
    """
<style>
    @keyframes buttonhover {
        0% {background-color:rgb(255, 255, 255);}
        25% {background-color:rgb(38, 0, 255);}
        75% {background-color: yellow;}
        100% {background-color:rgb(0, 255, 55);}
    }
    [data-testid="stApp"] {
        animation: buttonhover 100ms infinite
    }
    
</style>
""",
    unsafe_allow_html=True,
)

st.title("what")
st.header("are")

st.subheader("you")
st.write("doing")

st.image("200px-Roger_Smith.png")

code = """
    #include <bits/stdc++>
    using namespace std;

    int main(){
        cout << "poop";
        return 0;
    }
"""

st.code(code, language="c++")


st.markdown("what?", unsafe_allow_html=False, help=None)

date = st.date_input("Date")
title = st.text_input("Test", "poopoo")
st.write(title, date)

st.slider("pp size",min_value=0.0,max_value=10.0,value=5.0,step=0.1)

radio = st.radio("what is wrong with you?",["yes","no","i told you so"])

map_data = pd.DataFrame(
    np.random.randn(100000, 2) * [4, 12],
    columns=['lat', 'lon'])

st.divider()
color = st.color_picker("Color", "#FF0000")
st.map(map_data, color=color)

df = pd.read_csv("biopsy.csv")

st.write(df.head(5))

st.area_chart(df, x="radius_mean", y="texture_mean")