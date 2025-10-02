## Marketing Campaign Insights Generator 📈


An AI-powered web application that automatically analyzes marketing campaign data from a CSV file and generates a professional insights report using Google's Gemini API.This project was built to demonstrate a practical, end-to-end AI solution that solves a real business problem: automating data analysis to save time and uncover actionable insights.Replace the URL above with a link to your own screenshot after running the app.


✨ Features

- Easy Data Upload: Upload your marketing data as a CSV file directly in the browser.

- Automated Data Summary: Performs initial data analysis using Pandas to calculate descriptive statistics and correlations.

- AI-Powered Insights: Uses the Google Gemini API to interpret the data summary and generate qualitative insights.

- Professional Reporting: The AI generates a structured report with:

  - An Executive Summary
  
  - Key Insights in bullet points
  
  - Actionable Recommendations
  
- Interactive UI: A simple, clean, and user-friendly interface built with Streamlit.


🛠️ Tech Stack

- Language: Python

- Web Framework: Streamlit

- Data Analysis: Pandas

- AI Model: Google Gemini Pro


🚀 Setup and Installation

Follow these steps to get the application running on your local machine.

1. Clone the Repository

     git clone [(https://github.com/Gautamgiri798/Marketing-Campaign-Insights-Generator.git)]
   
    cd insights-generator

2. Create and Activate a Virtual Environment

   It's recommended to use a virtual environment to manage project dependencies.
   
   On macOS/Linux:python -m venv venv
   
        source venv/bin/activate
   On Windows:python -m venv venv
   
        venv\Scripts\activate
3. Install Dependencies

Install all the required libraries from the requirements.txt file.
   
     pip install -r requirements.txt
   
4. Set Up Your API Key

   The application requires a Google Gemini API key to function.
   
     - Create a file named .env in the root of the project directory.
   
   Add your API key to the .env file as follows:
   
       GOOGLE_API_KEY="your_google_api_key_goes_here"

You can get a free API key from Google AI Studio.


🏃‍♀️ How to Run the Application

With the setup complete, you can now run the Streamlit application.

  1. Make sure your virtual environment is activated.

  2. Run the following command in your terminal:

    streamlit run app.py
     
  4. Your web browser will open a new tab at http://localhost:8501.
 
  5. Upload the advertising.csv file (or any other marketing CSV) and click the "Generate Insights Report" button.
  

📂 Dataset

This project uses the "Advertising Spend" dataset from Kaggle as an example.

  - Link: Kaggle Advertising CSV
  
  - The advertising.csv file is included in this repository for convenience.
