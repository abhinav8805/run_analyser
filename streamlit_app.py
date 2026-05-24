import streamlit as st
from langchain.messages import SystemMessage, HumanMessage
from main import model, prompt

st.set_page_config(page_title="Running Analyzer", page_icon="🏃")

st.title("🏃 AI Running Performance Analyzer")

st.text("lowkey better than strava premium")

runner_info = st.text_area(
    "Enter Runner Info",
    height=300
)

if st.button("Analyze Run"):

    if runner_info.strip() == "":
        st.warning("Please enter runner data.")

    else:
        with st.spinner("Analyzing..."):

            messages = [
                SystemMessage(prompt),
                HumanMessage(runner_info)
            ]
            import re

            response = model.invoke(messages)

            cleaned_response = re.sub(
                r"<think>.*?</think>",
                "",
                response.content,
                flags=re.DOTALL
            ).strip()

            st.markdown(cleaned_response)