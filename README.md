# AI Agent for Answering Questions from CSV

This project is an AI agent designed to answer questions based on the content of an uploaded CSV file. The agent works by performing parallel Google searches using the Serper API, React Agent, and parallel processing techniques.

## Prerequisites

Before running the project, make sure you have the following:

1. **API Key for Serper API**:  
   - Visit [https://serpapi.com/](https://serpapi.com/) to get your API key.
   - Once you have the API key, create a `.env` file in the root directory of the project and add your key.

2. **API Key for Llama Model**:  
   - For using the Llama model, visit [https://console.groq.com/](https://console.groq.com/) to get your API key.
   - Add this API key in your `.env` file as well.

   Note: You can also try integrating **Serper.dev** or **TavilySearchResult** (from the list of available tools) to evaluate which performs better for your specific needs.

## Installation

1. Clone the repository or download the project files.
2. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt

## Running the Project

### Option 1: Running from `app` directory

Navigate to the `app` directory and run:
streamlit run main.py
or streamlit run app\main.py 
Important Notes
Ensure you have added your API keys correctly in the .env file.
Make sure you are connected to the internet as the project relies on Google searches and API calls.
You can experiment with Serper.dev or TavilySearchResult as search engines to determine which performs better for your use case.
Project Video
For a demo and further instructions, check out the project video on Loom:
## Project Video

For a demo and further instructions, check out the project video on Loom:

[**Project Video**](https://www.loom.com/share/a3c982e854644d3d9c20a6daa2263057)

