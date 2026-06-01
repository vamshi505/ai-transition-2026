import streamlit as st
import datetime
import pandas as pd
import time

# --- 1. STADIUM ARCHITECTURE & CONFIGURATION ---
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

    /* Professional Power Buttons */
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

# --- 4. TOURNAMENT SCHEDULE ANCHORS (2026) ---
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
    st.sidebar.success("Streak saved! Maximum Effort!")

nav_choice = st.sidebar.radio("NAVIGATE ARENA SECTORS:", [
    "🏟️ The Pavilion (Dashboard)",
    "📅 Complete 7-Month Roadmap",
    "📊 Master Progress Scorecard",
    "🧠 The Coding Nets (Logic Lab)",
    "💬 Chat with Deadpool (Direct Mode)",
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

    st.subheader("🔋 Energy Recovery Tracker")
    energy = st.select_slider("How is your physical battery right now?", options=["0% (Exhausted)", "25%", "50%", "100% (Full Power)"])
    
    if "0%" in energy:
        st.error("🚨 OVERLOAD. Do not code. Talk to Deadpool or do a vocal drill, then sleep.")
    elif "100%" in energy:
        st.success("🔥 POWERPLAY! Open 'The Nets' and crush a logic problem.")

    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #e23636;'>⚔️ Deadpool's Mentorship</h3>
        <p>"Vamshi, listen to me. I once regrew my whole body from a thumb. You can learn Python after a 12-hour shift. 
        Don't let a 404 error take your hope. That's just the universe testing your <b>endurance</b>. 
        If you can handle escalations at Tech Mahindra, you can handle a backend server. <b>Maximum Effort!</b>"</p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. SECTOR: 7-MONTH ROADMAP ---
elif nav_choice == "📅 Complete 7-Month Roadmap":
    st.title("📅 The 2026 Professional Transition Timeline")
    
    st.markdown("""
    <div class='stadium-card'>
        <h3>🏏 PHASE 1: THE NETS PRACTICE (June - July)</h3>
        <p><b>Focus:</b> Algorithmic Thinking, Data Manipulation, and SQL.</p>
        <ul>
            <li>June: Variables, Loops, Conditionals, and modular functions.</li>
            <li>July: Relational Databases, multi-table joins, and Pandas analytics.</li>
        </ul>
    </div>
    <div class='stadium-card'>
        <h3>🎯 PHASE 2: THE MID-OVER EXPLOSION (August - September)</h3>
        <p><b>Focus:</b> Machine Learning & Magical AI (GenAI).</p>
        <ul>
            <li>August: Regression, Decision Trees, Forests, and model evaluation metrics.</li>
            <li>September: Neural Networks, Transformers, LLMs, APIs, and Capstone Project.</li>
        </ul>
    </div>
    <div class='stadium-card'>
        <h3>🏆 PHASE 3: THE WORLD CUP FINALS (October - December)</h3>
        <p><b>Focus:</b> Portfolio Deployment & Interview Execution.</p>
        <ul>
            <li>October 1: Launch applications. Intensive Data Structures review.</li>
            <li>Nov-Dec: Technical panel mocks, resume remodeling, and securing the Offer Letter.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- 8. SECTOR: MASTER PROGRESS SCORECARD (FULL 37 POINTS) ---
elif nav_choice == "📊 Master Progress Scorecard":
    st.title("📊 Complete 37-Point Interactive Mastery Matrix")
    st.write("Track every single milestone from absolute zero to AI Engineer.")

    # JUNE (10 POINTS)
    st.markdown("### 📅 JUNE: Python Core Foundations")
    j1 = st.checkbox("Memory Mapping & Variable Assignment")
    j2 = st.checkbox("Data Types: Int, Float, String, and Booleans")
    j3 = st.checkbox("Comparison Mechanics (==, !=, >, <)")
    j4 = st.checkbox("Chained Logical Conditions (AND, OR, NOT)")
    j5 = st.checkbox("Conditional Architectures (If, Elif, Else)")
    j6 = st.checkbox("Iterative Processing: For Loops")
    j7 = st.checkbox("Conditional Processing: While Loops")
    j8 = st.checkbox("Layouts Part 1: Python Lists (Arrays)")
    j9 = st.checkbox("Layouts Part 2: Dictionaries (Key-Value Maps)")
    j10 = st.checkbox("Functional Paradigms: Return Scope & Arguments")
    st.markdown("<div class='video-box'>📺 <b>June Masterclass:</b> <a href='https://www.youtube.com/results?search_query=freecodecamp+python+full+course' target='_blank'>Python Foundational Training</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # JULY (7 POINTS)
    st.markdown("### 📅 JULY: SQL & Data Manipulation")
    jy1 = st.checkbox("Relational Concepts & Schema Design")
    jy2 = st.checkbox("Query Selections (SELECT, WHERE, LIKE)")
    jy3 = st.checkbox("Data Merges: INNER JOIN and LEFT JOIN")
    jy4 = st.checkbox("Dataset Aggregates: GROUP BY and HAVING")
    jy5 = st.checkbox("Pandas Engineering: Series and DataFrames")
    jy6 = st.checkbox("Data Sanitization: Treating Null Values")
    jy7 = st.checkbox("Handling Duplicate & Corrupted Records")
    st.markdown("<div class='video-box'>📺 <b>July Masterclass:</b> <a href='https://www.youtube.com/results?search_query=freecodecamp+sql' target='_blank'>Complete SQL Guide</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # AUGUST (7 POINTS)
    st.markdown("### 📅 AUGUST: Machine Learning Architecture")
    a1 = st.checkbox("Supervised Pipelines: Linear Regression math")
    a2 = st.checkbox("Classification: Logistic Regression boundaries")
    a3 = st.checkbox("Ensemble Systems: Decision Trees & Forests")
    a4 = st.checkbox("Feature Engineering: Scaling & Normalization")
    a5 = st.checkbox("Validation: Train-Test Data Splitting")
    a6 = st.checkbox("Performance: Precision, Recall, and F1 math")
    a7 = st.checkbox("Confusion Matrix Visualization")
    st.markdown("<div class='video-box'>📺 <b>August Masterclass:</b> <a href='https://www.youtube.com/results?search_query=statquest+machine+learning' target='_blank'>Visual ML Fundamentals</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # SEPTEMBER (7 POINTS)
    st.markdown("### 📅 SEPTEMBER: Generative AI & Capstone Final")
    s1 = st.checkbox("Neural Networks & Activation Functions")
    s2 = st.checkbox("Transformer Mechanics: Tokenization & Attention")
    s3 = st.checkbox("API Engineering: Gemini & OpenAI Endpoints")
    s4 = st.checkbox("Prompt Engineering Strategy (Few-Shot)")
    s5 = st.checkbox("Capstone Phase 1: Recommendation System Design")
    s6 = st.checkbox("Capstone Phase 2: Sentiment Feature Analysis")
    s7 = st.checkbox("Capstone Phase 3: Deployment to Streamlit Cloud")
    st.markdown("<div class='video-box'>📺 <b>September Masterclass:</b> <a href='https://www.youtube.com/results?search_query=andrej+karpathy+llm' target='_blank'>LLMs from Scratch</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # OCT-DEC (6 POINTS)
    st.markdown("### 📅 OCTOBER - DECEMBER: The Final Placement")
    o1 = st.checkbox("Algorithmic Basics: Binary Search implementation")
    o2 = st.checkbox("Sorting Routines: Bubble & Merge Sort complexity")
    o3 = st.checkbox("Interview Structures: Arrays, Strings, HashMaps")
    o4 = st.checkbox("Resume Remodeling: Framing Support as Tech Ops")
    o5 = st.checkbox("GitHub Pipeline Polish & Documentation")
    o6 = st.checkbox("Technical Panel Prep: Mock Simulations")

    st.markdown("---")
    checked = j1+j2+j3+j4+j5+j6+j7+j8+j9+j10+jy1+jy2+jy3+jy4+jy5+jy6+jy7+a1+a2+a3+a4+a5+a6+a7+s1+s2+s3+s4+s5+s6+s7+o1+o2+o3+o4+o5+o6
    st.subheader(f"Overall Season Mastery: {int((checked/37)*100)}%")
    st.progress(checked/37)

# --- 9. SECTOR: THE CODING NETS (LOGIC LAB) ---
elif nav_choice == "🧠 The Coding Nets (Logic Lab)":
    st.title("🧠 Programmatic Logic Training Ground")
    st.write("Deconstruct algorithmic parameters using cricket match scenarios.")
    
    st.subheader("Match Scenario: Tactical Selection Logic")
    st.code("""
# Rule: Select if runs > 50 AND Strike Rate > 150.
# If runs > 50 but SR is lower, label as 'Anchor'.
# Otherwise, 'Keep Playing'.

player_runs = 62
strike_rate = 165

if player_runs > 50 and strike_rate > 150:
    print("Elite Performance")
elif player_runs > 50:
    print("Anchor Inning")
else:
    print("Keep Playing")
    """, language="python")
    
    ans = st.text_input("What keyword will print on the screen? (Check the values carefully)")
    if st.button("Submit Decision Review (DRS)"):
        if ans.strip() == "Elite Performance":
            st.balloons()
            st.success("🎯 BOUNDARY! Both conditions were true. +10 Runs added to your score!")
            st.session_state.runs += 10
        else:
            st.error("❌ Dot Ball! Read the variables again. Both 62 and 165 pass the 'Elite' criteria.")

# --- 10. SECTOR: LIVE CHAT WITH DEADPOOL (SMART MODEL SELECTOR) ---
elif nav_choice == "💬 Chat with Deadpool (Direct Mode)":
    st.title("💬 Talk to Deadpool (Direct Access)")
    st.write("No more distractions. Just you, me, and the AI.")
    
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("🚨 BRAIN DISCONNECTED! Deadpool needs his API Key fuel.")
        st.info("Fix this in 2 seconds: Go to Streamlit Cloud -> Settings -> Secrets and paste: GEMINI_API_KEY = 'your_key'")
    else:
        try:
            import google.generativeai as genai
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            
            # --- SMART MODEL AUTO-SELECTOR (No more 404s) ---
            if 'model_name' not in st.session_state:
                with st.spinner("⚔️ Scanning Google's backend for a working model..."):
                    try:
                        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                        # Prioritize 1.5-flash, then 1.5-pro, then legacy pro
                        if 'models/gemini-1.5-flash' in available_models: st.session_state.model_name = 'gemini-1.5-flash'
                        elif 'models/gemini-pro' in available_models: st.session_state.model_name = 'gemini-pro'
                        else: st.session_state.model_name = available_models[0]
                    except:
                        st.session_state.model_name = 'gemini-pro' # Absolute fallback

            model = genai.GenerativeModel(st.session_state.model_name)
            
            user_msg = st.chat_input("Ask me anything, Vamshi...")
            
            if user_msg:
                st.session_state.chat_log.append(f"Vamshi: {user_msg}")
                instr = f"Reply as Deadpool, sarcastic and funny AI mentor. Help Vamshi. Use cricket analogies. Question: {user_msg}"
                res = model.generate_content(instr)
                st.session_state.chat_log.append(f"Deadpool ⚔️: {res.text}")

            for m in st.session_state.chat_log:
                if m.startswith("Vamshi:"): st.write(f"🧑 **{m}**")
                else: st.markdown(f"<div class='stadium-card' style='border-left: 5px solid #e23636;'>🔴 <b>{m}</b></div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Chimichangas! Technical Fault: {str(e)}")

# --- 11. SECTOR: PROFESSIONAL ENGLISH TUNER ---
elif nav_choice == "🗣️ Professional English Tuner":
    st.title("🗣️ Technical Screener Communication Coach")
    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #3b82f6;'>🎤 The 2-Minute Vocal Alignment Drill</h3>
        <p>1. Open your phone recorder right now.</p>
        <p>2. Explain exactly <b>how a Python Variable works</b> in English for 2 minutes.</p>
        <p>3. Listen to it. Notice the 'ums'. Fix one word and record again. Neural confidence is built through repetition!</p>
    </div>
    """, unsafe_allow_html=True)
    
    phrase_data = {
        "Casual Phrase (Avoid)": ["I want to do code for runs", "I wasted a lot of time", "I handle chat customer escalations"],
        "Elite Engineering Phrase (Use)": ["I am implementing logic architectures", "I am strategically re-aligning my career roadmap", "I manage high-pressure database queue logs and resolve critical escalations"]
    }
    st.table(pd.DataFrame(phrase_data))
