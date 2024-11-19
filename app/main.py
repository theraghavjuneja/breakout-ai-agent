import streamlit as st
import pandas as pd
from langchain_community.utilities import SerpAPIWrapper
from llmsupportingcode import agent_executor
from concurrent.futures import ThreadPoolExecutor
import os
params = {
    "engine": "google",
    "gl": "in",
    "google_domain":"google.co.in",
    "hl": "en",
}

def ask_agent(question):
    return {"question": question, "answer": agent_executor.invoke({"input": question})}
def main():
    st.title("Answer Generator from Internet")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read CSV into a DataFrame
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded DataFrame:")
        st.dataframe(df)

        primary_column = st.selectbox("Select a primary column:", df.columns)
        custom_question = st.text_input(
            "Write your custom question (use {value} for dynamic insertion)",
            value="Who is the support email id of {value}?"
        )
        
        if primary_column and custom_question:
            st.write(f"Custom question template: **{custom_question}**")
            values = df[primary_column].dropna().unique()  # Ensure no NaN values
            question_list = [custom_question.format(value=val) for val in values]
            st.write("Generated Questions:")
            st.write(question_list)
            
            # Option to confirm if questions are correct
            questions_correct = st.radio(
                "Are all your questions correct?",
                options=["No", "Yes"],
                index=0
            )

            if questions_correct == "Yes":
                st.write("Processing questions...")
                with ThreadPoolExecutor() as executor:
                    results = list(executor.map(ask_agent, question_list))
                
                # Ask user for the name of the new column
                new_column_name = st.text_input(
                    "Enter the name for the new column containing the answers:",
                    value="Answer"
                )

                # Extract answers and create a new column in the DataFrame
                answers = [result['answer']['output'] for result in results]
                df[new_column_name] = answers

                # Display the updated DataFrame
                st.write(f"Updated DataFrame with '{new_column_name}' column:")
                st.dataframe(df)

                # Provide a download link for the updated CSV
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download Updated CSV",
                    data=csv,
                    file_name="updated_results.csv",
                    mime="text/csv"
                )

if __name__ == '__main__':
    main()