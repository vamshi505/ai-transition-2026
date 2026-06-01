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
        text-transform: uppercase;
        letter-spacing: 1.5px;
        transition: 0.4s all ease-in-out;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 0 30px rgba(226, 54, 54, 0.75);
    }
    
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

# --- 6. SECTOR: THE PAVILION (DASHBOARD) ---
if menu_selection == "🏟️ The Pavilion (Dashboard)":
    st.title("🏟️ Main Command Pavilion")
    st.write("Wankhede Stadium under neon stadium floodlights. Today is June 1, 2026. Your transition begins now.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='stadium-card'><h5>Days to October 1st Qualification</h5><h2 class='glow-gold'>{(interview_match_day - current_match_day).days} Days</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='stadium-card'><h5>Player Strategy Tier</h5><h2 style='color: #3b82f6;'>Pace All-Rounder ⚡</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='stadium-card'><h5>Accumulated Runs Score</h5><h2 style='color: #10b981;'>{st.session_state.stadium_runs} Runs</h2></div>", unsafe_allow_html=True)

    energy_input = st.select_slider("What is your physical baseline battery level after work?", options=["0%", "25%", "50%", "100%"])
    if "0%" in energy_input:
        st.error("🚨 Critical Fatigue. Take a short breather, read your roadmap, and rest up.")
    else:
        st.success("🔥 Powerplay active! Dive into the logic training blocks.")

    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #e23636;'>⚔️ Deadpool's Mentorship Blueprint</h3>
        <p><i>"Look at the screen, Vamshi. You managed to build a cloud server pipeline from scratch tonight. That is genuine data architecture work. Don't let a backend version mismatch steal your focus. We are tracking down the exact line right now. Maximum Effort."</i></p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. SECTOR: COMPLETE 7-MONTH ROADMAP ---
