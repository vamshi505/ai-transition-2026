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

st.sidebar.markdown(f"🔥 **Current Win Streak:** `{st.session_state.streak_counter} Matches`")
if st.sidebar.button("🏏 LOG DAILY TRAINING SESSION"):
    st.session_state.streak_counter += 1
    st.sidebar.success("Session logged cleanly onto the scoreboard!")

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

    st.subheader("🔋 Shift Fatigue Strategy Balancer")
    energy_input = st.select_slider("What is your physical baseline battery level after work?", options=["0% (Dead Exhausted)", "25% (Fatigued)", "50% (Steady)", "100% (Match Ready)"])
    
    if "0%" in energy_input:
        st.error("🚨 Critical Fatigue Detected. Do not write complex loops tonight. Head over to the 'Chat with Deadpool' tab, ask a text question to review a logic analogy, get your 7 hours of sleep, and rest.")
    elif "25%" in energy_input:
        st.warning("⚡ Low energy warning. Spend 15 minutes checking off finished items in the Master Scorecard and review one short pre-linked YouTube track.")
    else:
        st.success("🔥 Powerplay active! Open 'The Coding Nets' and crush the logic simulator engine right now.")

    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #e23636;'>⚔️ Deadpool's Mentorship Blueprint</h3>
        <p><i>"Listen to me, Vamshi. You manage real-time customer care chat processes and critical escalations for 12 hours straight at Tech Mahindra. That means your brain is already hardened to filter bad input data and solve edge-case errors under maximum pressure. Transitioning to AI is exactly the same—we are just moving your manual processing speed into clean Python data tracks. Let's get to work. Maximum Effort."</i></p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. SECTOR: COMPLETE 7-MONTH ROADMAP ---
