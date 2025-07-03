import streamlit as st

# Page Config
st.set_page_config(page_title="Calculator by Ali Imran", page_icon="🧮")

# Title & Developer Name
st.markdown("<h1 style='text-align: center;'>🧮 Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Developed by: <span style='color: green;'>Ali Imran</span></h4>", unsafe_allow_html=True)

# Custom CSS for Button Styling
st.markdown("""
    <style>
    .stButton>button {
        font-size: 24px !important;
        font-weight: bold !important;
        color: black !important;
        height: 3em !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize expression
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Functions
def add_to_expression(val):
    st.session_state.expression += str(val)

def clear_display():
    st.session_state.expression = ""

def delete_last():
    st.session_state.expression = st.session_state.expression[:-1]

def evaluate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"

# Display screen
st.text_input("Display", value=st.session_state.expression, disabled=True, label_visibility="collapsed")

# Button layout with visible labels and actual values
buttons = [
    [("7", "7"), ("8", "8"), ("9", "9"), ("÷", "/")],
    [("4", "4"), ("5", "5"), ("6", "6"), ("×", "*")],
    [("1", "1"), ("2", "2"), ("3", "3"), ("−", "-")],
    [("0", "0"), (".", "."), ("=", "="), ("＋", "+")]  # Full-width PLUS for display
]

# Render Buttons
for row in buttons:
    cols = st.columns(4)
    for i, (label, value) in enumerate(row):
        if label == "=":
            cols[i].button(label, on_click=evaluate, use_container_width=True)
        else:
            cols[i].button(label, on_click=add_to_expression, args=(value,), use_container_width=True)

# Clear and Delete Buttons
col1, col2 = st.columns(2)
col1.button("🧹 Clear", on_click=clear_display, use_container_width=True)
col2.button("⌫ Delete", on_click=delete_last, use_container_width=True)

# End
st.markdown("---")
