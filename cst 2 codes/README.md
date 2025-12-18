🛡️ Project Setup: Cyber Incident Platform 🛡️
Welcome! This guide will help you get the Intelligent Intelligence Platform running on your computer. This code is built to meet Tier 1 (Pass/Merit) requirements for Weeks 7 through 11.

🛠️ Step 1: Technical Prerequisites
Before doing anything else, you need to install the "engines" that run the code. Open your terminal in PyCharm and run:

Bash

pip install streamlit pandas plotly openai bcrypt
Streamlit: Runs the website 🌐

Pandas: Manages the data tables 📊

Plotly: Creates the cool interactive charts 📈

Bcrypt: Encrypts passwords for security 🔐

OpenAI: Prepares the AI Assistant 🤖

📂 Step 2: File Organization
Make sure your folder looks exactly like this. Do not put the .py files inside subfolders!

home.py (The main website)

application.py (Login & Security logic)

models.py (The OOP Classes - Week 11)

db_setup.py (The Database creator)

🚀 Step 3: Launch Sequence
Follow these steps in order to avoid errors:

Create the Database: Run python3 db_setup.py.

You will see a new folder called DATA appear. This is where your info is saved.

Start the Web Server: Run python3 -m streamlit run home.py.

Register: Go to the Account tab in the browser, register a new user, and log in.

Add Data: Go to Cyber Incidents and report 3-4 incidents so the charts have data to show.

🎨 Step 4: MAKE IT YOUR OWN (Crucial!)
To avoid plagiarism flags, everyone MUST change these "Slight Variations":

📍 Variation A: Change the Names
Don't use "Intelligent Platform." In home.py, find the st.set_page_config line and change the title to something else:

Examples: "CyberGuard Pro", "Sentinel Analytics", "ThreatTracker 3000".

📍 Variation B: Change the Colors
In home.py, find the px.bar code. Change the color theme so your charts look different:

Find: color_continuous_scale='Reds'

Change to: 'Blues', 'Greens', 'Viridis', or 'Gold'.

📍 Variation C: Change the Incident Types
In db_setup.py and the dropdown menu in home.py, change the categories.

Instead of Phishing/Malware, use: "Ransomware", "Social Engineering", "Cloud Leak", or "API Breach".

❓ Troubleshooting
"Table not found" Error: You didn't run db_setup.py first!

"Module Not Found": You missed a library in Step 1. Run the pip install command again.

Empty Charts: You need to click the "Resolve" button on an incident to make the "Resolution Bottleneck" chart appear.