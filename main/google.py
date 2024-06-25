import streamlit as st

# create the key "sayings" if it doesn't exist
if 'sayings' not in st.session_state:
    st.session_state['sayings'] = []

# for convenience, make a reference
sayings = st.session_state['sayings']

st.title("Take input from the user")
user_input = st.text_input("Say something:")

if sayings:
    # display "sayings" if it has inputs from previous runs
    st.write("You previously said:", sayings)

if user_input:
    # add to "sayings" if we get an input
    sayings.append(user_input)
    st.write("You said:", user_input)