elif menu_selection == "📅 Complete 7-Month Roadmap":
    st.title("📅 The 2026 Professional AI Career Transition Timeline")
    st.write("Your definitive tournament layout from June 1st to December 31st, 2026.")
    
    st.markdown("""
    <div class='stadium-card'>
        <h3>🏏 PHASE 1: THE NETS CLINIC (June — July)</h3>
        <p><b>Objective:</b> Construct pure algorithmic logic frameworks from absolute scratch.</p>
        <ul>
            <li><b>June:</b> Variable memory boundaries, logic operators, structural conditionals, execution loops, and functions.</li>
            <li><b>July:</b> Relational Database engineering, multi-table structural merges, and high-speed Pandas DataFrames.</li>
        </ul>
    </div>
    <div class='stadium-card'>
        <h3>🎯 PHASE 2: THE MID-OVER RUN RATE EXPLOSION (August — September)</h3>
        <p><b>Objective:</b> Master predictive scoring algorithms and Generative AI LLM architectures.</p>
        <ul>
            <li><b>August:</b> Linear & Logistic model equations, classification parameters, tree structures, and Scikit-Learn.</li>
            <li><b>September:</b> Neural networks, Transformer attention layers, and finishing your Sentiment Product Recommendation System.</li>
        </ul>
    </div>
    <div class='stadium-card'>
        <h3>🏆 PHASE 3: THE WORLD CUP FINALS PLACEMENT BLITZ (October — December)</h3>
        <p><b>Objective:</b> Scale active company outbound operations and clear recruitment evaluation panels.</p>
        <ul>
            <li><b>October 1st:</b> Launch applications. Review array data structures, sorting complexities, and transform resume metrics.</li>
            <li><b>November - December:</b> Run production mock panels, clear screening interviews, and lock down your offer contract.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- 8. SECTOR: THE COMPLETE 37-POINT TRACKING MATRIX ---
elif menu_selection == "📊 Master Progress Scorecard":
    st.title("📊 Complete 37-Point Interactive Syllabus Tracker")
    st.write("Every single technical milestone explicitly typed out line-by-line.")

    st.markdown("### 📅 JUNE: Python Core Analytics & Logic Gates")
    j1 = st.checkbox("Variables, core memory buckets, and scope tracking")
    j2 = st.checkbox("Data Types: Integers, Float vectors, string buffers, and Booleans")
    j3 = st.checkbox("Comparison Mechanics: Constructing truth valuations (==, !=, >, <)")
    j4 = st.checkbox("Chained Logical Conditions: Managing variable thresholds via AND, OR, NOT")
    j5 = st.checkbox("Conditional Selection: Writing nested If, Elif, and Else control flows")
    j6 = st.checkbox("Definite Iteration: For Loops across data sequences")
    j7 = st.checkbox("Indefinite Iteration: While Loops with operational exit constraints")
    j8 = st.checkbox("Sequence Layouts: Python Lists array manipulation and indexing")
    j9 = st.checkbox("Mapping Arrays: Python Dictionaries key-value layouts")
    j10 = st.checkbox("Functional Programming: Reusable functions and argument scopes")
    st.markdown("<div class='video-box'>📺 <b>June Masterclass Links:</b><br>• <a href='https://www.youtube.com/results?search_query=freecodecamp+python+full+course' target='_blank'>FreeCodeCamp: Python Masterclass</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 📅 JULY: Relational Data Models & SQL Processing")
    jy1 = st.checkbox("Relational Architecture and structured database layouts")
    jy2 = st.checkbox("Data Extraction Queries: SELECT, WHERE, LIKE filters")
    jy3 = st.checkbox("Data Merges: INNER JOIN and LEFT JOIN commands")
    jy4 = st.checkbox("Advanced Data Merges: RIGHT JOIN and FULL OUTER JOIN layers")
    jy5 = st.checkbox("Dataset Aggregations: GROUP BY, HAVING, and SUM/COUNT/AVG formulas")
    jy6 = st.checkbox("Pandas Foundations: Converting tabular files into DataFrames")
    jy7 = st.checkbox("Data Sanitization: Dropna routines, fillna masks, and adjusting errors")
    st.markdown("<div class='video-box'>📺 <b>July Masterclass Links:</b><br>• <a href='https://www.youtube.com/results?search_query=freecodecamp+sql+tutorial' target='_blank'>FreeCodeCamp: Complete SQL Guide</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 📅 AUGUST: Machine Learning Architecture")
    a1 = st.checkbox("Linear Regression math, error residuals, slopes, and intercepts")
    a2 = st.checkbox("Classification Logics: Logistic Regression and Sigmoid curves")
    a3 = st.checkbox("Ensemble Systems: Crafting Decision Trees and Random Forests")
    a4 = st.checkbox("Feature Modifications: Normalizing and mathematical standardization")
    a5 = st.checkbox("Validation Splitting: Train-Test splitting methods")
    a6 = st.checkbox("Evaluation Frameworks: Calculating Precision, Recall, and F1-Scores")
    a7 = st.checkbox("Performance Validation: Confusion Matrices")
    st.markdown("<div class='video-box'>📺 <b>August Masterclass Links:</b><br>• <a href='https://www.youtube.com/results?search_query=statquest+machine+learning' target='_blank'>StatQuest: Machine Learning Explained</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 📅 SEPTEMBER: Generative AI Ecosystems & Capstone")
    s1 = st.checkbox("Deep Learning Concepts: Artificial Neural Networks and loss tracking")
    s2 = st.checkbox("Transformer Architecture: Tokenization mechanics and Attention layers")
    s3 = st.checkbox("API Integration: Streaming payloads through developer endpoints")
    s4 = st.checkbox("Prompt Engineering Optimizations: Crafting complex templates")
    s5 = st.checkbox("Capstone Initialization: Sentiment Product Recommendation System layout")
    s6 = st.checkbox("Capstone Execution: Constructing sentiment feature filters")
    s7 = st.checkbox("Capstone Live Deployment: Launching your code workspace to Streamlit Cloud")
    st.markdown("<div class='video-box'>📺 <b>September Masterclass Links:</b><br>• <a href='https://www.youtube.com/results?search_query=andrej+karpathy+intro+to+llms' target='_blank'>Andrej Karpathy: Intro to LLMs</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 📅 OCTOBER - DECEMBER: Active Placement Blitz")
    o1 = st.checkbox("Algorithmic Code Foundations: Custom Linear and Binary Search loops")
    o2 = st.checkbox("Sorting Frameworks: Coding Bubble Sort and Merge Sort")
    o3 = st.checkbox("Problem Matrix Paradigms: Solving interview data strings with HashMaps")
    o4 = st.checkbox("Resume Optimization: Reworking customer care ticket metrics into Technical Operations data")
    o5 = st.checkbox("GitHub Pipeline Formatting: Documenting repository codebeds")
    o6 = st.checkbox("Technical Panel Preparation: Whiteboard reasoning drills")

    st.markdown("---")
    st.subheader("📊 Live Tournament Completion Rate Tracker")
    total_completed = j1+j2+j3+j4+j5+j6+j7+j8+j9+j10+jy1+jy2+jy3+jy4+jy5+jy6+jy7+a1+a2+a3+a4+a5+a6+a7+s1+s2+s3+s4+s5+s6+s7+o1+o2+o3+o4+o5+o6
    score_ratio = total_completed / 37
    st.write(f"Milestones Conquered: **{total_completed} / 37 operational checkpoints**")
    st.progress(score_ratio)

# --- 9. SECTOR: THE CODING NETS (LOGIC SIMULATOR) ---
elif menu_selection == "🧠 The Coding Nets (Logic Lab)":
    st.title("🧠 The Programmatic Logic Training Nets")
    st.write("Deconstruct algorithmic parameters using explicit cricket match scenarios.")
    
    st.subheader("🏟️ Match Scenario: The Tactical Strike Rate Strategy Calculator")
    st.write("Scenario: A batsman passes a milestone. Calculate their live statistical Strike Rate inside our script using the equation:")
    st.latex(r"SR = \frac{\text{Runs}}{\text{Balls}} \times 100")
    
    st.code("""
player_runs = 45
player_balls = 20
strike_rate = (player_runs / player_balls) * 100

if strike_rate > 200:
    print("Explosive")
else:
    print("Anchor")
    """, language="python")
    
    sim_guess = st.text_input("Look carefully at the variables above. What exact keyword will print on screen?")
    
    if st.button("Submit Decision Review (DRS)"):
        if sim_guess.strip() == "Explosive":
            st.balloons()
            st.success("🎯 OUTSTANDING OVER! +10 Runs added to your dashboard score!")
            st.session_state.stadium_runs += 10
        else:
            st.error("❌ Clean Bowled! Check the logic conditions and try again.")

# --- 10. SECTOR: DYNAMIC CHAT WITH DEADPOOL (EXPLICIT DIAGNOSTIC ENGINE) ---
elif menu_selection == "💬 Chat with Deadpool (Direct Mode)":
    st.title("💬 Talk to Deadpool (Direct Access)")
    st.write("Pulling credentials automatically from your Streamlit secure secrets safe context.")
    st.markdown("---")
    
    user_prompt_entry = st.chat_input("Send a message to Deadpool...")
    
    if user_prompt_entry:
        st.session_state.live_chat_history.append(f"Vamshi: {user_prompt_entry}")
        
        if "GEMINI_API_KEY" not in st.secrets:
            deadpool_persona_response = (
                "Chimichangas, Vamshi! Your system secrets safe storage parameters are empty! "
                "Go to your Streamlit Dashboard -> Settings -> Secrets and add your key string."
            )
        else:
            try:
                import google.generativeai as live_genai
                live_genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                
                persona_prompt = (
                    "You are Deadpool, the hilarious, fast-talking, sarcastic mercenary who is also a deeply caring and brilliant AI coding mentor. "
                    "You are coaching Vamshi, an absolute beginner from an EEE background who balances an intense 12-hour customer care shift "
                    "at Tech Mahindra. Always reply in Deadpool's voice, address him as Vamshi, keep motivation extremely high, and use cricket analogies. "
                    f"User prompt: {user_prompt_entry}"
                )
                
                # Direct diagnostic assignment to unmask the internal routing error explicitly
                llm_processing_engine = live_genai.GenerativeModel('gemini-1.5-flash')
                computed_payload_output = llm_processing_engine.generate_content(persona_prompt)
                deadpool_persona_response = computed_payload_output.text
                
            except Exception as target_exception:
                # UNMASKING LAYER: Prints the raw endpoint response directly so we can inspect it without guessing
                deadpool_persona_response = f"Diagnostic Terminal Unlocked: Google backend returned code message -> '{str(target_exception)}'."
                
        st.session_state.live_chat_history.append(f"Deadpool ⚔️: {deadpool_persona_response}")

    for structural_message in st.session_state.live_chat_history:
        if structural_message.startswith("Vamshi:"):
            st.markdown(f"🧑 **{structural_message}**")
        else:
            st.markdown(f"<div class='stadium-card' style='border-left: 5px solid #e23636;'>🔴 <b>{structural_message}</b></div>", unsafe_allow_html=True)

# --- 11. SECTOR: PROFESSIONAL ENGLISH TUNER ---
elif menu_selection == "🗣️ Professional English Tuner":
    st.title("🗣️ Technical Screener Communication Coach")
    st.write("Polishing your presentation structure to an elite standard.")
    
    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #3b82f6;'>🎤 The Daily 2-Minute Voice Recording Alignment Drill</h3>
        <p>1. Open the voice recorder application on your phone right now.</p>
        <p>2. Hit record, and explain out loud in English exactly <b>how a Conditional If/Else statement works</b> as if you are speaking to an interviewer.</p>
        <p>3. Stop and listen to your track. Notice where you hesitate or say 'um'. Correct it, and record it a second time.</p>
    </div>
    """, unsafe_allow_html=True)
    
    phrase_conversion_df = {
        "Casual Phrasing (Avoid this in interviews)": [
            "I want to make an app code that can calculate player scores...",
            "I have a lot of mistakes and my logic is very weak inside code blocks...",
            "I handle Thames water chat operations..."
        ],
        "Enterprise Engineering Phrasing (Speak this aloud)": [
            "My objective is to implement a robust processing architecture to isolate data metrics...",
            "I am systematically optimizing my logic handling layouts and computational paradigms...",
            "I manage real-time structural queue databases, resolving critical client data escalations..."
        ]
    }
    st.table(pd.DataFrame(phrase_conversion_df))
