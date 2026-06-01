import streamlit as st
import datetime
import pandas as pd
import time

# --- 1. ARENA ARCHITECTURE CONFIGURATION ---
st.set_page_config(
    page_title="Vamshi's Deadpool AI Stadium 2026",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. HIGH-DOPAMINE CRIMSON & STADIUM DARK CSS ---
st.markdown("""
    <style>
    /* Global Canvas Dark Mode */
    .stApp {
        background: radial-gradient(circle at center, #1f0606 0%, #000000 100%);
        color: #f1f5f9;
    }
    
    /* Neon Crimson Sidebar Dugout */
    section[data-testid="stSidebar"] {
        background-color: #0d0101 !important;
        border-right: 3px solid #e23636;
    }
    
    /* Interactive Metric Cards */
    .stadium-card {
        background: linear-gradient(135deg, #2a0808 0%, #080101 100%);
        padding: 24px;
        border-radius: 16px;
        border: 2px solid #e23636;
        box-shadow: 0 0 20px rgba(226, 54, 54, 0.35);
        margin-bottom: 24px;
    }
    
    /* Embedded Resource Links Block */
    .video-box {
        background-color: #0b0f19;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #3b82f6;
        margin-top: 12px;
    }
    
    /* Power Button Global Styles */
    .stButton>button {
        background: linear-gradient(90deg, #e23636 0%, #7f1d1d 100%);
        color: #ffffff !important;
        border: 1px solid #ffffff !important;
        border-radius: 40px !important;
        padding: 14px 28px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        transition: 0.4s all ease-in-out !important;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 0 30px rgba(226, 54, 54, 0.75);
    }
    
    /* Typography Overrides */
    h1, h2, h3, h4 {
        color: #e23636;
        font-family: 'Impact', 'Arial Black', sans-serif;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    
    .glow-gold {
        color: #fbbf24;
        text-shadow: 0 0 12px rgba(251, 191, 36, 0.7);
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. COGNITIVE APPLICATION MEMORY ARRAYS ---
if 'streak_counter' not in st.session_state: 
    st.session_state.streak_counter = 1
if 'stadium_runs' not in st.session_state: 
    st.session_state.stadium_runs = 0
if 'live_chat_history' not in st.session_state: 
    st.session_state.live_chat_history = []

# --- 4. TOURNAMENT SCHEDULE ANCHORS (2026) ---
current_match_day = datetime.date(2026, 6, 1)
interview_match_day = datetime.date(2026, 10, 1)
world_cup_deadline = datetime.date(2026, 12, 31)

# --- 5. SIDEBAR COMMAND PANEL CONTROL ---
st.sidebar.markdown("<h1 style='text-align: center; color: #e23636;'>⚔️ DEADPOOL</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #9ca3af;'><b>BATSMAN: VAMSHI THE ALL-ROUNDER</b></p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown(f"🔥 **Win Streak:** `{st.session_state.streak_counter} Matches`")
if st.sidebar.button("🏏 LOG DAILY TRAINING"):
    st.session_state.streak_counter += 1
    st.sidebar.success("Session logged!")

menu_selection = st.sidebar.radio("NAVIGATE ARENA SECTORS:", [
    "🏟️ The Pavilion (Dashboard)",
    "📅 Complete 7-Month Roadmap",
    "📊 Master Progress Scorecard",
    "🧠 The Coding Nets (Logic Lab)",
    "💬 Chat with Deadpool (Direct Mode)",
    "🗣️ Professional English Tuner"
])

# --- 6. SECTOR: THE PAVILION ---
if menu_selection == "🏟️ The Pavilion (Dashboard)":
    st.title("🏟️ Main Command Pavilion")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='stadium-card'><h5>Days to Oct 1st Finals</h5><h2 class='glow-gold'>{(interview_match_day - current_match_day).days}</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='stadium-card'><h5>Current Rank</h5><h2 style='color: #3b82f6;'>All-Rounder ⚡</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='stadium-card'><h5>Your Score</h5><h2 style='color: #10b981;'>{st.session_state.stadium_runs} Runs</h2></div>", unsafe_allow_html=True)

    energy_input = st.select_slider("Energy Level:", options=["0%", "25%", "50%", "100%"])
    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #e23636;'>⚔️ Deadpool's Corner</h3>
        <p>"Listen, Vamshi. I've built this stadium for you. No more typing keys. Just pure AI logic. 
        You worked 12 hours? Great, now give me 20 minutes of <b>Maximum Effort</b>."</p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. ROADMAP ---
elif menu_selection == "📅 Complete 7-Month Roadmap":
    st.title("📅 The 2026 Career Roadmap")
    st.markdown("""
    <div class='stadium-card'><h3>June: Python Logic Foundations</h3><p>Variables, Loops, and If/Else constructions.</p></div>
    <div class='stadium-card'><h3>July: SQL & Data Manipulation</h3><p>Joins, Aggregations, and Pandas.</p></div>
    <div class='stadium-card'><h3>August: Machine Learning Pipelines</h3><p>Regression, Trees, and Model Metrics.</p></div>
    <div class='stadium-card'><h3>September: GenAI & LLM Projects</h3><p>The 'Magic' phase. APIs and Capstone.</p></div>
    <div class='stadium-card'><h3>Oct-Dec: World Cup Finals</h3><p>Interview Blitz and Placements.</p></div>
    """, unsafe_allow_html=True)

# --- 8. SCORECARD ---
elif menu_selection == "📊 Master Progress Scorecard":
    st.title("📊 Complete Syllabus Tracker")
    with st.expander("✅ JUNE: Python Core (Nets)"):
        j1 = st.checkbox("Variables & Data Types")
        j2 = st.checkbox("If/Else Decisions")
        j3 = st.checkbox("For & While Loops")
        j4 = st.checkbox("Lists & Dictionaries")
        j5 = st.checkbox("Functions & Modules")
        st.markdown("<div class='video-box'>📺 <a href='https://www.youtube.com/results?search_query=freecodecamp+python' target='_blank'>FreeCodeCamp: Python Course</a></div>", unsafe_allow_html=True)
    
    with st.expander("✅ JULY - AUGUST: Middle Overs"):
        st.checkbox("SQL Selection & Joins")
        st.checkbox("Pandas Analytics")
        st.checkbox("ML Regression Models")
    
    with st.expander("✅ SEPTEMBER: GenAI (Magic Phase)"):
        st.checkbox("LLM Attention & Transformers")
        st.checkbox("Sentiment Capstone Finalization")

    st.progress((j1+j2+j3+j4+j5)/37)

# --- 9. LOGIC LAB ---
elif menu_selection == "🧠 The Coding Nets (Logic Lab)":
    st.title("🧠 The Interactive Logic Lab")
    st.code("""
player_runs = 45
player_balls = 20
strike_rate = (player_runs / player_balls) * 100

if strike_rate > 200:
    print("Explosive")
else:
    print("Anchor")
    """, language="python")
    
    sim_guess = st.text_input("What exact word will print on screen?")
    if st.button("Submit Review"):
        if sim_guess.strip() == "Explosive":
            st.balloons()
            st.success("🎯 BOUNDARY! +10 Runs!")
            st.session_state.stadium_runs += 10

# --- 10. CHAT WITH DEADPOOL (FIXED NAME) ---
elif menu_selection == "💬 Chat with Deadpool (Direct Mode)":
    st.title("💬 Talk to Deadpool (Direct Mode)")
    st.write("No keys needed in the code. Uses your Streamlit Secrets.")
    
    user_prompt_entry = st.chat_input("Send a message to Deadpool...")
    
    if user_prompt_entry:
        st.session_state.live_chat_history.append(f"Vamshi: {user_prompt_entry}")
        try:
            import google.generativeai as live_genai
            secure_vault_key = st.secrets["GEMINI_API_KEY"]
            live_genai.configure(api_key=secure_vault_key)
            llm_processing_engine = live_genai.GenerativeModel('gemini-1.5-flash')
            
            persona_prompt = f"You are Deadpool, the sarcastic AI coding mentor. Help Vamshi. Question: {user_prompt_entry}"
            model_output = llm_processing_engine.generate_content(persona_prompt)
            deadpool_reply = model_output.text
        except Exception as e:
            deadpool_reply = f"Chimichangas! Check your 'Secrets' in Streamlit settings. Error: {str(e)}"
            
        st.session_state.live_chat_history.append(f"Deadpool ⚔️: {deadpool_reply}")

    for structural_message in st.session_state.live_chat_history:
        if structural_message.startswith("Vamshi:"):
            st.markdown(f"🧑 **{structural_message}**")
        else:
            st.markdown(f"<div class='stadium-card' style='border-left: 5px solid #e23636;'>🔴 <b>{structural_message}</b></div>", unsafe_allow_html=True)

# --- 11. ENGLISH TUNER ---
elif menu_selection == "🗣️ Professional English Tuner":
    st.title("🗣️ Technical Communication Coach")
    st.markdown("""
    <div class='stadium-card'>
        <h3>🎤 2-Minute Vocal Routine</h3>
        <p>1. Record yourself explaining 'What is a Loop' for 2 minutes in English.<br>2. Listen and fix one mistake. Repeat.</p>
    </div>
    """, unsafe_allow_html=True)
    st.table(pd.DataFrame({
        "Casual": ["I want to do code", "I am weak in logic"],
        "Enterprise": ["I am implementing architecture", "I am optimizing my problem-solving paradigms"]
    }))
