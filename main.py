import streamlit as st
import pandas as pd
import numpy as np
import time

if 'page' not in st.session_state:
    st.session_state['page'] = 1
    st.session_state['organisation'] = 'recipient'
    st.session_state["x"] = False

st.set_page_config(page_title = "Surplus Manager|I10", page_icon = "us2.png")

foods_d = [
    ["pork", "T-Pork"],
    ["beef", "T-Beef"],
    ["mutton", "T-Mutton"],
    ["poultry", "T-Poultry"],
    ["fish", "T-Fish"],
    ["cabbage", "T-Cabbage"],
    ["lettuce", "T-Lettuce"],
    ["onions", "T-Onions"],
    ["potato", "T-Potato"],
    ["tomato", "T-Tomato"],
    ["broccoli", "T-Broccoli"],
    ["carrot", "T-Carrot"],
    ["cucumber", "T-Cucumber"],
    ["mushroom", "T-Mushroom"],
    ["rice", "T-Rice"],
    ["noodles", "T-Noodles"],
    ["egg", "T-Egg"],
    ["peanut", "T-Peanuts"],
    ["soy", "T-Soy"]]

foods_r = [
            ["pork"],
            ["beef"],
            ["mutton"],
            ["poultry"],
            ["fish"],
            ["cabbage"],
            ["lettuce"],
            ["onions"],
            ["potato"],
            ["tomato"],
            ["broccoli"],
            ["carrot"],
            ["cucumber"],
            ["mushroom"],
            ["rice"],
            ["noodles"],
            ["egg", "egg_A"],
            ["peanut","nut_A"],
            ["soy", "soy_A"],
        ]

def food_query_d(food):
    quantity = st.slider(
        f"How much {food[0]} will your organisation be donating? (kg)",
        0, 50, 25
    )
    expiration = str(st.date_input(f"Expiration date of {food[0]}?", key=food))
    return quantity, expiration

def food_query_r(food_lst):
            allergen_check = False
            quantity = st.slider(
            f"Quantity of {food_lst[0]} required by your organisation? (kg)",
                0, 50, 25
            )
            if len(food_lst) > 1:
                allergen_check = st.checkbox(f"Do members of your organisation have an allergy to {food_lst[0]}?",value=False,key=food_lst[0])
            if allergen_check:
                allergy_quantity = st.slider(f"How many members of your organsation are allergic to {food_lst[0]}?",
                1, 10000, 5000)
            else:
                allergy_quantity = 0
            return quantity, allergy_quantity

if st.session_state['page'] == 1: # Log In page
    st.header("Login Page")
    userName = st.text_input("Organisation Name")
    password = st.text_input("Password")

    col = st.columns(2)
    with col[0]:
        if st.button("Sign Up"):
            st.session_state["page"] = 2
            st.rerun()
    with col[1]:
        if st.button("Confirm"):
            st.session_state["page"] = 3
            st.rerun()
    
elif st.session_state["page"] == 2: # Sign Up page
    st.write("Sign Up")
    userType = st.selectbox(
        "Are you a distributor or a recipient?",
        ("Distributor", "Recipient"))
    
    if userType == "Recipient":
        st.session_state['organisation'] = "recipient"
        userName = st.text_input("Organisation Name")
        establishment = st.selectbox(
            "Organisation Type:",
            ("Old Folk's Home", "Homeless Shelter", "Animal Shelter"))
        address = st.text_input("Address")
        street = st.text_input("Street")
        opHour = st.text_input("Opening Hours/Availability")
        noOfRec = st.slider("Number of beneficiaries", 1, 100)
        

    elif userType == "Distributor":
        st.session_state['organisation'] = "distributor"
        userName = st.text_input("Organisation Name:")
        establishment = st.selectbox(
            "Organisation Type:",
            ("Hotels/Restuarants", "Supermarkets"))

        address = st.text_input("Address")
        street = st.text_input("Street")
        opHour = st.text_input("Opening Hours/Availability")
    st.write()
    if st.button("Sign Up"):
        st.session_state["page"] = 3
        st.rerun()

# Main Page
elif st.session_state['page'] == 3:

    col1, col2 = st.columns(2, gap = "medium")

    col1.image("us.png")

    col2.title("SURPLUS MANAGER")
    col2.markdown(":rainbow[made with love by I10 <3]")
    col2.markdown("*a tool that aims to help out many cool people in Singapore!*")

    col2.write("restaurants, food outlets, hotels, and supermarkets are one of the main contributors to the increased food waste in Singapore  (25% of all food passed through hotel kitchens are thrown out as food waste, dunkin donut example, 3.37 metric tons worth of food wasted across NTUC supermarket stores etc).")
    col2.write("our project aims to distribute food surplus from distributors (restaurants, food outlets, supermarkets, hotels) to the recipients (homeless shelters, old folks home, food shelters) as quickly as possible. ")

    # butt ons
    if st.session_state['organisation'] == 'distributor':
        display = "Donate"
    else:
        display = "Request"
    
    if st.session_state["x"] == True:
        @st.experimental_dialog("Linked! ✨✨✨✨✨✨✨")
        def terrible():
            st.header("Congrats! You are now Linked with Pastamania Singapore")
            map_data = pd.DataFrame(
                [[1.363, 103.8502],[1.363, 103.8502]],
                columns=['lat', 'lon']
            )

            st.divider()
            color = st.color_picker("Color", "#FF0000")
            st.map(map_data, color=color)
            if st.button("Okay"):
                st.session_state["x"] = False
                st.rerun()
        terrible()

    if col1.button(display):
        st.session_state['page'] = 4
        st.rerun()
        
    
#Creating offers/requests
elif st.session_state['page'] == 4:
    st.header("TICKET")

    if st.session_state['organisation'] == 'distributor':

        for i in range(len(foods_d)):
            option = st.selectbox(
                f"Is {foods_d[i][0]} part of your package?",
                ("nuh uh", "yuh uh")
            )
            if option == "yuh uh":
                quantity, expiration = food_query_d(foods_d[i][0])
            st.divider()

        
    elif st.session_state['organisation'] == 'recipient':
        st.session_state["x"] = True
        for i in range(len(foods_r)):
            option = st.selectbox(
                f"Does your organisation require {foods_r[i][0]}?",
                ("nuh uh", "yuh uh")
            )
            if option == "yuh uh":
                quantity, allergy_quantity = food_query_r(foods_r[i])
            st.divider()

    if st.button("Submit ticket"):
        st.session_state["page"] = 3
        st.rerun()
    