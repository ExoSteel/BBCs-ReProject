import streamlit as st

if 'page' not in st.session_state:
    st.session_state['page'] = 1
    st.session_state['organisation'] = None

st.set_page_config(page_title="Log In", page_icon="smile.png", layout="wide")

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
    pass

#Creating offers/requests
elif st.session_state['page'] == 4:
    pass