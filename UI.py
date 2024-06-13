import streamlit as st

st.set_page_config(page_title = "BBCS_i10", page_icon = " ")


sidebarChoice = st.sidebar.radio("Menu", ["Create Offer/Request", "View Offers/Requests", "Profile"])

if sidebarChoice == "Create Offer/Request":
    st.header("Login")
    st.text_input("Enter your username")


if sidebarChoice == "Profile":
    userType = st.selectbox(
        "Are you a distributor or a recipient?",
        ("Distributor", "Recipient"))
    
    if userType == "Recipient":
        userName = st.text_input("Username")
        address = st.text_input("Address")
        opHour = st.text_input("Opening Hours/Availability")
        dietaryPref = st.text_input("Dietary Preferences (Religious customs etc)")
        healthRest = st.text_input("Health Restrictions (Allergies etc)")

        st.button("Create Profile")

    elif userType == "Distributor":
        userName = st.text_input("Username")
        establishment = st.selectbox(
            "Select your type of organisation",
            ("Hotels/Restuarants", "Supermarkets"))
        
        if establishment == "Hotels/Restuarants":
            cuisine = st.selectbox(
                "What cuisine does your organisation mainly supply",
            ("N/A","Asian","Western","Others"))
            if cuisine == "Others":
              st.text_input("Enter cuisine type")

        address = st.text_input("Address")
        opHour = st.text_input("Opening Hours/Availability")

        st.button("Create Profile")