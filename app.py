import streamlit as st
import datetime
import pandas as pd

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Vamshi's AI Transition 2026", page_icon="🏏", layout="wide")

# --- CUSTOM INTERFACE THEME ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { background-color: #238636; color: white; border-radius: 10px; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #f59e0b; }
    h1, h2, h3 { color: #58a6ff; font-family: 'Helvetica'; }
    .metric-card { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- SYSTEM DATES ---
today = datetime.date(2026, 6, 1)
interview_start = datetime.date(2026, 10, 1)
final_goal = datetime.date(2026, 12, 31)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://img.icons8.com/fluency/96/cricket.png", width=80)
st.sidebar.title("🏆 Match Center")
nav = st.sidebar.radio("Sectors:", [
    "🏠 Dashboard", 
    "📅 7-Month Roadmap", 
    "🧠 Logic Lab (Cricket Ed.)",
    "💻 Coddy Interactive Hub",
    "💼 Interview & Job Vault", 
    "🗣️ English Fluency Pro"
])

# --- 1. DASHBOARD ---
if nav == "🏠 Dashboard":
    st.title("🚀 The Comeback Starts Now")
    st.write(f"Welcome back, Champion. It's **June 1, 2026**. The second innings of your career begins today.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Days to Interview Phase", (interview_start - today).days)
    with col2:
        st.metric("Days to Goal", (final_goal - today).days)
    with col3:
        st.metric("Daily Target", "2 Hours")

    st.markdown("---")
    st.header("🔥 Daily Dopamine Boost")
    st.success("> \"You don't need to see the whole staircase, just take the first step. Every line of code is a run on the board.\"")
    
    st.subheader("⚡ Concentration Mode: The T20 Session")
    st.write("Exhausted from the shift? Don't study for hours. Just do one 20-minute 'Over'.")
    if st.button("Start 20-Minute Focus Timer"):
        st.write("⏳ Timer Active. Put your phone away. Focus on the Logic Lab.")

# --- 2. 7-MONTH ROADMAP ---
elif nav == "📅 7-Month Roadmap":
    st.title("📅 The Championship Roadmap")
    st.info("Your plan from June 1st to December 31st, 2026.")
    
    data = {
        "Month": ["June", "July", "August", "September", "October", "November", "December"],
        "Focus": ["Python Logic & English", "SQL & Stats", "Machine Learning", "GenAI & Projects", "Applications & Interviews", "Mock Rounds", "Offer Letter"],
        "Phase": ["The Nets", "Middle Overs", "The Powerplay", "The Final Over", "The Trophy", "The Trophy", "The Trophy"]
    }
    st.table(pd.DataFrame(data))
    
    st.markdown("### 🎯 Critical Targets for June")
    st.write("- **Logic:** Solve 30 cricket-based Python problems.")
    st.write("- **English:** Record 5 minutes of yourself explaining AI concepts.")
    st.write("- **Project:** Finalize the dataset for your Sentiment-based Recommendation System.")

# --- 3. LOGIC LAB ---
elif nav == "🧠 Logic Lab (Cricket Ed.)":
    st.title("🧠 Logic Building Playground")
    st.write("Let's build your logic using the game you love. Logic is just 'IF this happens, THEN do that.'")
    
    st.subheader("Challenge: The Selection Logic")
    st.write("Write code to select an 'All-Rounder' who has a Strike Rate > 120 and Economy < 8.")
    
    st.code("""
def is_all_rounder(strike_rate, economy):
    if strike_rate > 120 and economy < 8:
        return "Selected"
    else:
        return "Keep Practicing"

# Test your logic
print(is_all_rounder(145, 7.2)) # Output: Selected
    """)
    
    st.markdown("### 🛠️ Problem Solving Technique: The 'DRS' Method")
    st.markdown("""
    - **D (Define):** What do I need? (e.g., A list of player runs)
    - **R (Refine):** What are the rules? (e.g., Add them all up)
    - **S (Solve):** Write the code ball-by-ball.
    """)

# --- 4. CODDY INTERACTIVE HUB (NEW TAB) ---
elif nav == "💻 Coddy Interactive Hub":
    st.title("💻 Gamified Learning Tracks (Roadmap-Synced)")
    st.write("Use this tab to pick up daily badges and coding streaks. These interactive links directly map to your monthly schedule:")
    
    st.markdown("---")
    
    # Month-by-Month Bite-sized Targets
    st.subheader("🏏 JUNE TARGET: Python Syntax & Logic Mastery")
    st.info("🎯 **Goal:** Complete basic arithmetic shortcuts, conditional structures, and iteration engines.")
    st.markdown("- 🔗 **[Coddy: Core Python Fundamentals Journey](https://coddy.tech/landing/python)** — Teaches variables, operators, loops, and list filtering step-by-step.")
    st.markdown("- 🔗 **[Coddy: Python Dictionary Masterclass](https://coddy.tech/courses/dictionary_in_python)** — Learn map structures to organize complex data points.")
    
    st.subheader("📊 JULY TARGET: Relational Databases & Data Manipulation")
    st.info("🎯 **Goal:** Learn how to clean data and link relational spreadsheets together.")
    st.markdown("- 🔗 **[Coddy: Pandas Analytics Module](https://coddy.tech/landing/python/courses)** — Crucial for learning tables, data filtering, and column arrays.")
    st.markdown("- 🔗 **[Coddy: Interactive SQL Track](https://coddy.tech/)** — Practice structure querying, aggregations, and tables joining live.")
    
    st.subheader("📈 AUGUST TARGET: Numerical Engineering & Core Vectors")
    st.info("🎯 **Goal:** Understand numerical tracking arrays before touching full predictive models.")
    st.markdown("- 🔗 **[Coddy: NumPy Fundamentals](https://coddy.tech/landing/python/courses)** — Build multidimensional data layouts for statistical equations.")
    
    st.subheader("🤖 SEPTEMBER TARGET: Machine Pipelines & API Delivery")
    st.info("🎯 **Goal:** Hook your programs up to web platforms and large models.")
    st.markdown("- 🔗 **[Coddy: Connecting APIs in Python](https://coddy.tech/landing/courses/api_in_python)** — Learn data ingestion protocols to supply real-time tracking streams.")
    st.markdown("- 🔗 **[Coddy: AI Prompt Engineering Gym](https://coddy.tech/)** — Structural training for directing LLM outputs cleanly.")
    
    st.subheader("💼 OCTOBER - DECEMBER TARGET: Strategic Interview Blitz")
    st.info("🎯 **Goal:** Crack algorithmic logic problems and data sorting hurdles.")
    st.markdown("- 🔗 **[Coddy: Python Technical Interview Series](https://coddy.tech/landing/python/courses)** — 12 core foundational scenarios frequently used by interview boards.")
    st.markdown("- 🔗 **[Coddy: Data Structures Playbook](https://coddy.tech/landing/python/courses)** — Implement structural data systems like Stacks and Arrays from scratch.")

# --- 5. INTERVIEW & JOB VAULT ---
elif nav == "💼 Interview & Job Vault":
    st.title("💼 Interview Preparation & Job Reminders")
    st.warning("Note: Job alerts and active tracking will unlock on October 1st, 2026.")
    
    st.subheader("Top Interview Topics (Must Master by Oct)")
    topics = [
        "Python: Memory management (Lists vs Generators)",
        "SQL: Joins and Aggregate functions",
        "ML: How to handle missing data",
        "GenAI: Difference between LLMs and Traditional NLP"
    ]
    for t in topics:
        st.checkbox(t)
        
    st.markdown("---")
    st.subheader("📈 Job Market Strategy")
    st.write("From Oct 1, we will target roles like: **Junior AI Engineer**, **Associate Data Scientist**, and **Product Analyst**.")

# --- 6. ENGLISH FLUENCY PRO ---
elif nav == "🗣️ English Fluency Pro":
    st.title("🗣️ Communication & Fluency")
    st.write("Your current English is clear enough to learn, but we need it 'Interview-Ready'.")
    
    st.info("💡 **Tip:** AI companies don't need perfect grammar; they need **clarity**. Practice explaining your project out loud.")
    
    st.subheader("The 2-Minute Drill")
    st.write("1. Pick a topic (e.g., 'What is a Loop?').")
    st.write("2. Record yourself on your phone for 2 minutes.")
    st.write("3. Listen to it. Correct one mistake. Repeat.")
    
    st.subheader("Tools for Accuracy")
    st.markdown("- **Grammarly:** For fixing spelling in your messages.")
    st.markdown("- **ELSA Speak:** For practicing technical pronunciation.")
