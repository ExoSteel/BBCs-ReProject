import streamlit as st

if 'page' not in st.session_state:
    st.session_state['page'] = 1

st.set_page_config(page_title="Log In", page_icon="smile.png", layout="wide")

if st.session_state['page'] == 1:
    st.write("This is page one")
    if st.button("Next page"):
        st.session_state["page"] = 2
        st.rerun()
elif st.session_state["page"] == 2:
    st.write("This is page two")
    if st.button("Previous page"):
        st.session_state["page"] = 1
        st.rerun()

