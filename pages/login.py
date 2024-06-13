import streamlit as st

if 'page' not in st.session_state:
    st.session_state['page'] = 1
    st.session_state['organisation'] = None

st.set_page_config(page_title="Log In", page_icon="smile.png", layout="wide")

if st.session_state['page'] == 1:
    st.Header("Login Page")
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
        st.session_state["page"] = 2
        st.rerun()
elif st.session_state["page"] == 2:
    st.write("This is page two")
    if st.button("Previous page"):
        st.session_state["page"] = 1
        st.rerun()


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