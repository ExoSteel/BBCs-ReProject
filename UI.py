import streamlit as st

st.set_page_config(page_title = "BBCS_i10", page_icon = " ")


sidebarChoice = st.sidebar.radio("Menu", ["Create Offer/Request", "View Offers/Requests", "Profile"])

#Profile choice
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

        address = st.text_input("Address")
        opHour = st.text_input("Opening Hours/Availability")

        st.button("Create Profile")

#Creating offers/requests
if sidebarChoice == "Create Offer/Request":
    st.header("Submitting a ticket")
    userType = st.selectbox(
        "Are you a distributor or a recipient?",
        ("Distributor", "Recipient"))
    userName = st.text_input("Enter username")
    st.write("Do not have an account? Create one in the profile tab")

    establishment = st.selectbox(
        "Type of organisation",
    ("Hotels/Restaurants","Supermarkets"))

    if userType == "Recipient":
        noOfRec = st.slider("Number of beneficiaries", 1, 50)

    elif userType == "Distributor":
        if establishment == "Hotels/Restaurants":
            foodName = st.text_input("Enter name of food")
            foodType = st.selectbox(
                "What are you donating",
            ("raw ingredients","cooked/baked goods"))

            if foodType == "raw ingredients":
                ingredient = st.selectbox(
                    "Enter ingredients you will be donating",
                ("Veg","Fruit","Meat","Wheat","Dairy","Others"))

            elif foodType == "cooked/baked goods":
                allergens = st.text_input("Enter any common allergens in the dish")

        elif establishment == "Supermarkets":
            foodName = st.text_input("Enter name of food")

        expire = st.text_input("Enter expiration date/best by date")
        qty = st.slider("Quantity of food supplied",1,50)
        fridge = st.checkbox("Requires refridgeration?")

    st.button("Submit ticket")