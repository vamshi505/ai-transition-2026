import streamlit as st
import datetime
import pandas as pd
import time
import os

# --- 1. STADIUM ARCHITECTURE & CONFIG ---
st.set_page_config(
    page_title="VAMSHI'S AI STADIUM 2026",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE "MAXIMUM EFFORT" CUSTOM UI (NEON CRIMSON & CHARCOAL) ---
st.markdown("""
    <style>
    /* Full Stadium Dark Mode */
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #000000 100%);
        color: #f8fafc;
    }
    
    /* Neon Red Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0d0101 !important;
        border-right: 3px solid #e23636;
    }
    
    /* Interactive Stadium Cards */
    .stadium-card {
        background: linear-gradient(135deg, #2d0a0a 0%, #0d0202 100%);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #e23636;
        box-shadow: 0 0 30px rgba(226, 54, 54, 0.4);
        margin-bottom: 25px;
    }

    .video-box {
        background-color: #0b0f19;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #3b82f6;
        margin-top: 10px;
    }

    /* Professional Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #e23636 0%, #7f1d1d 100%);
        color: #ffffff !important;
        border: 1px solid #ffffff !important;
        border-radius: 40px !important;
        padding: 15px 30px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        transition: 0.4s all ease-in-out !important;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 0 40px rgba(226, 54, 54, 0.8);
    }
    
    h1, h2, h3, h4 {
        color: #e23636;
        font-family: 'Impact', 'Arial Black', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .gold {
        color: #fbbf24;
        text-shadow: 0 0 15px rgba(251, 191, 36, 0.8);
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PERSISTENT SYSTEM MEMORY ---
if 'streak' not in st.session_state: st.session_state.streak = 1
if 'runs' not in st.session_state: st.session_state.runs = 0
if 'chat_log' not in st.session_state: st.session_state.chat_log = []

# --- 4. CALENDAR ANCHORS ---
today = datetime.date(2026, 6, 1)
interview_season = datetime.date(2026, 10, 1)
goal_deadline = datetime.date(2026, 12, 31)

# --- 5. SIDEBAR: THE DUGOUT ---
st.sidebar.markdown("<h1 style='text-align: center; color: #e23636;'>⚔️ DEADPOOL</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'><b>BATSMAN: VAMSHI ALL-ROUNDER</b></p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown(f"🔥 **Win Streak:** `{st.session_state.streak} Matches`")
if st.sidebar.button("🏏 LOG PRACTICE INNINGS"):
    st.session_state.streak += 1
    st.sidebar.success("Innings saved to the board!")

nav_choice = st.sidebar.radio("CHOOSE SECTOR:", [
    "🏟️ The Pavilion (Dashboard)",
    "📅 7-Month Roadmap",
    "📊 Master Scorecard (37 Points)",
    "🧠 The Coding Nets (Logic Lab)",
    "💬 Chat with Deadpool (AI Mode)",
    "🗣️ Professional English Tuner"
])

# --- 6. SECTOR: THE PAVILION (DASHBOARD) ---
if nav_choice == "🏟️ The Pavilion (Dashboard)":
    st.title("🏟️ Main Command Pavilion")
    st.write("Wankhede Stadium, June 1st. Time to make a legendary comeback.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='stadium-card'><h5>Days to Finals (Oct 1)</h5><h2 class='gold'>{(interview_season - today).days}</h2></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='stadium-card'><h5>Current Rank</h5><h2 style='color: #3b82f6;'>Rookie All-Rounder</h2></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='stadium-card'><h5>Total Runs</h5><h2 style='color: #10b981;'>{st.session_state.runs}</h2></div>", unsafe_allow_html=True)

    st.subheader("🔋 Energy Recovery (After 12H Shift)")
    energy = st.select_slider("How is your human battery right now?", options=["0%", "25%", "50%", "100%"])
    
    if "0%" in energy:
        st.error("🚨 OVERLOAD. Do not code. Talk to Deadpool or do a vocal drill, then sleep.")
    elif "100%" in energy:
        st.success("🔥 POWERPLAY! Open 'The Nets' and crush a logic problem.")

    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #e23636;'>⚔️ Deadpool's Voice</h3>
        <p>"Vamshi, listen to me. Most people quit after a 4-hour shift. You do 12. That means you have the heart of a champion. 
        Don't let a missing variable or a 404 error stop you. We are building an AI engineer here, not a taco stand. 
        <b>Maximum Effort!</b>"</p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. SECTOR: 7-MONTH ROADMAP ---
elif nav_choice == "📅 7-Month Roadmap":
    st.title("📅 The 2026 Season Schedule")
    
    st.markdown("""
    <div class='stadium-card'>
        <h3>🏏 PHASE 1: THE NETS PRACTICE (June - July)</h3>
        <p><b>Focus:</b> Python Logic, SQL, and Data Handling.</p>
        <p><i>June:</i> Variables, Loops, If/Else, and Functions.<br><i>July:</i> SQL Queries, Joins, and Pandas DataFrames.</p>
    </div>
    <div class='stadium-card'>
        <h3>🎯 PHASE 2: THE MID-OVER EXPLOSION (August - September)</h3>
        <p><b>Focus:</b> Machine Learning & Magical AI (GenAI).</p>
        <p><i>August:</i> Regression, Decision Trees, and Model Metrics.<br><i>September:</i> Transformers, LLMs, Gemini APIs, and Capstone Project.</p>
    </div>
    <div class='stadium-card'>
        <h3>🏆 PHASE 3: THE WORLD CUP FINALS (October - December)</h3>
        <p><b>Focus:</b> Job Applications & Interviews.</p>
        <p><i>October 1:</i> Launch applications. Review Data Structures.<br><i>Nov-Dec:</i> Clear technical panels and land the Offer Letter.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 8. SECTOR: MASTER SCORECARD (ALL 37 POINTS) ---
elif nav_choice == "📊 Master Scorecard (37 Points)":
    st.title("📊 Complete 37-Point Mastery Tracker")
    st.write("Every single milestone from June to December. Check them off as you score.")

    # JUNE (10 POINTS)
    with st.expander("📅 JUNE: Python Core Foundations"):
        j1 = st.checkbox("Variable Memory & Object Naming")
        j2 = st.checkbox("Data Types (Int, Float, String, Bool)")
        j3 = st.checkbox("Comparison Operators (==, !=, >)")
        j4 = st.checkbox("Logical Operators (AND, OR, NOT)")
        j5 = st.checkbox("If, Elif, Else branches")
        j6 = st.checkbox("For Loops (Definite Sequences)")
        j7 = st.checkbox("While Loops (Indefinite Constraints)")
        j8 = st.checkbox("Python Lists (Indexing & Slicing)")
        j9 = st.checkbox("Python Dictionaries (Key-Value Maps)")
        j10 = st.checkbox("Functional Programming (Returns & Scopes)")
        st.markdown("<div class='video-box'>📺 <a href='https://www.youtube.com/results?search_query=freecodecamp+python' target='_blank'>June Masterclass</a></div>", unsafe_allow_html=True)

    # JULY (7 POINTS)
    with st.expander("📅 JULY: SQL & Data Processing"):
        jy1 = st.checkbox("Relational Database Schemas")
        jy2 = st.checkbox("SELECT, WHERE, and LIKE filters")
        jy3 = st.checkbox("INNER JOIN and LEFT JOIN")
        jy4 = st.checkbox("GROUP BY and HAVING Aggregates")
        jy5 = st.checkbox("Pandas Series and DataFrames")
        jy6 = st.checkbox("Data Cleaning (Dropna / Fillna)")
        jy7 = st.checkbox("Handling Duplicate Records")
        st.markdown("<div class='video-box'>📺 <a href='https://www.youtube.com/results?search_query=freecodecamp+sql' target='_blank'>July Masterclass</a></div>", unsafe_allow_html=True)

    # AUGUST (7 POINTS)
    with st.expander("📅 AUGUST: Machine Learning Algorithms"):
        a1 = st.checkbox("Linear Regression (Continuous Outputs)")
        a2 = st.checkbox("Logistic Regression (Binary Selection)")
        a3 = st.checkbox("Decision Trees & Node Splitting")
        a4 = st.checkbox("Random Forest Ensembles")
        a5 = st.checkbox("Train-Test Data Splitting")
        a6 = st.checkbox("Accuracy, Precision, and Recall math")
        a7 = st.checkbox("Confusion Matrix Visualization")
        st.markdown("<div class='video-box'>📺 <a href='https://www.youtube.com/results?search_query=statquest+machine+learning' target='_blank'>August Masterclass</a></div>", unsafe_allow_html=True)

    # SEPTEMBER (7 POINTS)
    with st.expander("📅 SEPTEMBER: Generative AI & Capstone"):
        s1 = st.checkbox("Neural Networks & Activation Layers")
        s2 = st.checkbox("Transformer Mechanics (Attention)")
        s3 = st.checkbox("Ingesting LLM APIs (Gemini/OpenAI)")
        s4 = st.checkbox("Prompt Engineering (System Persona)")
        s5 = st.checkbox("Capstone: Sentiment Recommendation Layout")
        s6 = st.checkbox("Capstone: Feature Vector Construction")
        s7 = st.checkbox("Capstone: Live Deployment on Cloud")
        st.markdown("<div class='video-box'>📺 <a href='https://www.youtube.com/results?search_query=andrej+karpathy+llm' target='_blank'>September Masterclass</a></div>", unsafe_allow_html=True)

    # OCT-DEC (6 POINTS)
    with st.expander("📅 OCTOBER - DECEMBER: Placements"):
        o1 = st.checkbox("Linear & Binary Search algorithms")
        o2 = st.checkbox("Bubble Sort & Merge Sort logic")
        o3 = st.checkbox("HashMaps and Problem Solving")
        o4 = st.checkbox("Resume: Tech Mahindra ➔ AI Engineer")
        o5 = st.checkbox("GitHub Portfolio Documentation")
        o6 = st.checkbox("Live Coding Interview Mocks")
        st.markdown("<div class='video-box'>📺 <a href='https://www.youtube.com/results?search_query=coding+interview+prep' target='_blank'>Placement Masterclass</a></div>", unsafe_allow_html=True)

    st.markdown("---")
    checked = j1+j2+j3+j4+j5+j6+j7+j8+j9+j10+jy1+jy2+jy3+jy4+jy5+jy6+jy7+a1+a2+a3+a4+a5+a6+a7+s1+s2+s3+s4+s5+s6+s7+o1+o2+o3+o4+o5+o6
    st.subheader(f"Overall Season Progress: {int((checked/37)*100)}%")
    st.progress(checked/37)

# --- 9. SECTOR: THE CODING NETS (LOGIC LAB) ---
elif nav_choice == "🧠 The Coding Nets (Logic Lab)":
    st.title("🧠 The Logic Training Nets")
    st.write("Master algorithmic thinking through cricket rules.")
    
    st.subheader("Challenge: The Milestone Selection Logic")
    st.code("""
# Scenario: A batsman scores runs. 
# Logic: If runs >= 50 and balls < 30, it is an "Explosive" inning.
# If runs >= 50 but balls >= 30, it is a "Solid" inning.
# Else, "Keep Playing".

runs = 52
balls = 25

if runs >= 50 and balls < 30:
    print("Explosive")
elif runs >= 50:
    print("Solid")
else:
    print("Keep Playing")
    """, language="python")
    
    guess = st.text_input("What exact word will print on the screen?")
    if st.button("Submit Decision (DRS)"):
        if guess.strip() == "Explosive":
            st.balloons()
            st.success("🎯 BOUNDARY! 52 runs in 25 balls is Explosive. +10 Runs!")
            st.session_state.runs += 10
        else:
            st.error("❌ Dot Ball. Read the logic again. Is 25 less than 30? Yes!")

# --- 10. SECTOR: LIVE CHAT WITH DEADPOOL (DIRECT API MODE) ---
elif nav_choice == "💬 Chat with Deadpool (AI Mode)":
    st.title("💬 Talk to Deadpool (Direct Access)")
    st.write("No more distractions. Just you and me. Ask anything—cricket, code, or life.")
    
    # SAFE SECRETS MODE
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("🚨 DEADPOOL DISCONNECTED! I need my brain fuel (The API Key).")
        st.markdown("""
        ### How to connect Deadpool in 10 seconds:
        1. Open **[Streamlit Cloud](https://share.streamlit.io/)**.
        2. Click the **3 dots** next to your app and select **Settings**.
        3. Go to **Secrets**.
        4. Paste this: `GEMINI_API_KEY = "PASTE_YOUR_KEY_HERE"`
        5. Save and refresh this page.
        """)
        st.info("Get a free key here: [Google AI Studio](https://aistudio.google.com/app/apikey)")
    else:
        try:
            import google.generativeai as live_ai
            live_ai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            llm = live_ai.GenerativeModel('gemini-1.5-flash')
            
            user_msg = st.chat_input("What's on your mind, Vamshi?")
            
            if user_msg:
                st.session_state.chat_log.append(f"Vamshi: {user_msg}")
                persona = f"You are Deadpool, Vamshi's sarcastic but brilliant AI mentor. Be funny, use cricket talk, and motivate him. He is 23 and works at Tech Mahindra. Question: {user_msg}"
                res = llm.generate_content(persona)
                st.session_state.chat_log.append(f"Deadpool ⚔️: {res.text}")

            for m in st.session_state.chat_log:
                if m.startswith("Vamshi:"): st.write(f"🧑 **{m}**")
                else: st.markdown(f"<div class='stadium-card' style='border-left: 5px solid #e23636;'>🔴 <b>{m}</b></div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Chimichangas! Something broke: {str(e)}")

# --- 11. SECTOR: PROFESSIONAL ENGLISH TUNER ---
elif nav_choice == "🗣️ Professional English Tuner":
    st.title("🗣️ The Tech Interview Communication Coach")
    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #3b82f6;'>🎤 The 2-Minute Vocal Alignment Drill</h3>
        <p>1. Open your voice recorder app on your phone.</p>
        <p>2. Explain exactly <b>how a Python Loop works</b> out loud for 2 minutes.</p>
        <p>3. Listen to your track. Delete it and record again until you sound confident and professional.</p>
    </div>
    """, unsafe_allow_html=True)
    
    data = {
        "What you say now": ["I want to do code for runs", "I wasted a lot of time", "I handle Thames water chat"],
        "What an AI Engineer says": ["I am implementing logic architectures", "I am strategically re-aligning my technical timeline", "I manage high-pressure data escalation logs"]
    }
    st.table(pd.DataFrame(data))