elif menu_selection == "📅 Complete 7-Month Roadmap":
    st.title("📅 The 2026 Professional AI Career Transition Timeline")
    st.write("Your definitive tournament layout from June 1st to December 31st, 2026.")
    
    st.markdown("""
    <div class='stadium-card'>
        <h3>🏏 PHASE 1: THE NETS CLINIC (June — July)</h3>
        <p><b>Objective:</b> Construct pure algorithmic logic frameworks and automated data querying models from absolute scratch.</p>
        <ul>
            <li><b>June:</b> Variable memory boundaries, logic operators, structural conditionals, execution loops, list indexing, and object blueprints.</li>
            <li><b>July:</b> Relational Database engineering, multi-table structural merges, aggregations, and high-speed Pandas DataFrames.</li>
        </ul>
    </div>
    
    <div class='stadium-card'>
        <h3>🎯 PHASE 2: THE MID-OVER RUN RATE EXPLOSION (August — September)</h3>
        <p><b>Objective:</b> Master mathematical predictive scoring algorithms and 'Magical' Generative AI LLM architectures.</p>
        <ul>
            <li><b>August:</b> Linear & Logistic model equations, classification parameters, tree structures, normalization, and Scikit-Learn evaluation arrays.</li>
            <li><b>September:</b> Neural processing networks, Transformer attention layers, live Gemini/OpenAI API parsing loops, and finishing your Sentiment-Based Product Recommendation System.</li>
        </ul>
    </div>
    
    <div class='stadium-card'>
        <h3>🏆 PHASE 3: THE WORLD CUP FINALS PLACEMENT BLITZ (October — December)</h3>
        <p><b>Objective:</b> Scale active company outbound operations, technical presentation polish, and clear recruitment evaluation panels.</p>
        <ul>
            <li><b>October 1st:</b> Launch applications. Review array data structures, sorting complexities, and transform non-IT resume text fields.</li>
            <li><b>November - December:</b> Run production mock panels, clear screening interviews, and lock down your junior AI engineer offer contract.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- 8. SECTOR: THE INTENSE COMPLETE 37-POINT TRACKING MATRIX ---
elif menu_selection == "📊 Master Progress Scorecard":
    st.title("📊 Complete 37-Point Interactive Syllabus Tracker")
    st.write("Every single technical milestone explicitly typed out line-by-line. No shortcuts allowed.")

    # --- JUNE SYLLABUS SECTION (10 CHECKPOINTS) ---
    st.markdown("### 📅 JUNE: Python Core Analytics & Logic Gates")
    j1 = st.checkbox("Memory Mapping: Variable assignments, physical object scoping, and safe tracking conventions")
    j2 = st.checkbox("Data Structural Baselines: Processing Integers, Float vectors, string buffers, and Boolean logic gates")
    j3 = st.checkbox("Comparison Mechanics: Constructing exact logical truth valuations (==, !=, >, <)")
    j4 = st.checkbox("Chained Logical Conditions: Managing variable thresholds via AND, OR, and NOT arguments")
    j5 = st.checkbox("Conditional Selection: Writing multi-branch nested If, Elif, and Else control flows")
    j6 = st.checkbox("Definite Iteration: For Loops (Looping across explicit numerical lists and sequences)")
    j7 = st.checkbox("Indefinite Iteration: While Loops (Looping continuously until operational exit constraints trigger)")
    j8 = st.checkbox("Sequence Layouts: Python Lists (Array manipulation, slice parameters, index retrieval, and list mutation)")
    j9 = st.checkbox("Mapping Arrays: Python Dictionaries (Optimizing structural key-value pairing loops)")
    j10 = st.checkbox("Functional Paradigms: Defining reusable functions, operational arguments, and return variables")
    st.markdown("<div class='video-box'>📺 <b>Top-Rated June Masterclass Video Links:</b><br>"
                "• <a href='https://www.youtube.com/results?search_query=freecodecamp+python+full+course' target='_blank'>FreeCodeCamp: Python Foundational Masterclass Training</a><br>"
                "• <a href='https://www.youtube.com/results?search_query=corey+schafer+python+beginner' target='_blank'>Corey Schafer: Production-Grade Python Beginner Blueprint</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # --- JULY SYLLABUS SECTION (7 CHECKPOINTS) ---
    st.markdown("### 📅 JULY: Relational Data Models & SQL Processing")
    jy1 = st.checkbox("Relational Concepts: Managing structured schemas, schemas design constraints, and data table layouts")
    jy2 = st.checkbox("Data Extraction Queries: Writing automated SELECT loops, WHERE criteria, LIKE filters, and IN parameters")
    jy3 = st.checkbox("Data Merges Part 1: Linking structural data arrays via INNER JOIN and LEFT JOIN commands")
    jy4 = st.checkbox("Data Merges Part 2: Linking data matrices via advanced RIGHT JOIN and FULL OUTER JOIN layers")
    jy5 = st.checkbox("Dataset Aggregations: Using GROUP BY, HAVING thresholds, and tracking metrics via SUM, COUNT, and AVG")
    jy6 = st.checkbox("Pandas Foundations: Converting raw tabular files into memory-efficient Series and DataFrames")
    jy7 = st.checkbox("Data Sanitization: Dropping null coordinates, running fillna masks, and adjusting corrupted data values")
    st.markdown("<div class='video-box'>📺 <b>Top-Rated July Masterclass Video Links:</b><br>"
                "• <a href='https://www.youtube.com/results?search_query=freecodecamp+sql+tutorial' target='_blank'>FreeCodeCamp: Complete Structured Query Language Guide</a><br>"
                "• <a href='https://www.youtube.com/results?search_query=keith+galli+pandas' target='_blank'>Keith Galli: Comprehensive Pandas Data Wrangling Training</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # --- AUGUST SYLLABUS SECTION (7 CHECKPOINTS) ---
    st.markdown("### 📅 AUGUST: Machine Learning Architecture & Feature Engineering")
    a1 = st.checkbox("Supervised Pipelines: Linear Regression math, error residuals, slopes, intercepts, and target paths")
    a2 = st.checkbox("Classification Logics: Logistic Regression parameters, log-odds ratios, and Sigmoid probability curves")
    a3 = st.checkbox("Ensemble Systems: Crafting Decision Trees and aggregating output bounds via Random Forests")
    a4 = st.checkbox("Feature Modifications: Normalizing input bounds, scaling columns, and mathematical standardization")
    a5 = st.checkbox("Validation Splitting: Splitting Train-Test rows and preventing data leaks into training sets")
    a6 = st.checkbox("Evaluation Frameworks: Calculating Precision equations, tracking Recall metrics, and mapping F1-Scores")
    a7 = st.checkbox("Performance Validation: Structuring Confusion Matrices to map prediction anomalies")
    st.markdown("<div class='video-box'>📺 <b>Top-Rated August Masterclass Video Links:</b><br>"
                "• <a href='https://www.youtube.com/results?search_query=statquest+machine+learning' target='_blank'>StatQuest: Machine Learning Math and Concept Layouts Explained Simply</a><br>"
                "• <a href='https://www.youtube.com/results?search_query=programming+with+mosh+machine+learning' target='_blank'>Programming with Mosh: Practical Scikit-Learn Essentials</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # --- SEPTEMBER SYLLABUS SECTION (7 CHECKPOINTS) ---
    st.markdown("### 📅 SEPTEMBER: Generative AI Ecosystems & Capstone Finalization")
    s1 = st.checkbox("Deep Learning Concepts: Artificial Neural Networks, backward loss tracking, weights, and processing activation nodes")
    s2 = st.checkbox("Transformer Architecture: Deep dive into Tokenization mechanics, context vectors, and Attention layers")
    s3 = st.checkbox("API Engineering Ingestion: Streaming secure payload prompts through OpenAI and Google Gemini developer endpoints")
    s4 = st.checkbox("Prompt Engineering Optimizations: Crafting complex few-shot context templates and forcing structural outputs")
    s5 = st.checkbox("Capstone Initialization: Planning text vector mapping loops for your Sentiment Product Recommendation System")
    s6 = st.checkbox("Capstone Execution: Constructing production-grade sentiment feature token filters to parse client review files")
    s7 = st.checkbox("Capstone Live Deployment: Bundling, debugging, and launching your complete code workspace to Streamlit Cloud")
    st.markdown("<div class='video-box'>📺 <b>Top-Rated September Masterclass Video Links:</b><br>"
                "• <a href='https://www.youtube.com/results?search_query=andrej+karpathy+intro+to+llms' target='_blank'>Andrej Karpathy: Introduction to Large Language Models from Scratch</a><br>"
                "• <a href='https://www.youtube.com/results?search_query=freecodecamp+langchain' target='_blank'>FreeCodeCamp: Building Advanced Applications with LangChain & LLM APIs</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    # --- OCTOBER TO DECEMBER SYLLABUS SECTION (6 CHECKPOINTS) ---
    st.markdown("### 📅 OCTOBER - DECEMBER: Enterprise Data Structures & Active Placement")
    o1 = st.checkbox("Algorithmic Code Foundations: Writing custom iterative Linear Search and high-speed Binary Search loops")
    o2 = st.checkbox("Sorting Frameworks: Coding Bubble Sort functions, complex Merge Sort maps, and computing algorithmic runtimes")
    o3 = st.checkbox("Problem Matrix Paradigms: Solving interview data strings cleanly using basic Arrays, Strings, and quick HashMaps")
    o4 = st.checkbox("Resume Optimization: Reworking customer care ticket logging metrics into Technical System operations data")
    o5 = st.checkbox("GitHub Pipeline Formatting: Polishing and documenting clear repository codebeds to present to engineering managers")
    o6 = st.checkbox("Technical Panel Preparation: Whiteboard reasoning drills and talking cleanly through computational choices")
    st.markdown("<div class='video-box'>📺 <b>Top-Rated October Masterclass Video Links:</b><br>"
                "• <a href='https://www.youtube.com/results?search_query=freecodecamp+data+structures+and+algorithms' target='_blank'>FreeCodeCamp: Comprehensive Data Structures and Algorithms Master Course</a><br>"
                "• <a href='https://www.youtube.com/results?search_query=ml+engineer+interview+questions' target='_blank'>Tech Interview Pro: Cracking Enterprise AI Screening Boards Successfully</a></div>", unsafe_allow_html=True)

    # --- MASTER CALCULATION AND PROGRESS GENERATION ---
    st.markdown("---")
    st.subheader("📊 Live Tournament Completion Rate Tracker")
    total_completed = j1+j2+j3+j4+j5+j6+j7+j8+j9+j10+jy1+jy2+jy3+jy4+jy5+jy6+jy7+a1+a2+a3+a4+a5+a6+a7+s1+s2+s3+s4+s5+s6+s7+o1+o2+o3+o4+o5+o6
    score_ratio = total_completed / 37
    st.write(f"Championship Milestones Conquered: **{total_completed} / 37 operational checkpoints**")
    st.progress(score_ratio)

# --- 9. SECTOR: THE CODING NETS (LOGIC SIMULATOR) ---
elif menu_selection == "🧠 The Coding Nets (Logic Lab)":
    st.title("🧠 The Programmatic Logic Training Nets")
    st.write("Deconstruct algorithmic parameters using explicit cricket match scenarios.")
    
    st.markdown("""
    ### 🛠️ Problem Solving Strategy: The 'DRS' Cognitive Engine
    *   **D (Define Inputs):** Isolate the exact metrics stored within your program's variable buckets.
    *   **R (Refine Boundaries):** Define the exact rules of the constraint scenario (e.g. tracking boundaries).
    *   **S (Solve Sequentially):** Map out the data transformation steps in human language before writing programmatic syntax.
    """)
    
    st.subheader("🏟️ Match Scenario: The Tactical Strike Rate Strategy Calculator")
    st.write("Scenario: A batsman passes a milestone. We need to calculate their live statistical Strike Rate inside our script using the equation:")
    st.latex(r"SR = \frac{\text{Runs}}{\text{Balls}} \times 100")
    st.write("If their final computed value is strictly higher than 200, our system must return `'Explosive'`. Otherwise, it returns `'Anchor'`.")
    
    st.code("""
# Let's inspect the automated script block:
player_runs = 45
player_balls = 20
strike_rate = (player_runs / player_balls) * 100

if strike_rate > 200:
    print("Explosive")
else:
    print("Anchor")
    """, language="python")
    
    st.subheader("🕹️ Live Execution Simulator Playground")
    sim_guess = st.text_input("Look carefully at the script variables above. What exact keyword will print on screen when Python executes this block?")
    
    if st.button("Submit Decision Review (DRS)"):
        if sim_guess.strip() == "Explosive":
            st.balloons()
            st.success("🎯 OUTSTANDING OVER! Spot-on reading. Because 45 divided by 20 multiplied by 100 equals 225.0, the condition returns true. +10 Runs added to your dashboard score!")
            st.session_state.stadium_runs += 10
        elif sim_guess.strip() == "":
            st.warning("Type your targeted keyword answer into the simulator input field first.")
        else:
            st.error("❌ Clean Bowled! Let's re-calculate line 4: Is 225.0 higher than 200? Yes! So Python completely skips the 'else' block and targets the first option. Fix your spelling and try again!")

# --- 10. SECTOR: DYNAMIC CHAT WITH DEADPOOL (AUTOMATED STREAMLIT SECRETS MODE) ---
elif menu_selection == "💬 Chat with Deadpool (API Mode)":
    st.title("💬 Automated On-Demand Deadpool AI Workspace")
    st.write("No pre-baked options, text file updates, or manual fields. Type anything you want—AI systems, Python arrays, general knowledge, or cricket analytics.")
    
    st.markdown("---")
    st.write("💬 **Live Conversation Arena**")
    
    user_prompt_entry = st.chat_input("Send a message to Deadpool...")
    
    if user_prompt_entry:
        st.session_state.live_chat_history.append(f"Vamshi: {user_prompt_entry}")
        
        # CORE KEY LAYER EXTRACTION FROM STREAMLIT SECRETS (NO CLUTTERED FIELDS)
        try:
            import google.generativeai as live_genai
            secure_vault_key = st.secrets["GEMINI_API_KEY"]
            live_genai.configure(api_key=secure_vault_key)
            llm_processing_engine = live_genai.GenerativeModel('gemini-1.5-flash')
            
            persona_conditioning_prompt = (
                "You are Deadpool, the hilarious, fast-talking, highly sarcastic mercenary who is also a deeply supportive, expert AI coding mentor. "
                "You are coaching Vamshi, a 23-year-old absolute beginner from an EEE background who balances an intense 12-hour customer care shift "
                "at Tech Mahindra. Always reply using Deadpool's signature voice, address him as Vamshi, keep his motivation at absolute maximum, and frame explanations using clever cricket analogies. "
                f"User query payload: {user_prompt_entry}"
            )
            computed_payload_output = llm_processing_engine.generate_content(persona_conditioning_prompt)
            deadpool_persona_response = computed_payload_output.text
        except Exception as hardware_fault_exception:
            # Clear step instructions in case secret key hasn't been saved in Streamlit settings dashboard yet
            deadpool_persona_response = (
                f"Chimichangas, Vamshi! I tried swinging the bat but my background connection thrown a curveball error: {str(hardware_fault_exception)}. "
                "This means the background 'GEMINI_API_KEY' parameter isn't saved in your Cloud dashboard secrets yet! "
                "Do not touch the code file. Simply click 'Manage App' at the bottom right corner of your running app screen, open Settings, go to Secrets, "
                "and paste your key as: GEMINI_API_KEY = 'your_actual_key_here'. Once saved, I'll be live instantly!"
            )
            
        st.session_state.live_chat_history.append(f"Deadpool ⚔️: {deadpool_persona_response}")

    for structural_message in st.session_state.live_chat_history:
        if structural_message.startswith("Vamshi:"):
            st.markdown(f"🧑 **{structural_message}**")
        else:
            st.markdown(f"<div class='stadium-card' style='border-left: 5px solid #e23636;'>🔴 <b>{structural_message}</b></div>", unsafe_allow_html=True)

# --- 11. SECTOR: PROFESSIONAL ENGLISH TUNER ---
elif menu_selection == "🗣️ Professional English Tuner":
    st.title("🗣️ Technical Screener Communication Coach")
    st.write("Polishing your presentation structure from a 5/10 casual baseline to an elite **8/10 technical developer standard**.")
    
    st.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #3b82f6;'>🎤 The Daily 2-Minute Voice Recording Alignment Drill</h3>
        <p>1. Open the default voice recorder application on your smartphone device right now.</p>
        <p>2. Hit record, and explain out loud in English exactly <b>how a Conditional If/Else statement works</b> as if you are answering an enterprise tech panel lead.</p>
        <p>3. Stop the recording and listen back. Note down every hesitation or instances where you say 'um'. Correct one word phrasing option, and record it a second time. This physical routine builds neural confidence twice as fast as reading books.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📋 Executive Technical Transformation Matrix")
    st.write("Review these phrasing samples before technical conversations to replace conversational habits with engineering structure:")
    
    phrase_conversion_df = {
        "Casual Phrasing (Avoid this in interviews)": [
            "I want to make an app code that can calculate player scores...",
            "I have a lot of mistakes and my logic is very weak inside code blocks...",
            "I missed a lot of time before and now I want to start fresh..."
        ],
        "Enterprise Engineering Phrasing (Speak this aloud)": [
            "My objective is to implement a robust processing architecture to isolate data metrics...",
            "I am systematically optimizing my logic handling layouts and computational paradigms...",
            "I am strategically re-aligning my technical progression roadmap from Day 1 onward..."
        ]
    }
    st.table(pd.DataFrame(phrase_conversion_df))
