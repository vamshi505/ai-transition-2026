import streamlit as st
import datetime
import pandas as pd
import time

# --- 1. THE "ULTIMATE" UI CONFIGURATION ---
st.set_page_config(
    page_title="Vamshi's AI Transition Hub",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS: CYBER-CRICKET DARK THEME ---
st.markdown("""
    <style>
    /* Dark Theme Background */
    .stApp {
        background-color: #0b0e14;
        color: #e0e6ed;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    
    /* Neon Green & Gold Accent Cards */
    .metric-card {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #34d399; /* Cricket Green */
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    
    .status-gold {
        color: #fbbf24; /* Gold */
        font-weight: bold;
    }
    
    /* Interactive Button Styling */
    .stButton>button {
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s all ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(16, 185, 129, 0.4);
    }

    /* Roadmap Steps */
    .step-box {
        border-left: 4px solid #10b981;
        padding-left: 20px;
        margin-bottom: 20px;
        background: #1c2128;
        padding: 15px;
        border-radius: 0 10px 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE FOR INTERACTIVITY ---
if 'flash_idx' not in st.session_state: st.session_state.flash_idx = 0
if 'energy_level' not in st.session_state: st.session_state.energy_level = "Steady"

# --- 4. DATA CONTENT ---
today = datetime.date(2026, 6, 1)
goal_date = datetime.date(2026, 12, 31)
interview_date = datetime.date(2026, 10, 1)

flashcards = [
    {"q": "What is an Algorithm?", "a": "A step-by-step recipe for the computer. Like a cricket strategy for a Super Over."},
    {"q": "What is a Neural Network?", "a": "An AI structure inspired by the human brain to find complex patterns."},
    {"q": "What is Generative AI?", "a": "AI that can create new content (text, images, code) instead of just analyzing old data."},
    {"q": "What is 'Fine-Tuning'?", "a": "Taking a smart AI and training it specifically for one task, like coaching a general batsman to play only spin."}
]

# --- 5. NAVIGATION ---
st.sidebar.markdown("<h1 style='text-align: center; color: #10b981;'>🏏 TITAN HUB</h1>", unsafe_allow_html=True)
st.sidebar.markdown("---")
page = st.sidebar.radio("CHOOSE SECTOR:", [
    "🚀 Command Dashboard",
    "📅 7-Month Roadmap",
    "🧠 Logic & Code Gym",
    "📚 The Knowledge Vault (GenAI)",
    "🗣️ Communication Mentor",
    "🎯 Progress Scorecard"
])

# --- 6. PAGE: COMMAND DASHBOARD ---
if page == "🚀 Command Dashboard":
    st.title("Welcome to the Second Innings")
    
    # Hero Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='metric-card'><h3>Days to Job Hunt</h3><h2 class='status-gold'>{(interview_date - today).days}</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-card'><h3>Season Progress</h3><h2 style='color: #10b981;'>12%</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-card'><h3>Current Level</h3><h2 style='color: #58a6ff;'>Beginner</h2></div>", unsafe_allow_html=True)

    # Energy-Based Recommendation
    st.subheader("🔋 Energy Check")
    st.session_state.energy_level = st.select_slider("How is your battery after the 12hr shift?", options=["Dead", "Low", "Steady", "Fully Charged"])
    
    if st.session_state.energy_level == "Dead":
        st.error("⚠️ CRITICAL: Brain overload. Do not code. Go to 'Knowledge Vault' and read 2 flashcards, then sleep.")
    elif st.session_state.energy_level == "Fully Charged":
        st.success("🔥 POWERPLAY: You have high focus. Go to 'Logic & Code Gym' and solve the Hard Challenge.")
    else:
        st.info("⚡ STEADY: Good for Roadmap review and 10 mins of English practice.")

    # Concentration Timer
    st.markdown("---")
    st.subheader("⏲️ T20 Concentration Timer")
    if st.button("Start 20-Minute Study Over"):
        st.balloons()
        st.write("Timer Active! Put your phone away. No distractions until the over is finished.")

# --- 7. PAGE: ROADMAP ---
elif page == "📅 7-Month Roadmap":
    st.title("📅 The 2026 Championship Path")
    
    months = {
        "June": "Python Logic & Syntax (Mastering the Batting Stance)",
        "July": "SQL & Data Analytics (Reading the Pitch)",
        "August": "Machine Learning Foundations (The Powerplay)",
        "September": "GenAI & Capstone Project (The Death Overs)",
        "October": "Interview Prep & Job Hunt (The Grand Finale)",
        "Nov-Dec": "Landing the Offer & Onboarding (Winning the Trophy)"
    }
    
    for month, task in months.items():
        st.markdown(f"<div class='step-box'><h3>{month}</h3><p>{task}</p></div>", unsafe_allow_html=True)

# --- 8. PAGE: LOGIC & CODE GYM ---
elif page == "🧠 Logic & Code Gym":
    st.title("🧠 The Logic Playground")
    st.write("Convert your cricket knowledge into Python logic.")
    
    st.subheader("Problem Solving Technique: 'The DRS Method'")
    st.markdown("""
    1. **Define** (The Input): What data do I have? (e.g., Runs per ball)
    2. **Review** (The Logic): What is the condition? (e.g., If run == 0, it's a dot ball)
    3. **Solve** (The Code): Write it ball-by-ball.
    """)
    
    st.subheader("Challenge: The Strike Rate Logic")
    st.code("""
runs = 45
balls = 20

# Calculate Strike Rate
strike_rate = (runs / balls) * 100

if strike_rate > 200:
    print("Explosive Finish!")
elif strike_rate > 150:
    print("Aggressive Batting")
else:
    print("Rotating Strike")
    """, language="python")
    
    st.markdown("### 🕹️ Interactive Learning Sites")
    st.write("Click these to get your dopamine fix through gamified coding:")
    st.markdown("- [Coddy.tech](https://coddy.tech) (Interactive Python)")
    st.markdown("- [CheckiO](https://py.checkio.org/) (Coding Game)")

# --- 9. PAGE: KNOWLEDGE VAULT ---
elif page == "📚 The Knowledge Vault (GenAI)":
    st.title("📚 AI Knowledge & Flashcards")
    
    st.subheader("⚡ Commuter Flashcards")
    card = flashcards[st.session_state.flash_idx]
    st.markdown(f"<div style='background: #1f2937; padding: 40px; border-radius: 15px; border: 2px solid #58a6ff; text-align: center;'><h2>{card['q']}</h2></div>", unsafe_allow_html=True)
    
    if st.button("Reveal Magic"):
        st.success(card['a'])
    
    if st.button("Next Ball (Next Card)"):
        st.session_state.flash_idx = (st.session_state.flash_idx + 1) % len(flashcards)
        st.rerun()

    st.markdown("---")
    st.subheader("🤖 The 'Magical' AI Topics")
    st.write("**Generative AI:** The ability for machines to generate content. It uses something called **Transformers** (Attention mechanism) to focus on important words in a sentence.")

# --- 10. PAGE: COMMUNICATION MENTOR ---
elif nav == "🗣️ Communication Mentor":
    st.title("🗣️ The English Coaching Sector")
    st.write("Current Rating: **5/10** ➔ Target: **8/10**")
    
    st.markdown("""
    <div class='metric-card'>
    <h3>🎤 The 2-Minute Interview Drill</h3>
    <p>1. Record yourself explaining 'What is a Loop?'</p>
    <p>2. Don't use 'um' or 'uh'.</p>
    <p>3. Use Grammarly to check your written logic emails.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Technical English Tip")
    st.info("Instead of saying 'I want to do this', say 'My objective is to implement this logic.'")

# --- 11. PAGE: PROGRESS SCORECARD ---
elif nav == "🎯 Progress Scorecard":
    st.title("🏆 Career Progress Tracking")
    st.write("Check these off as you complete them. No skipping!")
    
    with st.expander("✅ JUNE: Python Foundations"):
        st.checkbox("Variables & Data Types")
        st.checkbox("Conditionals (If/Else)")
        st.checkbox("For & While Loops")
        st.checkbox("Lists & Dictionaries")
    
    with st.expander("✅ JULY: Data & SQL"):
        st.checkbox("SQL Select & Filters")
        st.checkbox("Pandas Basics")
        
    st.subheader("Your Career Growth")
    st.progress(12)
    st.write("Level 1: The Rookie All-Rounder")
