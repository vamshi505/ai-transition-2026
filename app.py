import streamlit as st
import datetime
import pandas as pd
import time

# --- 1. STADIUM CONFIGURATION ---
st.set_page_config(
    page_title="VAMSHI'S AI STADIUM 2026",
    page_icon="🏏",
    layout="wide"
)

# --- 2. THE "NIGHT MATCH" INTERACTIVE UI ---
st.markdown("""
    <style>
    /* Stadium Background */
    .stApp {
        background: radial-gradient(circle at top, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
    }
    
    /* Sidebar: The Dugout */
    section[data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 2px solid #10b981;
    }
    
    /* Neon Stadium Cards */
    .stadium-card {
        background: rgba(30, 41, 59, 0.7);
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #10b981; /* Pitch Green */
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.3);
        margin-bottom: 25px;
    }
    
    /* Interactive Buttons: The Power-Hitters */
    .stButton>button {
        background: linear-gradient(90deg, #10b981 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 30px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.4s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(59, 130, 246, 0.6);
    }

    /* Progress Bars */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #10b981, #f59e0b);
    }
    
    h1, h2, h3 {
        font-family: 'Black Ops One', cursive, sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #f1f5f9;
    }
    
    .magic-text {
        color: #fbbf24; /* Gold */
        font-weight: bold;
        text-shadow: 0 0 10px rgba(251, 191, 36, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CORE LOGIC & STATE ---
today = datetime.date(2026, 6, 1)
interview_day = datetime.date(2026, 10, 1)
if 'streak' not in st.session_state: st.session_state.streak = 1
if 'flash_idx' not in st.session_state: st.session_state.flash_idx = 0

# --- 4. NAVIGATION: THE SCOREBOARD ---
st.sidebar.markdown("<h1 style='text-align: center; color: #10b981;'>🏏 MATCH CENTER</h1>", unsafe_allow_html=True)
st.sidebar.markdown(f"<p style='text-align: center;'><b>Vamshi 'The All-Rounder'</b><br>Day {st.session_state.streak} of Transition</p>", unsafe_allow_html=True)

nav = st.sidebar.radio("CHOOSE YOUR SECTOR:", [
    "🏟️ THE PAVILION (Dashboard)",
    "📅 SEASON SCHEDULE (Roadmap)",
    "🏆 SCORECARD (Progress)",
    "🧠 THE NETS (Logic Lab)",
    "💻 THE ACADEMY (Interactive)",
    "🗣️ MENTAL COACH (English)",
    "✨ THE MAGIC VAULT (GenAI & Jobs)"
])

# --- 5. THE PAVILION (DASHBOARD) ---
if nav == "🏟️ THE PAVILION (Dashboard)":
    st.title("🏟️ Main Stadium Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='stadium-card'><p>Days to Interviews</p><h2>{(interview_day - today).days}</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='stadium-card'><p>Career Average</p><h2 style='color: #10b981;'>85% Focus</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='stadium-card'><p>Current Rank</p><h2 style='color: #fbbf24;'>Future AI Lead</h2></div>", unsafe_allow_html=True)

    st.markdown("---")
    
    # Energy Strategy (Survivor Mode)
    st.subheader("🔋 Battery Check: How's the Energy after the 12H Shift?")
    energy = st.select_slider("", options=["0% (Exhausted)", "25% (Tired)", "50% (Steady)", "100% (Match Ready)"])
    
    if "0%" in energy:
        st.error("🚨 OVERLOAD DETECTED. Don't touch the code. Listen to one 'Mental Coach' audio and sleep.")
    elif "100%" in energy:
        st.success("🔥 POWERPLAY MODE! Go to 'The Nets' and build a complex Python loop right now.")
    else:
        st.info("⚡ ROTATE STRIKE. Spend 15 minutes on Flashcards and 5 minutes on English.")

    st.markdown("""
    <div class='stadium-card'>
        <h3 class='magic-text'>🔥 Mentor Buddy Message</h3>
        <p>"Vamshi, a pace all-rounder doesn't win the game by just bowling fast. He wins by staying at the crease when everyone else is tired. You've worked 12 hours? Great. That's your endurance. Now, let's play the straight drive into the world of AI."</p>
    </div>
    """, unsafe_allow_html=True)

# --- 6. SEASON SCHEDULE (ROADMAP) ---
elif nav == "📅 SEASON SCHEDULE (Roadmap)":
    st.title("📅 The 2026 Championship Journey")
    st.write("Every month is a different phase of the match.")
    
    roadmap = {
        "JUNE": "🏏 *THE NETS:* Python logic, strike rate calculators, data types.",
        "JULY": "📊 *THE MIDDLE OVERS:* SQL, Pandas, handling massive datasets.",
        "AUGUST": "🎯 *THE POWERPLAY:* Machine Learning algorithms (Predictions).",
        "SEPTEMBER": "✨ *THE MAGIC:* Generative AI, LLMs, and your Capstone Project.",
        "OCTOBER": "🏆 *THE FINALS:* Interviews start. Resume is ready. Applications live.",
        "NOV-DEC": "🏅 *VICTORY:* Landing the AI Engineer role."
    }
    
    for month, task in roadmap.items():
        with st.expander(f"📌 {month}"):
            st.write(task)
            st.button(f"Mark {month} as Completed", key=month)

# --- 7. SCORECARD (PROGRESS) ---
elif nav == "🏆 SCORECARD (Progress)":
    st.title("🏆 Career Scorecard")
    st.write("Track your 'Magical' topics and code logic mastery.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Python & Logic")
        p1 = st.checkbox("Variables & Math Logic")
        p2 = st.checkbox("If/Else Decision Making")
        p3 = st.checkbox("Loops (Over Analysis)")
    with col2:
        st.subheader("AI & Machine Learning")
        a1 = st.checkbox("What is Data Science?")
        a2 = st.checkbox("Linear Regression (Predictions)")
        a3 = st.checkbox("Generative AI Basics")
    
    total = sum([p1, p2, p3, a1, a2, a3])
    st.markdown(f"### Total Completion: {int((total/6)*100)}%")
    st.progress(total/6)

# --- 8. THE NETS (LOGIC LAB) ---
elif nav == "🧠 THE NETS (Logic Lab)":
    st.title("🧠 The Logic Nets")
    st.write("Learn coding through the rules of cricket.")
    
    tab1, tab2 = st.tabs(["English-to-Code Bridge", "Cricket Code Scenarios"])
    
    with tab1:
        st.subheader("🌉 The Bridge")
        st.write("If I say: 'If the batsman scores a 6, he gets a bonus.'")
        st.write("Python says:")
        st.code("""
if runs == 6:
    score = score + 12  # Double the reward!
        """, language="python")
        
    with tab2:
        st.subheader("🏏 Scenario: All-Rounder Selection")
        st.write("Logic: Select the player if Strike Rate > 140 AND Wickets > 1.")
        st.code("""
sr = 150
wickets = 2

if sr > 140 and wickets > 1:
    print("SELECTED FOR NATIONAL TEAM")
else:
    print("SEND BACK TO DOMESTIC")
        """, language="python")

# --- 9. THE ACADEMY (INTERACTIVE) ---
elif nav == "💻 THE ACADEMY (Interactive)":
    st.title("💻 Interactive Learning Hub")
    st.write("High-dopamine websites to keep you addicted to learning.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='stadium-card'>
            <h4>🎮 Gamified Coding</h4>
            <p><a href='https://coddy.tech' target='_blank'>Coddy.tech</a> - Duolingo for Code.</p>
            <p><a href='https://py.checkio.org/' target='_blank'>CheckiO</a> - Save a world with Python.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='stadium-card'>
            <h4>🧩 Daily Logic</h4>
            <p><a href='https://www.codewars.com/' target='_blank'>Codewars</a> - Level up like a Pro.</p>
        </div>
        """, unsafe_allow_html=True)

