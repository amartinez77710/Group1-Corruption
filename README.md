# Village of Cuba Financial Dashboard

A Streamlit dashboard built from the two supplied MATLAB scripts.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. (Recommended) Create and activate a virtual environment.
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

The app opens in your browser, usually at http://localhost:8501.

## App contents

- **Financial Statement**: displays the 11 financial statement rows and the 2021–2025 plus Total columns from `net.m`. It also provides a selectable grouped bar chart.
- **Water & Sewer**: displays the revenue-versus-expense chart, annual operating-loss chart, summary metrics, and data table from `Graph_Cuba.m`.

The values are transcribed from the supplied MATLAB files into Python dataframes, so MATLAB is not required to run the Streamlit app.
