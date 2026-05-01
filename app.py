import streamlit as st #build interactive web app
import pdfplumber# to read pdf file via upload by user
from docx import Document#to read word or .doc file via upload by user
from pptx import Presentation#to read pptx file via upload by user
import anthropic  # to call Claude API


##let's start
st.set_page_config(
    page_title="studysandwhich",
    page_icon="🥪"
)
st.markdown("<h1 style='text-align: center;'>StudySandwhich🥪</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
    .stApp,[data-testid = "stAppViewContainer"],[data-testid="stHeader"] {
        background-color:#FDF6EC;       
    }
    .stButton button{
         background-color:#A0522D}  
    .stSlider [data-baseweb="slider"] [role="slider"] {
    background-color: #A0522D;
}             
    </style>
""", unsafe_allow_html=True)
st.markdown("*StudySandwich wraps up your study topics between two slices — upload your notes, pick your range, and enjoy every bite of knowledge!🥪📖*")
col1,col2=st.columns(2)
with col2:
  if st.button("let's start study"):
    st.switch_page("pages/quiz.py")

