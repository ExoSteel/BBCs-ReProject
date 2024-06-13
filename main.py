# main page, description of website + who made it :-)

import streamlit as st

if 'page' not in st.session_state:
    st.session_state['page'] = 1
    st.session_state['organisation'] = None

st.set_page_config(page_title = "Surplus Manager|I10", page_icon = "us.png")

col1, col2 = st.columns(2, gap = "medium")

col1.image("us.png")

col2.title("SURPLUS MANAGER")
col2.markdown(":rainbow[made with love by I10 <3]")
col2.markdown("*a tool that aims to help out many cool people in Singapore!*")

col2.write("restaurants, food outlets, hotels, and supermarkets are one of the main contributors to the increased food waste in Singapore  (25% of all food passed through hotel kitchens are thrown out as food waste, dunkin donut example, 3.37 metric tons worth of food wasted across NTUC supermarket stores etc).")
col2.write("our project aims to distribute food surplus from distributors (restaurants, food outlets, supermarkets, hotels) to the recipients (homeless shelters, old folks home, food shelters) as quickly as possible. ")




