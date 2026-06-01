import streamlit as st
import datetime
import pandas as pd

# --- 1. PREMIUM STADIUM CONFIGURATION ---
st.set_page_config(
    page_title="Vamshi's AI Master Arena 2026",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CYBER-STADIUM HIGH-DOPAMINE UI ---
st.markdown("""
    <style>
    /* Dark Neon Stadium Aesthetics */
    .stApp {
        background: radial-gradient(circle at top, #0f172a 0%, #020617 100%);
        color: #f8fafc;
    }
    section[data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 3px solid #10b981;
    }
    .stadium-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #10b981;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.2);
        margin-bottom: 25px;
    }
    .video-card {
        background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #6366f1;
        margin-top: 10px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #10b981 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 12px 28px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 20px rgba(37, 99, 235, 0.5);
    }
    .neon-gold {
        color: #f59e0b;
        font-weight: bold;
        text-shadow: 0 0 8px rgba(245, 158, 11, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PERSISTENT SYSTEM STATE ---
if 'streak_count' not in st.session_state: st.session_state.streak_count = 1
if 'interactive_score' not in st.session_state: st.session_state.interactive_score = 0
if 'ai_response' not in st.session_state: st.session_state.ai_response = ""

# --- 4. TIMELINE CALCULATIONS ---
timeline_start = datetime.date(2026, 6, 1)
current_date = datetime.date(2026, 6, 1) # Forced timeline anchor
interview_deadline = datetime.date(2026, 10, 1)
final_target_date = datetime.date(2026, 12, 31)
days_to_interviews = (interview_deadline - current_date).days

# --- 5. SIDEBAR NAVIGATION CONTROLS ---
st.sidebar.markdown("<h1 style='text-align: center; color: #10b981;'>🏟️ MATCH DAY</h1>", unsafe_allow_html=True)
st.sidebar.markdown(f"<p style='text-align: center;'><b>Vamshi 'The Pace All-Rounder'</b></p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown(f"🔥 **Current Streak:** `{st.session_state.streak_count} Days`")
if st.sidebar.button("🏏 Log Daily Practice Session"):
    st.session_state.streak_count += 1
    st.sidebar.success("Innings logged! Keep pushing.")

sector = st.sidebar.radio("CHOOSE HUB:", [
    "🏠 The Pavilion (Dashboard)",
    "📊 Master Scorecard (All Checkboxes)",
    "🧠 The Coding Nets (Simulator)",
    "🤖 Embedded AI Mentor Bot",
    "🗣️ Professional English Tuner"
])

# --- 6. SECTOR: THE PAVILION (DASHBOARD) ---
if sector == "🏠 The Pavilion (Dashboard)":
    st.title("🏟️ The Main Career Pavilion")
    st.write("Wankhede Stadium Under The Lights. Today is **June 1, 2026**. Your second innings begins now.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='stadium-card'><h5>Days to Interview Season</h5><h2 class='neon-gold'>{days_to_interviews} Days</h2></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='stadium-card'><h5>Current Mastery Tier</h5><h2 style='color: #3b82f6;'>Absolute Zero 🎯</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='stadium-card'><h5>Simulator Score</h5><h2 style='color: #10b981;'>{st.session_state.interactive_score} Runs</h2></div>", unsafe_allow_html=True)

    st.subheader("🔋 Shift Fatigue Strategy Optimizer")
    energy_level = st.select_slider("What is your physical battery level right now?", options=["0% (Exhausted)", "25% (Fatigued)", "50% (Steady)", "100% (Match Ready)"])
    
    if "0%" in energy_level:
        st.error("🚨 Brain fatigue boundary reached. Do not type code code tonight. Go to the 'Embedded AI Mentor Bot' tab, read one quick tactical explanation, get your 7 hours of sleep, and rest.")
    elif "25%" in energy_level:
        st.warning("⚡ Low energy warning. Spend 15 minutes reviewing the 'Master Scorecard' expanders and watch one short linked YouTube summary.")
    else:
        st.success("🔥 Powerplay active! Open 'The Coding Nets' and run the code simulator logic.")

    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #10b981;'>🛡️ Mentor Voice</h3>
        <p><i>"Vamshi, handling chat processes and escalations means your brain is already built to solve complex problems under immense pressure. That is exactly what an AI Engineer does. We aren't starting from scratch—we are just migrating your processing power from non-IT into Python logic. Trust the system."</i></p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. SECTOR: MASTER SCORECARD (ALL CHECKBOXES + YOUTUBE ARENA) ---
elif sector == "📊 Master Scorecard (All Checkboxes)":
    st.title("📊 Complete 7-Month Interactive Syllabus Tracker")
    st.write("Every single checkbox from June 1st to December 31st, complete with highest-rated YouTube learning tracks. No placeholders.")

    # --- JUNE ---
    with st.expander("📅 JUNE: Python Logic Foundations (The Opening Stand)"):
        st.markdown("##### 🚀 Technical Targets:")
        j1 = st.checkbox("Variables, Data Types (Integers, Strings, Booleans) & Memory Storage Concepts")
        j2 = st.checkbox("Comparison Operators (==, !=, >, <) & Logical Statements (AND, OR, NOT)")
        j3 = st.checkbox("Conditional Processing Architectures (If, Elif, Else blocks)")
        j4 = st.checkbox("Control Flow Loops (For loops over sequences, While loop criteria)")
        j5 = st.checkbox("Iterating Data Layouts (Nested loops, breaking out of loops)")
        j6 = st.checkbox("Data Collections Part 1: Lists (Appending, slicing, indexing arrays)")
        j7 = st.checkbox("Data Collections Part 2: Dictionaries (Key-Value structural indexing)")
        j8 = st.checkbox("Functional Programming: Defining functions, positional arguments, and return variables")
        
        st.markdown("<div class='video-card'>📺 <b>Top-Rated Video Tracks:</b><br>"
                    "• <a href='https://www.youtube.com/results?search_query=freecodecamp+python+full+course' target='_blank'>FreeCodeCamp: Complete Python Masterclass</a><br>"
                    "• <a href='https://www.youtube.com/results?search_query=corey+schafer+python+beginner' target='_blank'>Corey Schafer: Beginner Python Series</a></div>", unsafe_allow_html=True)

    # --- JULY ---
    with st.expander("📅 JULY: Relational Databases & Data Manipulation (The Strike Rotation)"):
        st.markdown("##### 🚀 Technical Targets:")
        jy1 = st.checkbox("Relational Database Fundamentals & SQL Syntax Structure")
        jy2 = st.checkbox("Filtering Rows with SELECT, WHERE, LIKE, and IN statements")
        jy3 = st.checkbox("Data Merging: INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN")
        jy4 = st.checkbox("Aggregations: GROUP BY, HAVING, and mathematical modifiers (SUM, AVG, COUNT)")
        jy5 = st.checkbox("Pandas Framework: Series, DataFrames, and indexing multidimensional objects")
        jy6 = st.checkbox("Pandas Row Operations: Filtering condition layouts, applying custom lambda formulas")
        jy7 = st.checkbox("Data Sanitization: Dropping null variables, filling empty metrics, treating column errors")
        
        st.markdown("<div class='video-card'>📺 <b>Top-Rated Video Tracks:</b><br>"
                    "• <a href='https://www.youtube.com/results?search_query=freecodecamp+sql+tutorial' target='_blank'>FreeCodeCamp: SQL Database Programming Tutorial</a><br>"
                    "• <a href='https://www.youtube.com/results?search_query=keith+galli+pandas' target='_blank'>Keith Galli: Complete Python Pandas Playlist</a></div>", unsafe_allow_html=True)

    # --- AUGUST ---
    with st.expander("📅 AUGUST: Core Machine Learning Pipelines (The Accelerated Run Rate)"):
        st.markdown("##### 🚀 Technical Targets:")
        a1 = st.checkbox("Supervised Learning: Linear Regression mathematical structures (Slopes & Intercepts)")
        a2 = st.checkbox("Classification Pipelines: Logistic Regression & Sigmoid Curve weights")
        a3 = st.checkbox("Tree Paradigms: Decision Trees, node splitting choices, and Random Forests")
        a4 = st.checkbox("Feature Engineering: Normalization, Standardization, and scaling data columns")
        a5 = st.checkbox("Model Training Routines: Train-Test splitting variables and cross-validation indexes")
        a6 = st.checkbox("Evaluation Mathematics: Deep understanding of Accuracy, Precision, Recall, and F1-Score")
        a7 = st.checkbox("The Confusion Matrix: Identifying true positives, true negatives, and type-I/II errors")
        
        st.markdown("<div class='video-card'>📺 <b>Top-Rated Video Tracks:</b><br>"
                    "• <a href='https://www.youtube.com/results?search_query=statquest+machine+learning+basics' target='_blank'>StatQuest: Machine Learning Fundamentals Explained</a><br>"
                    "• <a href='https://www.youtube.com/results?search_query=programming+with+mosh+machine+learning' target='_blank'>Programming with Mosh: Python Machine Learning for Beginners</a></div>", unsafe_allow_html=True)

    # --- SEPTEMBER ---
    with st.expander("📅 SEPTEMBER: Generative AI Foundations & Capstone Delivery (The Death Overs)"):
        st.markdown("##### 🚀 Technical Targets:")
        s1 = st.checkbox("Deep Learning Mechanics: Artificial Neural Networks, weights, biases, and activation nodes")
        s2 = st.checkbox("Large Language Models (LLMs): Understanding Tokenization, Attention layers, and context frames")
        s3 = st.checkbox("API Protocols: Connecting and streaming prompts through OpenAI and Google Gemini developer endpoints")
        s4 = st.checkbox("Prompt Engineering Optimizations: Few-shot context guidance and system persona architecture")
        s5 = st.checkbox("Capstone Initialization: Designing the layout of your Sentiment-Based Product Recommendation System")
        s6 = st.checkbox("Capstone Execution: Building text feature extractions to isolate buyer sentiments")
        s7 = st.checkbox("Capstone Hosting: Deploying your finalized AI system code to Streamlit Cloud platforms")
        
        st.markdown("<div class='video-card'>📺 <b>Top-Rated Video Tracks:</b><br>"
                    "• <a href='https://www.youtube.com/results?search_query=andrej+karpathy+intro+to+llms' target='_blank'>Andrej Karpathy: Intro to Large Language Models</a><br>"
                    "• <a href='https://www.youtube.com/results?search_query=freecodecamp+langchain' target='_blank'>FreeCodeCamp: Generative AI & LangChain Framework Masterclass</a></div>", unsafe_allow_html=True)

    # --- OCTOBER TO DECEMBER ---
    with st.expander("📅 OCTOBER - DECEMBER: Strategic Placement Blitz (Lifting The Trophy)"):
        st.markdown("##### 🚀 Technical Targets:")
        o1 = st.checkbox("Algorithmic Logic 101: Linear and Binary Search implementations")
        o2 = st.checkbox("Data Sorting Systems: Bubble sort math, Merge sort routines, and runtime granularities")
        o3 = st.checkbox("Data Structures Prep: Tracking operations using Arrays, Strings, and fast HashMaps")
        o4 = st.checkbox("Resume Architecture: Striking out non-IT text; framing your chat experience as Data Wrangling")
        o5 = st.checkbox("Portfolio Polish: Uploading clean, well-documented codebases onto GitHub repositories")
        o6 = st.checkbox("Interview Simulations: Running mock developer panels and answering system design boards")
        
        st.markdown("<div class='video-card'>📺 <b>Top-Rated Video Tracks:</b><br>"
                    "• <a href='https://www.youtube.com/results?search_query=freecodecamp+data+structures+and+algorithms' target='_blank'>FreeCodeCamp: Data Structures and Algorithms Deep Dive</a><br>"
                    "• <a href='https://www.youtube.com/results?search_query=luffie+codes+ai+ml+interview+prep' target='_blank'>Tech Interview Pro: Cracking the AI/ML Developer Screening</a></div>", unsafe_allow_html=True)

    # --- OVERALL MASTERY CALCULATION ---
    st.markdown("---")
    st.subheader("📊 Live Championship Completion Rate")
    total_boxes = j1+j2+j3+j4+j5+j6+j7+j8+jy1+jy2+jy3+jy4+jy5+jy6+jy7+a1+a2+a3+a4+a5+a6+a7+s1+s2+s3+s4+s5+s6+s7+o1+o2+o3+o4+o5+o6
    completion_rate = total_boxes / 35
    st.write(f"Syllabus Modules Mastered: **{total_boxes} / 35**")
    st.progress(completion_rate)

# --- 8. SECTOR: THE CODING NETS (SIMULATOR) ---
elif sector == "🧠 The Coding Nets (Simulator)":
    st.title("🧠 The Interactive Logic Simulation Ground")
    st.write("Build your code logic step-by-step through pure cricket scenarios. No boring textbook math.")
    
    st.markdown("""
    ### 🛠️ Problem Solving Technique: The 'DRS' Mental Engine
    *   **D (Define Inputs):** Identify the raw variables you hold in your code memory bucket.
    *   **R (Refine Conditions):** Define the exact rules of the scenario (e.g. boundary boundaries).
    *   **S (Solve Sequentially):** Write down the operations ball-by-ball before typing syntax.
    """)
    
    st.subheader("🏟️ Dynamic Match Challenge: The Strike Rate Decision Tracker")
    st.write("Scenario: You have a player who scored **45 runs** off **20 balls**. We need to calculate their strike rate using the formula:")
    st.latex(r"StrikeRate = \frac{Runs}{Balls} \times 100")
    st.write("If their Strike Rate is strictly greater than 200, our system must output `'Explosive'`. Otherwise, it outputs `'Normal'`.")
    
    st.code("""
# Let's write the conceptual blueprint out:
runs = 45
balls = 20
strike_rate = (runs / balls) * 100

if strike_rate > 200:
    print("Explosive")
else:
    print("Normal")
    """, language="python")
    
    st.subheader("🕹️ Live Validation Simulator")
    user_input = st.text_input("Look closely at the code variables above. What will Python output when this script executes? (Type the exact word):")
    
    if st.button("Submit Umpire Review (DRS)"):
        if user_input.strip() == "Explosive":
            st.balloons()
            st.success("🎯 OUTSTANDING SHOT! 45 runs in 20 balls equals a Strike Rate of 225.0, which is over 200. You scored 10 runs!")
            st.session_state.interactive_score += 10
        elif user_input.strip() == "":
            st.warning("Please type your answer in the box first.")
        else:
            st.error("❌ Dot ball! Let's recalculate: 45 divided by 20 is 2.25. Multiply by 100 equals 225. Is 225 greater than 200? Try typing the correct condition word!")

# --- 9. SECTOR: EMBEDDED AI MENTOR BOT ---
elif sector == "🤖 Embedded AI Mentor Bot":
    st.title("🤖 Your Virtual On-Demand AI Mentor")
    st.write("Struggling with a technical block or feeling low after your long shift? Enter your problem, and let's break down the logic together instantly.")
    
    mentor_topics = st.selectbox("Select what is blocking you tonight:", [
        "Select Topic",
        "I feel overwhelmed by my 12-hour shift and feel like giving up.",
        "Explain Python Loops using a simple cricket over analogy.",
        "What is the 'Magic' inside Large Language Models (LLMs)?",
        "How do I explain my customer care escalation work on an AI resume?"
    ])
    
    if st.button("Consult Mentor Blueprint"):
        if mentor_topics == "I feel overwhelmed by my 12-hour shift and feel like giving up.":
            st.session_state.ai_response = (
                "Take a deep breath, Vamshi. Working from 5 PM to 5 AM or grinding out 12 hours straight means your resilience is already higher than 95% of people entering tech. "
                "You are 23. You have a long, powerful career ahead of you. When energy is low, do not force code loops. "
                "Just read two commuter flashcards or log into your dashboard to protect your daily streak. The match isn't won in a single over—it's won by staying at the crease."
            )
        elif mentor_topics == "Explain Python Loops using a simple cricket over analogy.":
            st.session_state.ai_response = (
                "Think of a Python 'For Loop' as an Umpire counting the balls in an over. An over has a set sequence of 6 balls. "
                "Instead of rewriting the code to score each ball manually, you tell Python: 'For each ball in this over, check if a run was scored, add it to the scoreboard, and move to the next ball.' "
                "The loop repeats the exact same instructions 6 times automatically and then stops. Loop code is just an automated over counter!"
            )
        elif mentor_topics == "What is the 'Magic' inside Large Language Models (LLMs)?":
            st.session_state.ai_response = (
                "The 'magic' is just advanced sequence prediction. Imagine a cricket commentator who has memorized every single match played over the last 100 years. "
                "When a bowler runs in, the commentator knows exactly what probability statement to make next based on thousands of past records. "
                "LLMs don't 'think' like humans—they evaluate massive probability arrays to predict the absolute best next word in a sentence structure."
            )
        elif mentor_topics == "How do I explain my customer care escalation work on an AI resume?":
            st.session_state.ai_response = (
                "Never say 'I just answered customer queries.' On an AI resume, you frame it like a Data Analyst: "
                "'Managed structural user queue databases, filtered anomaly escalation logs under high-pressure parameters, and implemented root-cause classification logic to reduce resolution latency.' "
                "It's the exact same job, but written in the language of a tech professional."
            )
        else:
            st.session_state.ai_response = "Please select a valid blueprint option to activate the mentor file."

    if st.session_state.ai_response:
        st.markdown(f"""
        <div class='stadium-card' style='border-left: 5px solid #2563eb;'>
            <h4>💬 Mentor Response File:</h4>
            <p style='line-height: 1.6; font-size: 1.1em;'>{st.session_state.ai_response}</p>
        </div>
        """, unsafe_allow_html=True)

# --- 10. SECTOR: PROFESSIONAL ENGLISH TUNER ---
elif sector == "🗣️ Professional English Tuner":
    st.title("🗣️ The Tech Interview Communication Tuner")
    st.write("Your communication is clear enough to frame excellent code intent, but we need to refine your structure from a 5/10 to an **8/10** to smash tech interview screens.")
    
    st.markdown("""
    <div class='stadium-card'>
        <h3>🎤 The Daily 2-Minute Vocal Alignment Drill</h3>
        <p>1. Open the voice recording application on your mobile device right now.</p>
        <p>2. Press record, and explain the concept of an <b>'If/Else Statement'</b> aloud in English for 2 minutes straight without pausing.</p>
        <p>3. Listen to your track. Notice where you hesitate or say 'um'. Correct one structural phrasing, and record it a second time.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔧 Modern Transformation Dictionary")
    st.write("Replace casual words with high-impact engineering vocabulary during your study blocks:")
    
    conversion_data = {
        "What you might say casually": ["I want to make a code that fixes...", "I am very weak in building logic...", "I wasted time and want to start over..."],
        "What to say to an interviewer": ["My objective is to implement an optimization algorithm that resolves...", "I am systemically refining my programmatic problem-solving paradigms...", "I am strategically re-aligning my technical pipeline targets from Day 1..."]
    }
    st.table(pd.DataFrame(conversion_data))
