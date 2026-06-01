import streamlit as st
import datetime
import pandas as pd
import time

# --- 1. PREMIUM ARENA CONFIGURATION ---
st.set_page_config(
    page_title="Vamshi's Deadpool AI Stadium 2026",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. PREMIUM NEON CRIMSON & CHARCOAL THEME (HIGH INTERACTIVE) ---
st.markdown("""
    <style>
    /* Full Stadium Cyber Dark Background */
    .stApp {
        background: radial-gradient(circle at center, #1e0505 0%, #000000 100%);
        color: #f8fafc;
    }
    
    /* The Dugout Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #110202 !important;
        border-right: 3px solid #e23636;
    }
    
    /* Tactical Crimson Neon Cards */
    .stadium-card {
        background: linear-gradient(135deg, #2d0a0a 0%, #0d0202 100%);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #e23636;
        box-shadow: 0 0 25px rgba(226, 54, 54, 0.3);
        margin-bottom: 25px;
    }
    
    .video-box {
        background: #0f172a;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #3b82f6;
        margin-top: 10px;
    }
    
    /* Power-Hitter Interactive Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #e23636 0%, #991b1b 100%);
        color: white;
        border: 1px solid #ffffff;
        border-radius: 50px;
        padding: 12px 28px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        transition: 0.3s all ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 35px rgba(226, 54, 54, 0.7);
    }
    
    h1, h2, h3, h4 {
        color: #e23636;
        font-family: 'Impact', 'Arial Black', sans-serif;
        letter-spacing: 2px;
    }
    
    .gold-glow {
        color: #fbbf24;
        text-shadow: 0 0 10px rgba(251, 191, 36, 0.6);
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PERSISTENT SYSTEM STATE ARRAYS ---
if 'streak_counter' not in st.session_state: st.session_state.streak_counter = 1
if 'stadium_runs' not in st.session_state: st.session_state.stadium_runs = 0
if 'live_chat_history' not in st.session_state: st.session_state.live_chat_history = []

# --- 4. TIMELINE ANCHORS ---
current_match_day = datetime.date(2026, 6, 1) # System Launch Date
interview_match_day = datetime.date(2026, 10, 1)
world_cup_deadline = datetime.date(2026, 12, 31)

# --- 5. SIDEBAR NAVIGATION COMMAND PAVILION ---
st.sidebar.markdown("<h1 style='text-align: center; color: #e23636;'>⚔️ DEADPOOL AI</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #9ca3af;'><b>PLAYER: VAMSHI THE ALL-ROUNDER</b></p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown(f"🔥 **Current Win Streak:** `{st.session_state.streak_counter} Matches`")
if st.sidebar.button("🏏 LOG PRACTICE INNINGS"):
    st.session_state.streak_counter += 1
    st.sidebar.success("Streak Saved! Keep going.")

menu_selection = st.sidebar.radio("CHOOSE SECTOR:", [
    "🏟️ The Pavilion (Dashboard)",
    "📅 Complete 7-Month Roadmap",
    "📊 Master Progress Scorecard",
    "🧠 The Coding Nets (Logic Lab)",
    "💬 Chat with Deadpool (API Mode)",
    "🗣️ Professional English Tuner"
])

# --- 6. SECTOR: THE PAVILION (DASHBOARD) ---
if menu_selection == "🏟️ The Pavilion (Dashboard)":
    st.title("🏟️ THE MAIN COMMAND PAVILION")
    st.write("Wankhede Stadium under neon lights. Today is June 1, 2026. Your comeback innings starts right now.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='stadium-card'><h5>Days to October 1st Finals</h5><h2 class='gold-glow'>{(interview_match_day - current_match_day).days} Days</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='stadium-card'><h5>Current Title Rank</h5><h2 style='color: #3b82f6;'>Pace All-Rounder ⚡</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='stadium-card'><h5>Your Stadium Score</h5><h2 style='color: #10b981;'>{st.session_state.stadium_runs} Runs</h2></div>", unsafe_allow_html=True)

    st.subheader("🔋 Post-Shift Fatigue Strategy Optimizer")
    energy_input = st.select_slider("What is your human processing power right now?", options=["0% (Dead Exhausted)", "25% (Fatigued)", "50% (Steady)", "100% (Match Ready)"])
    
    if "0%" in energy_input:
        st.error("🚨 Fatigue Boundary Reached! Do not type code tonight. Open the 'Chat with Deadpool' tab, read one quick analogy to protect your mindset, get your 7 hours of sleep, and rest.")
    elif "25%" in energy_input:
        st.warning("⚡ Low Energy. Spend 15 minutes checking off items on the Master Scorecard and watch one short embedded YouTube link.")
    else:
        st.success("🔥 Powerplay active! Open 'The Coding Nets' and crush the logic simulator quiz right now.")

    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #e23636;'>⚔️ Deadpool's Corner</h3>
        <p><i>"Look, Vamshi. You are 23 years old. You handle customer care chat processes and intense escalations for 12 hours a day. That means your brain is already built to solve broken problems under extreme pressure. AI engineering isn't magic; it's just telling a machine how to filter and handle options step-by-step. Let's make this comeback real. Maximum Effort."</i></p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. SECTOR: THE COMPLETE 7-MONTH ROADMAP ---
elif menu_selection == "📅 Complete 7-Month Roadmap":
    st.title("📅 The 2026 Professional Career Transition Roadmap")
    st.write("Your month-by-month tournament layout. No shortcuts, no fluff.")
    
    st.markdown("""
    <div class='stadium-card'>
        <h3>🏏 PHASE 1: THE NETS PRACTICE (June - July)</h3>
        <p><b>Objective:</b> Build pure algorithmic thinking and data management patterns from absolute zero.</p>
        <ul>
            <li><b>June:</b> Python Variables, Logic Loops, Arrays, Conditionals, and Functional blueprints.</li>
            <li><b>July:</b> SQL Relational Database Queries, Multi-table Joins, and Pandas analytical DataFrames.</li>
        </ul>
    </div>
    
    <div class='stadium-card'>
        <h3>🎯 PHASE 2: THE ACCELERATED RUN RATE (August - September)</h3>
        <p><b>Objective:</b> Master mathematical prediction models and 'Magical' Generative AI architectures.</p>
        <ul>
            <li><b>August:</b> Linear & Logistic Regression, Decision Trees, Random Forests, and Scikit-Learn pipelines.</li>
            <li><b>September:</b> Neural Networks, Large Language Models (LLMs), Prompt Engineering, and Capstone Project completion.</li>
        </ul>
    </div>
    
    <div class='stadium-card'>
        <h3>🏆 PHASE 3: THE WORLD CUP FINALS (October - December)</h3>
        <p><b>Objective:</b> Active interview execution, portfolio deployment, and landing the offer letter.</p>
        <ul>
            <li><b>October 1st:</b> Launch applications. Review sorting routines, data structures, and rewrite resume metrics.</li>
            <li><b>Nov - Dec:</b> Run live coding mocks, clear interview panels, and secure the junior AI/ML engineer role.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- 8. SECTOR: THE COMPLETE INTERACTIVE SYLLABUS TRACKER ---
elif menu_selection == "📊 Master Progress Scorecard":
    st.title("📊 Complete 7-Month Interactive Progress Scorecard")
    st.write("Every single technical topic from June 1st to December 31st typed out. Check them off as you conquer them.")

    # --- JUNE CHECKBOXES ---
    st.markdown("### 📅 JUNE: Python Core & Logic Foundations")
    j1 = st.checkbox("Variables, Core Memory Buckets & Object Naming Guidelines")
    j2 = st.checkbox("Data Types: Integers, Floating Vectors, Strings, and Boolean States")
    j3 = st.checkbox("Comparison Mechanics: Evaluating Truth values (==, !=, >, <)")
    j4 = st.checkbox("Logical Operators: Linking multiple conditions together (AND, OR, NOT)")
    j5 = st.checkbox("Conditional Architectures: Writing nested If, Elif, and Else branches")
    j6 = st.checkbox("Iteration Control: For Loops (Processing definite data arrays)")
    j7 = st.checkbox("Conditional Control: While Loops (Iterating until conditions fail)")
    j8 = st.checkbox("Data Layouts Part 1: Python Lists (Slicing, indexing, and appending variables)")
    j9 = st.checkbox("Data Layouts Part 2: Dictionaries (Key-Value map data layouts)")
    j10 = st.checkbox("Functional Programming: Defining reusable functions, processing arguments, and return scope")
    st.markdown("<div class='video-box'>📺 <b>June Masterclass Video Links:</b><br>"
                "• <a href='[https://www.youtube.com/results?search_query=freecodecamp+python+full+course](https://www.youtube.com/results?search_query=freecodecamp+python+full+course)' target='_blank'>FreeCodeCamp: Python Foundational Programming Masterclass</a><br>"
                "• <a href='[https://www.youtube.com/results?search_query=corey+schafer+python+beginner](https://www.youtube.com/results?search_query=corey+schafer+python+beginner)' target='_blank'>Corey Schafer: Production-Grade Python Playlist</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # --- JULY CHECKBOXES ---
    st.markdown("### 📅 JULY: Relational Databases & Data Manipulation")
    jy1 = st.checkbox("Relational Architecture: Database patterns, schemas, and relational tables")
    jy2 = st.checkbox("Query Selection: Writing extractions with SELECT, WHERE, LIKE, and IN constraints")
    jy3 = st.checkbox("Relational Joins: Merging table blocks via INNER JOIN and LEFT JOIN structures")
    jy4 = st.checkbox("Advanced Relational Joins: Processing RIGHT JOIN and FULL OUTER JOIN matrices")
    jy5 = st.checkbox("Data Groupings: Harnessing GROUP BY, HAVING, and aggregations (SUM, COUNT, AVG)")
    jy6 = st.checkbox("Pandas Engineering: Loading dataset tables into speed-optimized Series and DataFrames")
    jy7 = st.checkbox("Data Cleansing Arrays: Treating missing data rows, null variables, and formatting bugs")
    st.markdown("<div class='video-box'>📺 <b>July Masterclass Video Links:</b><br>"
                "• <a href='[https://www.youtube.com/results?search_query=freecodecamp+sql+tutorial](https://www.youtube.com/results?search_query=freecodecamp+sql+tutorial)' target='_blank'>FreeCodeCamp: Complete Structured Query Language Guide</a><br>"
                "• <a href='[https://www.youtube.com/results?search_query=keith+galli+pandas](https://www.youtube.com/results?search_query=keith+galli+pandas)' target='_blank'>Keith Galli: Complete Pandas Data Wrangling Tutorial</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # --- AUGUST CHECKBOXES ---
    st.markdown("### 📅 AUGUST: Core Machine Learning Pipelines")
    a1 = st.checkbox("Supervised Equations: Linear Regression math, slopes, intercepts, and continuous paths")
    a2 = st.checkbox("Classification Methods: Logistic Regression mathematical boundaries & Sigmoid metrics")
    a3 = st.checkbox("Tree Paradigms: Building Decision Trees and running Random Forest ensembles")
    a4 = st.checkbox("Feature Transformations: Normalizing, standardizing, and scaling numerical columns")
    a5 = st.checkbox("Validation Splitting: Train-Test splitting methods and protecting validation states")
    a6 = st.checkbox("Evaluation Frameworks: Precision, Recall, and calculating unified F1-Scores")
    a7 = st.checkbox("The Performance Matrix: Structuring Confusion Matrices to map prediction anomalies")
    st.markdown("<div class='video-box'>📺 <b>August Masterclass Video Links:</b><br>"
                "• <a href='[https://www.youtube.com/results?search_query=statquest+machine+learning](https://www.youtube.com/results?search_query=statquest+machine+learning)' target='_blank'>StatQuest: Machine Learning Fundamentals Explained Visually</a><br>"
                "• <a href='[https://www.youtube.com/results?search_query=programming+with+mosh+machine+learning](https://www.youtube.com/results?search_query=programming+with+mosh+machine+learning)' target='_blank'>Programming with Mosh: Python Machine Learning Basics</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # --- SEPTEMBER CHECKBOXES ---
    st.markdown("### 📅 SEPTEMBER: Generative AI Foundations & Capstone Delivery")
    s1 = st.checkbox("Deep Learning Mechanics: Neural Networks, interconnected weights, biases, and activation nodes")
    s2 = st.checkbox("Transformer Architecture: Attention mechanics, text tokenization, and context sequence tracking")
    s3 = st.checkbox("API Integration: Connecting and sending payloads through OpenAI and Google Gemini developer tools")
    s4 = st.checkbox("Prompt Engineering Optimizations: System role setups, few-shot conditioning, and structure enforcement")
    s5 = st.checkbox("Capstone Initialization: Planning parsing structures for the Sentiment-Based Product Recommendation System")
    s6 = st.checkbox("Capstone Development: Building text classification code to process and catch customer sentiments")
    s7 = st.checkbox("Capstone Hosting: Packing, debugging, and deploying your complete final system onto Streamlit Cloud")
    st.markdown("<div class='video-box'>📺 <b>September Masterclass Video Links:</b><br>"
                "• <a href='[https://www.youtube.com/results?search_query=andrej+karpathy+intro+to+llms](https://www.youtube.com/results?search_query=andrej+karpathy+intro+to+llms)' target='_blank'>Andrej Karpathy: Intro to Modern Large Language Models</a><br>"
                "• <a href='[https://www.youtube.com/results?search_query=freecodecamp+langchain](https://www.youtube.com/results?search_query=freecodecamp+langchain)' target='_blank'>FreeCodeCamp: Generative AI Application Development Masterclass</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # --- OCTOBER TO DECEMBER CHECKBOXES ---
    st.markdown("### 📅 OCTOBER - DECEMBER: Strategic Placement Blitz")
    o1 = st.checkbox("Algorithmic Basics: Implementing basic Linear Search and high-speed Binary Search loops")
    o2 = st.checkbox("Sorting Routines: Coding Bubble Sort, Merge Sort, and tracking execution complexities")
    o3 = st.checkbox("Interview Core Structures: Solving problem matrix layouts using Arrays, Strings, and quick HashMaps")
    o4 = st.checkbox("Resume Remodeling: Turning previous customer support and ticket management metrics into Technical Operations")
    o5 = st.checkbox("Portfolio Presentation: Deploying cleanly documented coding repositories directly onto your GitHub profile")
    o6 = st.checkbox("Live Interview Strategy: Talking through your logic cleanly during whiteboard coding panels")
    st.markdown("<div class='video-box'>📺 <b>October Masterclass Video Links:</b><br>"
                "• <a href='[https://www.youtube.com/results?search_query=freecodecamp+data+structures+and+algorithms](https://www.youtube.com/results?search_query=freecodecamp+data+structures+and+algorithms)' target='_blank'>FreeCodeCamp: Data Structures and Algorithms Full Course</a><br>"
                "• <a href='[https://www.youtube.com/results?search_query=ml+engineer+interview+questions](https://www.youtube.com/results?search_query=ml+engineer+interview+questions)' target='_blank'>Tech Interview Pro: Cracking the Technical AI Engineer Screener</a></div>", unsafe_allow_html=True)

    # MASTER CALCULATION
    st.markdown("---")
    st.subheader("📊 Live Mastery Percentage Tracker")
    total_ticked = j1+j2+j3+j4+j5+j6+j7+j8+j9+j10+jy1+jy2+jy3+jy4+jy5+jy6+jy7+a1+a2+a3+a4+a5+a6+a7+s1+s2+s3+s4+s5+s6+s7+o1+o2+o3+o4+o5+o6
    score_ratio = total_ticked / 37
    st.write(f"Championship Objectives Conquered: **{total_ticked} / 37 items**")
    st.progress(score_ratio)

# --- 9. SECTOR: THE CODING NETS (LOGIC SIMULATOR) ---
elif menu_selection == "🧠 The Coding Nets (Logic Lab)":
    st.title("🧠 The Interactive Logic Training Ground")
    st.write("Learn how code parameters work using pure cricket rules. No boring math textbooks.")
    
    st.markdown("""
    ### 🛠️ Problem Solving Strategy: The 'DRS' Mental Engine
    *   **D (Define Inputs):** Identify the raw metrics you hold inside your variable buckets.
    *   **R (Refine Conditions):** Isolate the exact boundaries of the rule (e.g. tracking boundaries).
    *   **S (Solve Sequentially):** Plan out your tracking logic step-by-step before writing a single character of code.
    """)
    
    st.subheader("🏟️ Interactive Challenge: The Net Run Rate Threshold Filter")
    st.write("Scenario: A league team wraps up their season. We hold their evaluated **Net Run Rate (NRR)** inside a variable.")
    st.write("If their NRR is strictly higher than `+1.50`, our logic must return `'Qualifiers'`. If it is lower, it returns `'Knocked Out'`.")
    
    st.code("""
# Inspect the script layout:
team_nrr = 1.85

if team_nrr > 1.50:
    print("Qualifiers")
else:
    print("Knocked Out")
    """, language="python")
    
    st.subheader("🕹️ Live Execution Simulator")
    sim_guess = st.text_input("Look closely at the script blocks above. What exact word will print on the screen when Python executes this code?")
    
    if st.button("Submit Decision Review (DRS)"):
        if sim_guess.strip() == "Qualifiers":
            st.balloons()
            st.success("🎯 BOUNDARY! Superb reading, Vamshi. Because 1.85 is greater than 1.50, the condition checks out true and executes the first option. You scored +10 Runs!")
            st.session_state.stadium_runs += 10
        elif sim_guess.strip() == "":
            st.warning("Type your solution choice into the text input block first.")
        else:
            st.error("❌ Clean Bowled! Let's re-read line 4: Is 1.85 higher than 1.50? Yes, it is! So Python skips the 'else' block and hits the first print. Correct your spelling and hit submit again!")

# --- 10. SECTOR: LIVE CHAT WITH DEADPOOL (SAFE IMPORT DESIGN) ---
elif menu_selection == "💬 Chat with Deadpool (API Mode)":
    st.title("💬 Open-Ended Chat Workspace with Deadpool")
    st.write("No limited choices or annoying dropdowns. Ask anything you want—coding logic, data systems, general knowledge, or cricket metrics.")
    
    secure_api_key = st.text_input("🗝️ Enter Google Gemini API Key to activate Deadpool live:", type="password")
    st.markdown("---")
    
    user_chat_input = st.chat_input("Ask Deadpool anything...")
    
    if user_chat_input:
        st.session_state.live_chat_history.append(f"Vamshi: {user_chat_input}")
        
        if secure_api_key:
            try:
                # SAFE LOCAL IMPORT ENGINE
                import google.generativeai as live_genai
                live_genai.configure(api_key=secure_api_key)
                llm_engine = live_genai.GenerativeModel('gemini-1.5-flash')
                
                payload_instructions = (
                    "You are Deadpool, the hilarious, fast-talking, sarcastic mercenary who is also a deeply caring and brilliant AI coding mentor. "
                    "You are coaching Vamshi, an absolute beginner from an EEE background who works an exhausting 12-hour customer care shift "
                    "at Tech Mahindra. Always reply in Deadpool's voice, address him as Vamshi, keep motivation extremely high, and use cricket analogies whenever explaining complex ideas. "
                    f"User prompt: {user_chat_input}"
                )
                model_output = llm_engine.generate_content(payload_instructions)
                ai_reply = model_output.text
            except Exception as e:
                ai_reply = f"Chimichangas! I tried running that logic but the API server returned an error: {str(e)}. Make sure your key is fresh, kid!"
        else:
            ai_reply = (
                "Hey Vamshi! I am currently running in Offline Mode because you haven't pasted your free Google API key into the field above yet! "
                "No stress. Go to Google AI Studio, grab a free developer key, paste it here, and my full live mouthy brain will unlock. "
                "Until then, remember: Today is June 1st. Day 1. Focus on your logic targets, stay at the crease, and let's win this match!"
            )
            
        st.session_state.live_chat_history.append(f"Deadpool ⚔️: {ai_reply}")

    for message_block in st.session_state.live_chat_history:
        if message_block.startswith("Vamshi:"):
            st.markdown(f"🧑 **{message_block}**")
        else:
            st.markdown(f"<div class='stadium-card' style='border-left: 4px solid #e23636;'>🔴 <b>{message_block}</b></div>", unsafe_allow_html=True)

# --- 11. SECTOR: PROFESSIONAL ENGLISH TUNER ---
elif menu_selection == "🗣️ Professional English Tuner":
    st.title("🗣️ The Tech Interview Communication Tuner")
    st.write("Refining your verbal communication from a 5/10 baseline up to an elite **8/10 technical interview standard**.")
    
    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #3b82f6;'>🎤 The Daily 2-Minute Vocal Performance Routine</h3>
        <p>1. Open the default voice recording application on your mobile phone right now.</p>
        <p>2. Press record, and explain out loud in English exactly <b>what an If/Else block does</b> as if you are speaking directly to a technical recruiter.</p>
        <p>3. Play the track back. Notice where you hesitate or say 'um'. Fix that specific phrase structure and record it a second time. Doing this daily builds fluency twice as fast as reading books.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📋 Executive Technical Vocabulary Matrix")
    st.write("Review this table before interviews to replace casual phrasing with clean engineering language:")
    
    phrase_data = {
        "Casual Phrase (Avoid this in interviews)": [
            "I want to do a code that can calculate player scores...",
            "I have a lot of mistakes and my logic is very weak inside code blocks...",
            "I wasted a lot of time before and now I want to start fresh..."
        ],
        "Enterprise Engineering Phrase (Speak this aloud)": [
            "My objective is to implement a robust processing architecture to isolate data metrics...",
            "I am systematically optimizing my logic handling layouts and computational paradigms...",
            "I am strategically re-aligning my technical progression roadmap from Day 1 onward..."
        ]
    }
    st.table(pd.DataFrame(phrase_data))
