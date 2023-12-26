import streamlit as st
from dotenv import load_dotenv
from utils import query_agent
import pandas as pd

load_dotenv(override=True)

st.title("Let's do some analysis on your csv")
st.header("Please upload your csv file here:")

data = st.file_uploader("Upload CSV file", type="csv")

if data is not None:
    col1, col2 = st.columns([1,1])
    
    with col1:
        st.info("CSV Uploaded Successfully")
        dataframe_show = pd.read_csv(data)
        st.dataframe(dataframe_show, use_container_width=True)

    with col2:
        st.info("Chat with your csv below")
        
        query = st.text_area("Enter your query")
        button = st.button("Generate Response")
        if button:
            answer = query_agent(dataframe_show, query)
            st.write(answer)
    