# --- 10. MENTAL COACH (ENGLISH) ---
elif nav == "🗣️ MENTAL COACH (English)":
    st.title("🗣️ English & Communication")
    st.write("Goal: Move from *5/10* to *8/10*.")
    
    st.markdown("""
    <div class='stadium-card'>
        <h3>🎤 2-Minute Voice Drill</h3>
        <p>Topic: <b>'Why I want to be an AI Engineer'</b></p>
        <p>1. Open your phone recorder.<br>2. Speak for 2 mins in English.<br>3. Listen and find one mistake.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 *Mentor Tip:* Use the 'Grammarly' app on your phone while writing emails or chat tickets at Tech Mahindra. It fixes your mistakes while you work.")

# --- 11. THE MAGIC VAULT (GENAI & JOBS) ---
elif nav == "✨ THE MAGIC VAULT (GenAI & Jobs)":
    st.title("✨ The Magic Vault")
    
    st.subheader("🧙 'Magical' AI Concepts")
    with st.expander("What is Generative AI? (Simple terms)"):
        st.write("Think of it as a batsman who has seen every single cricket match ever played. Now, you ask him to play a shot that has never been played before. Because he knows the 'patterns' of the game, he can 'generate' a new shot.")
    
    with st.expander("What are LLMs (Large Language Models)?"):
        st.write("Massive brains that predict the next word just like a bowler predicts the next weakness in a batsman.")

    st.markdown("---")
    st.subheader("💼 Job Market Radar (Oct 1st Active)")
    st.warning("Note: Starting October 1st, this section will host your Resume Builder and Job Application Tracker.")
    st.write("Target Roles: Junior AI/ML Engineer, Data Analyst, Technical Solutions Associate.")
