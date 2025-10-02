import streamlit as st
import pandas as pd
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# --- 1. API Configuration & Model Initialization ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Gemini client if the key exists
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    # Initialize the Generative Model (using a stable, widely available model)
    model = genai.GenerativeModel('gemini-pro')
else:
    model = None

# --- 2. Core Functions ---

def get_data_summary(df: pd.DataFrame) -> str:
    """
    Analyzes a Pandas DataFrame and returns a string summary including shape,
    columns, descriptive statistics, and correlation.
    """
    summary_parts = []
    
    # Basic info
    summary_parts.append(f"### Data Overview\n- The dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
    summary_parts.append(f"- Column Names: {', '.join(df.columns)}")
    
    # Descriptive Statistics
    summary_parts.append("\n### Descriptive Statistics\n```\n" + df.describe().to_string() + "\n```")
    
    # Correlation Matrix for numeric columns
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        summary_parts.append("\n### Correlation Matrix\n```\n" + numeric_df.corr().to_string() + "\n```")
    
    return "\n".join(summary_parts)

def generate_insights_report(data_summary: str) -> str:
    """
    Sends the data summary to the Gemini API to generate insights and recommendations.
    """
    if not model:
        return "Google API key is not configured. Please set it in your .env file."
        
    prompt = f"""
    You are a senior marketing data analyst. Your task is to analyze the following data summary from a marketing campaign and generate a concise, professional report for a business executive.

    **Data Summary Provided:**
    {data_summary}

    **Your Report Must Contain:**
    1.  **Executive Summary:** A brief, high-level overview of the key findings in 2-3 sentences.
    2.  **Key Insights:** 3-4 bullet points detailing the most significant trends or relationships found in the data (e.g., "TV advertising spend shows the strongest correlation with sales.").
    3.  **Actionable Recommendations:** Two concrete, data-driven recommendations for the marketing team to optimize future ad spend.

    Structure your response clearly with these headings. Be direct and focus on business impact.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred with the Google Gemini API: {e}"

# --- 3. Streamlit User Interface ---

st.set_page_config(page_title="Marketing Insights Generator", layout="wide", page_icon="📈")

st.title("📈 Marketing Campaign Insights Generator")
st.markdown("Upload your marketing campaign data as a CSV file to get instant, AI-powered insights.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        
        st.header("Data Preview")
        st.dataframe(df.head())
        
        # Button to trigger the analysis
        if st.button("🚀 Generate Insights Report"):
            if not model:
                st.error("Google API key is not configured. Please add it to your .env file.")
            else:
                with st.spinner("Analyzing data and crafting your report..."):
                    # Step 1: Get data summary
                    summary = get_data_summary(df)
                    
                    # Step 2: Generate insights report from the summary
                    report = generate_insights_report(summary)
                    
                    # Step 3: Display the final report
                    st.header("Your AI-Generated Marketing Report")
                    st.markdown(report)
                    
                    # Optional: Show the raw summary in an expander
                    with st.expander("See the Raw Data Summary Used by the AI"):
                        st.markdown(summary)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")

else:
    st.info("Awaiting for a CSV file to be uploaded.")