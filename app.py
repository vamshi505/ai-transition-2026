import streamlit as st
import datetime
import pandas as pd

# --- 1. GLOBAL APP CONFIGURATION ---
st.set_page_config(
    page_title="Vamshi's AI Transition Engine 2026", 
    page_icon="🏏", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THEMATIC STYLING (The "Dopamine" UI) ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { background-color: #238636; color: white; border-radius: 12px; font-weight: bold; width: 100%; border: none; transition: 0.3s; }
    .stButton>button:hover { background-color: #2ea043; transform: scale(1.02); }
    .stProgress > div > div > div > div { background-color: #f59e0b; }
    .sidebar .sidebar-content { background-color: #161b22; }
    h1, h2, h3 { color: #58a6ff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .card { background: linear-gradient(145deg, #161b22, #0d1117); padding: 20px; border-radius: 15px; border: 1px solid #30363d; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .roadmap-step { border-left: 3px solid #f59e0b; padding-left: 15px; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TIMELINE CALCULATIONS ---
today = datetime.date(2026, 6, 1)
interview_season = datetime.date(2026, 10, 1)
goal_deadline = datetime.date(2026, 12, 31)

# --- 4. SIDEBAR NAVIGATION ---
st.sidebar.markdown("# 🏏 VAMSHI'S MATCH DAY")
st.sidebar.info("🎯 Status: 7 Months to AI Engineer")
nav = st.sidebar.radio("Navigation Hub", [
    "🏠 Dashboard & Focus", 
    "📅 7-Month Roadmap", 
    "🏆 My Progress Scorecard",
    "🧠 Logic Lab (Cricket scenarios)",
    "💻 Gamified Coding Hub",
    "💼 Interview & Job Vault", 
    "🗣️ English & Communication"
])

# --- PAGE 1: DASHBOARD ---
if nav == "🏠 Dashboard & Focus":
    st.title("🚀 The 2026 Comeback Dashboard")
    st.write("Today is **June 1, 2026**. This is Day 1 of your new life. No more looking back at wasted time.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Days to Oct 1 Interviews", (interview_season - today).days)
    with col2:
        st.metric("Total Days Remaining", (goal_deadline - today).days)
    with col3:
        st.metric("Shift Resilience", "12H Done ✅")

    st.markdown("---")
    st.markdown("""
    <div class='card'>
        <h3>🔥 Mentor's Daily Fuel</h3>
        <p style='font-size: 1.15em; line-height: 1.6;'>
            "Vamshi, listen to me: You are 23. You have the energy of a young fast bowler. Your shift at Tech Mahindra is your fitness training. Your MTech is your strategy room. Most people would quit. The fact that you are here at 19:00 today makes you <b>dangerous</b> to the competition. Let's build that logic one ball at a time."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("⚡ Concentration Engine (Pomodoro)")
    st.write("Exhausted? Just give me 20 minutes. That's one high-intensity over.")
    if st.button("Start 20-Minute Study Over"):
        st.balloons()
        st.success("Timer Active. Silence your phone. Open Python. Let's go!")

# --- PAGE 2: ROADMAP ---
elif nav == "📅 7-Month Roadmap":
    st.title("📅 The Ultimate Career Roadmap")
    
    st.markdown("""
    <div class='card'>
    <h4>Phase 1: The Foundation (June - July)</h4>
    <p><b>Focus:</b> Python Logic, SQL, and English. Building the 'batter's stance'.</p>
    <div class='roadmap-step'>June: Variables, Loops, Conditionals, and Logical Operators.</div>
    <div class='roadmap-step'>July: SQL Joins, Pandas DataFrames, and Data Cleaning.</div>
    </div>
    
    <div class='card'>
    <h4>Phase 2: The Magical Science (August - September)</h4>
    <p><b>Focus:</b> Machine Learning & "Magical" AI (GenAI).</p>
    <div class='roadmap-step'>August: Linear/Logistic Regression, Random Forests, and Scikit-Learn.</div>
    <div class='roadmap-step'>September: Large Language Models (LLMs), Prompt Engineering, and Capstone Project.</div>
    </div>
    
    <div class='card'>
    <h4>Phase 3: The Match Day (October - December)</h4>
    <p><b>Focus:</b> Applications, Interviews, and Success.</p>
    <div class='roadmap-step'>Oct 1st: Interview Ready. Start applying to AI/ML startups and tech firms.</div>
    <div class='roadmap-step'>Nov-Dec: Mock interviews, refining the portfolio, and landing the offer.</div>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 3: PROGRESS TRACKER ---
elif nav == "🏆 My Progress Scorecard":
    st.title("🏆 My Progress Scorecard")
    st.write("Track your journey. As you check these off, you are earning your 'International Cap'.")
    
    with st.expander("✅ JUNE: The Opening Stand (Core Logic)"):
        j1 = st.checkbox("Variables & Basic Math (Strike Rate logic)")
        j2 = st.checkbox("If/Else & Comparison (Selection logic)")
        j3 = st.checkbox("For Loops (Over-by-over analysis)")
        j4 = st.checkbox("Lists & Dicts (Team roster management)")
        j5 = st.checkbox("Functions (Modular playbooks)")
    
    with st.expander("✅ JULY - AUGUST: The Middle Overs (Data & ML)"):
        m1 = st.checkbox("SQL: Selecting & Joining Tables")
        m2 = st.checkbox("Pandas: Data Cleaning (Removing bad balls)")
        m3 = st.checkbox("ML: Supervised Learning Foundations")
        m4 = st.checkbox("ML: Decision Trees & Predictions")
    
    with st.expander("✅ SEPTEMBER: Magical AI (GenAI Focus)"):
        s1 = st.checkbox("GenAI: Prompt Engineering")
        s2 = st.checkbox("LLMs: Building with OpenAI/Gemini APIs")
        s3 = st.checkbox("Capstone: Sentiment Recommendation System Finish")
    
    total_items = 12
    completed = sum([j1,j2,j3,j4,j5,m1,m2,m3,m4,s1,s2,s3])
    st.subheader(f"Overall Completion: {int((completed/total_items)*100)}%")
    st.progress(completed/total_items)

# --- PAGE 4: LOGIC LAB ---
elif nav == "🧠 Logic Lab (Cricket scenarios)":
    st.title("🧠 Logic Lab & Problem Solving")
    st.write("Improve your logic by relating it to the cricket field.")
    
    st.subheader("💡 Technique: The 'DRS' Method")
    st.markdown("""
    - **D (Define):** What do I have? (Runs, Balls)
    - **R (Refine):** What is the rule? (If runs > balls, aggressive batting)
    - **S (Solve):** Write the code step-by-step.
    """)
    
    st.subheader("Scenario: The Death Over Selection")
    st.write("Goal: Create a list of bowlers who conceded less than 10 runs in the last over.")
    st.code("""
bowlers = [
    {"name": "Siraj", "runs": 8},
    {"name": "Bumrah", "runs": 4},
    {"name": "Hardik", "runs": 12}
]

death_specialists = []

for b in bowlers:
    if b['runs'] < 10:
        death_specialists.append(b['name'])

print(death_specialists) # Output: ['Siraj', 'Bumrah']
    """)
    st.info("Logic Tip: Every complicated AI model is just a series of small 'If/Else' decisions. Master this, and you master AI.")

# --- PAGE 5: CODDY HUB ---
elif nav == "💻 Gamified Coding Hub":
    st.title("💻 Interactive Learning (Dopamine Centers)")
    st.write("Use these to keep your brain focused and excited.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🕹️ Gamified Practice")
        st.markdown("- **[Coddy.tech](https://coddy.tech/):** Interactive Python tracks.")
        st.markdown("- **[CheckiO](https://py.checkio.org/):** Code to save the world.")
        st.markdown("- **[Codewars](https://www.codewars.com/):** Rank up like a pro.")
    with col2:
        st.markdown("### 📘 Roadmap-Specific Modules")
        st.markdown("- **June Target:** [Python Basics on Coddy](https://coddy.tech/landing/python)")
        st.markdown("- **July Target:** [SQL Mastery on Coddy](https://coddy.tech/courses/sql)")

# --- PAGE 6: INTERVIEW VAULT ---
elif nav == "💼 Interview & Job Vault":
    st.title("💼 Interview Preparation & Job Alerts")
    st.info("From Oct 1, this tab will update with live job search strategies.")
    
    st.subheader("High-Level Interview Checklist")
    st.checkbox("Python: Difference between List and Tuple (Memory focus)")
    st.checkbox("Math: What is the Mean and Standard Deviation?")
    st.checkbox("ML: What is Overfitting and Underfitting?")
    st.checkbox("GenAI: What is a Large Language Model?")
    
    st.markdown("---")
    st.subheader("📡 Job Market Strategy")
    st.write("We will target roles for: **Junior AI Engineer, Data Analyst, Associate ML Developer**.")

# --- PAGE 7: ENGLISH ---
elif nav == "🗣️ English & Communication":
    st.title("🗣️ English Fluency Pro")
    st.write("Current Rating: **5/10** | Target: **8/10**")
    
    st.markdown("""
    <div class='card'>
        <h4>🚀 Today's English Drill (The 2-Minute Voice Record)</h4>
        <p>1. Open your phone's recorder.</p>
        <p>2. Explain the difference between an <b>Integer</b> and a <b>String</b> in English.</p>
        <p>3. Listen to it. Correct one word. Repeat once.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Concentration Tip")
    st.warning("Working 12-hour shifts creates 'Brain Fog'. Drink water, take a 5-minute walk, and then study for 20 minutes. Don't fight your body; work with it.")
