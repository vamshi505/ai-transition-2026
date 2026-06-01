import streamlit as str_layout
import datetime
import pandas as pd
import google.generativeai as gemini_ai

# --- 1. PREMIUM ARENA ARCHITECTURE ---
str_layout.set_page_config(
    page_title="Vamshi's Deadpool AI Stadium 2026",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. MAXIMUM EFFORT NEON CRIMSON & CHARCOAL THEME ---
str_layout.markdown("""
    <style>
    /* Full Stadium Dark Mode */
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #000000 100%);
        color: #f8fafc;
    }
    
    /* The Dugout Sidebar */
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
        box-shadow: 0 0 25px rgba(226, 54, 54, 0.25);
        margin-bottom: 25px;
    }
    
    .video-box {
        background: #111827;
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
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 30px rgba(226, 54, 54, 0.6);
    }
    
    h1, h2, h3 {
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

# --- 3. CORE COGNITIVE SYSTEM STATE ---
if 'streak_counter' not in str_layout.session_state: str_layout.session_state.streak_counter = 1
if 'stadium_runs' not in str_layout.session_state: str_layout.session_state.stadium_runs = 0
if 'live_chat_history' not in str_layout.session_state: str_layout.session_state.live_chat_history = []

# --- 4. TIMELINE ANCHORS ---
start_match_day = datetime.date(2026, 6, 1)
current_match_day = datetime.date(2026, 6, 1) # Forced System Time
interview_match_day = datetime.date(2026, 10, 1)
world_cup_deadline = datetime.date(2026, 12, 31)

# --- 5. SIDEBAR CONTROL CENTER ---
str_layout.sidebar.markdown("<h1 style='text-align: center; color: #e23636;'>⚔️ DEADPOOL AI</h1>", unsafe_allow_html=True)
str_layout.sidebar.markdown("<p style='text-align: center; color: #9ca3af;'><b>PLAYER: VAMSHI THE ALL-ROUNDER</b></p>", unsafe_allow_html=True)
str_layout.sidebar.markdown("---")

str_layout.sidebar.markdown(f"🔥 **Current Streak:** `{str_layout.session_state.streak_counter} Days Continuous`")
if str_layout.sidebar.button("🏏 LOG DAILY PRACTICE"):
    str_layout.session_state.streak_counter += 1
    str_layout.sidebar.success("Innings saved! Streak increased.")

menu_selection = str_layout.sidebar.radio("CHOOSE SECTOR:", [
    "🏟️ The Pavilion (Dashboard)",
    "📊 Complete 7-Month Scorecard",
    "🧠 The Coding Nets (Simulator)",
    "💬 Chat with Deadpool (API Mode)",
    "🗣️ Professional English Tuner"
])

# --- 6. SECTOR: THE PAVILION (DASHBOARD) ---
if menu_selection == "🏟️ The Pavilion (Dashboard)":
    str_layout.title("🏟️ THE MAIN PAVILION")
    str_layout.write("Wankhede Stadium under the neon lights. The scoreboard is clean. Time to shine.")
    
    col1, col2, col3 = str_layout.columns(3)
    with col1:
        str_layout.markdown(f"<div class='stadium-card'><h5>Days to October 1st Finals</h5><h2 class='gold-glow'>{(interview_match_day - current_match_day).days} Days</h2></div>", unsafe_allow_html=True)
    with col2:
        str_layout.markdown("<div class='stadium-card'><h5>Current Title</h5><h2 style='color: #3b82f6;'>Pace All-Rounder ⚡</h2></div>", unsafe_allow_html=True)
    with col3:
        str_layout.markdown(f"<div class='stadium-card'><h5>Stadium Score</h5><h2 style='color: #10b981;'>{str_layout.session_state.stadium_runs} Runs</h2></div>", unsafe_allow_html=True)

    str_layout.subheader("🔋 Post-Shift Fatigue Strategy Optimizer")
    energy_input = str_layout.select_slider("What is your human processing power right now?", options=["0% (Dead Exhausted)", "25% (Fatigued)", "50% (Steady)", "100% (Match Ready)"])
    
    if "0%" in energy_input:
        str_layout.error("🚨 Brain battery low. Do not try complex data modeling tonight. Head over to the **'Chat with Deadpool'** tab, ask a quick text question, clean up your headspace, and get your solid 7 hours of sleep.")
    elif "25%" in energy_input:
        str_layout.warning("⚡ Fatigue detected. Open the **'Complete 7-Month Scorecard'** tab, review the expanders for 15 minutes, and click one of the pre-linked YouTube searches.")
    else:
        str_layout.success("🔥 Powerplay active! Dive into **'The Coding Nets'** and execute the interactive logic scenarios.")

    str_layout.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #e23636;'>⚔️ Deadpool's Corner</h3>
        <p><i>"Look, Vamshi. You are 23. You manage customer escalations and chat operations during intense shifts—that means your brain is already wired to handle messy data errors and angry parameters under pressure. AI engineering isn't a magic spell; it's just telling a computer how to handle parameters step-by-step. Let's get to work. Maximum Effort."</i></p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. SECTOR: THE COMPLETE 7-MONTH SYLLABUS SCORECARD ---
elif menu_selection == "📊 Complete 7-Month Scorecard":
    str_layout.title("📊 The Complete 7-Month Interactive Progress Scorecard")
    str_layout.write("Every single milestone from June 1st to December 31st explicitly built out. Check them off as you conquer them.")

    # JUNE
    with str_layout.expander("📅 PHASE 1: JUNE — Python Logic Foundations (The Opening Stand)"):
        str_layout.markdown("##### 🚀 Foundational Milestones:")
        j1 = str_layout.checkbox("Memory Allocation: Variables, Core Objects & Naming Conventions")
        j2 = str_layout.checkbox("Data Structures: Integers, Floating Vectors, Text Strings, and Booleans")
        j3 = str_layout.checkbox("Comparison Mechanics: Evaluating Truth States (==, !=, >, <)")
        j4 = str_layout.checkbox("Logical Operators: Chaining Structural Conditions (AND, OR, NOT)")
        j5 = str_layout.checkbox("Conditional Trees: Implementation of complex If, Elif, and Else branches")
        j6 = str_layout.checkbox("Iteration Loops: For Loops (Processing definite numerical sequences)")
        j7 = str_layout.checkbox("Conditional Loops: While Loops (Iterating until structural criteria is reached)")
        j8 = str_layout.checkbox("Data Layouts Part 1: Python Lists (Slicing, structural indexing, appending arrays)")
        j9 = str_layout.checkbox("Data Layouts Part 2: Dictionaries (Key-Value map data optimization)")
        j10 = str_layout.checkbox("Functional Blueprints: Defining modular functions, processing parameters, and return statements")
        
        str_layout.markdown("<div class='video-box'>📺 <b>High-Dopamine Video Resources:</b><br>"
                            "• <a href='https://www.youtube.com/results?search_query=freecodecamp+python+for+beginners+full+course' target='_blank'>FreeCodeCamp: Python Foundational Programming Masterclass</a><br>"
                            "• <a href='https://www.youtube.com/results?search_query=corey+schafer+python+playlist' target='_blank'>Corey Schafer: Production-Grade Python Tutorials</a></div>", unsafe_allow_html=True)

    # JULY
    with str_layout.expander("📅 PHASE 2: JULY — Relational Databases & SQL Processing (The Middle Overs)"):
        str_layout.markdown("##### 🚀 Foundational Milestones:")
        jy1 = str_layout.checkbox("Relational Architecture: Database design, schemas, and structural tables")
        jy2 = str_layout.checkbox("Query Selection: Extraction arrays with SELECT, WHERE, LIKE, and IN boundaries")
        jy3 = str_layout.checkbox("Relational Joins: Merging data via INNER JOIN and LEFT JOIN structures")
        jy4 = str_layout.checkbox("Advanced Data Merging: Harnessing RIGHT JOIN and FULL OUTER JOIN matrices")
        jy5 = str_layout.checkbox("Data Groupings: Organizing datasets using GROUP BY, HAVING, and aggregate formulas (SUM, COUNT, AVG)")
        jy6 = str_layout.checkbox("Pandas Engineering: Translating tables into high-speed Series and DataFrames")
        jy7 = str_layout.checkbox("Data Cleansing: Structural dropna, fillna, and treating data format discrepancies")
        
        str_layout.markdown("<div class='video-box'>📺 <b>High-Dopamine Video Resources:</b><br>"
                            "• <a href='https://www.youtube.com/results?search_query=freecodecamp+sql+tutorial+for+beginners' target='_blank'>FreeCodeCamp: Complete Structured Query Language Guide</a><br>"
                            "• <a href='https://www.youtube.com/results?search_query=keith+galli+pandas+tutorial' target='_blank'>Keith Galli: Comprehensive Pandas Data Analysis Training</a></div>", unsafe_allow_html=True)

    # AUGUST
    with str_layout.expander("📅 PHASE 3: AUGUST — Machine Learning Pipelines (The Accelerated Run Rate)"):
        str_layout.markdown("##### 🚀 Foundational Milestones:")
        a1 = str_layout.checkbox("Supervised Equations: Linear Regression mechanics, slopes, intercepts, and continuous outputs")
        a2 = str_layout.checkbox("Classification Methods: Logistic Regression mathematical boundaries & Sigmoid optimization")
        a3 = str_layout.checkbox("Tree Architectures: Structuring Decision Trees and running Random Forest ensembles")
        a4 = str_layout.checkbox("Feature Scaling: Standardizing and normalizing varied input data bounds")
        a5 = str_layout.checkbox("Validation Splitting: Train-Test splitting strategies and protecting model validation states")
        a6 = str_layout.checkbox("Evaluation Frameworks: Precision vs Recall equations and calculating F1-Scores")
        a7 = str_layout.checkbox("The Performance Matrix: Structuring Confusion Matrices to capture false positives/negatives")
        
        str_layout.markdown("<div class='video-box'>📺 <b>High-Dopamine Video Resources:</b><br>"
                            "• <a href='https://www.youtube.com/results?search_query=statquest+machine+learning' target='_blank'>StatQuest: Machine Learning Foundations Broken Down Visually</a><br>"
                            "• <a href='https://www.youtube.com/results?search_query=programming+with+mosh+machine+learning' target='_blank'>Programming with Mosh: Practical Machine Learning Essentials</a></div>", unsafe_allow_html=True)

    # SEPTEMBER
    with str_layout.expander("📅 PHASE 4: SEPTEMBER — Generative AI & Capstone Deployment (The Death Overs)"):
        str_layout.markdown("##### 🚀 Foundational Milestones:")
        s1 = str_layout.checkbox("Deep Learning Mechanics: Artificial Neural Networks, processing nodes, and activation layers")
        s2 = str_layout.checkbox("Transformer Architecture: Attention layers, computational tokenization, and structural context text processing")
        s3 = str_layout.checkbox("API Engineering: Ingesting live operational endpoints from OpenAI and Google Gemini")
        s4 = str_layout.checkbox("System Prompt Architecture: Few-shot prompting strategies and enforcing system personas")
        s5 = str_layout.checkbox("Capstone Phase 1: Planning text parsing loops for the Sentiment-Based Product Recommendation System")
        s6 = str_layout.checkbox("Capstone Phase 2: Processing text data strings to isolate client sentiment categories")
        s7 = str_layout.checkbox("Capstone Phase 3: Packaging and deploying your completed model live onto Streamlit Cloud platforms")
        
        str_layout.markdown("<div class='video-box'>📺 <b>High-Dopamine Video Resources:</b><br>"
                            "• <a href='https://www.youtube.com/results?search_query=andrej+karpathy+intro+to+llms' target='_blank'>Andrej Karpathy: Introduction to Modern Large Language Models</a><br>"
                            "• <a href='https://www.youtube.com/results?search_query=freecodecamp+generative+ai+course' target='_blank'>FreeCodeCamp: Comprehensive Generative AI Application Engineering</a></div>", unsafe_allow_html=True)

    # OCTOBER - DECEMBER
    with str_layout.expander("📅 PHASE 5: OCTOBER - DECEMBER — Strategic Placement Blitz (Lifting The Trophy)"):
        str_layout.markdown("##### 🚀 Foundational Milestones:")
        o1 = str_layout.checkbox("Search Algorithms: Writing programmatic Linear Search and optimized Binary Search models")
        o2 = str_layout.checkbox("Sorting Paradigms: Mechanics of Bubble Sort, Merge Sort, and evaluating execution granularities")
        o3 = str_layout.checkbox("Interview Core Structures: Managing data sequences cleanly using Arrays, Strings, and quick HashMaps")
        o4 = str_layout.checkbox("Resume Remodeling: Structuring previous support experience into technical Data Engineering metrics")
        o5 = str_layout.checkbox("GitHub Pipeline Polish: Organizing well-documented repositories to showcase to hiring engineering leads")
        o6 = str_layout.checkbox("Live Screener Simulations: Tackling whiteboards and talking through code logic under pressure")
        
        str_layout.markdown("<div class='video-box'>📺 <b>High-Dopamine Video Resources:</b><br>"
                            "• <a href='https://www.youtube.com/results?search_query=freecodecamp+data+structures+and+algorithms' target='_blank'>FreeCodeCamp: Data Structures and Algorithms Deep Dive</a><br>"
                            "• <a href='https://www.youtube.com/results?search_query=tech+interview+pro+coding+interview' target='_blank'>Tech Interview Pro: Cracking Advanced Technical Screening Boards</a></div>", unsafe_allow_html=True)

    # LIVE COMPLETION COUNTER
    str_layout.markdown("---")
    str_layout.subheader("🏆 Live Championship Mastery Progress")
    checked_items = j1+j2+j3+j4+j5+j6+j7+j8+j9+j10+jy1+jy2+jy3+jy4+jy5+jy6+jy7+a1+a2+a3+a4+a5+a6+a7+s1+s2+s3+s4+s5+s6+s7+o1+o2+o3+o4+o5+o6
    final_ratio = checked_items / 37
    str_layout.write(f"Syllabus Objectives Unlocked: **{checked_items} / 37 modules**")
    str_layout.progress(final_ratio)

# --- 8. SECTOR: THE CODING NETS (LOGIC SIMULATOR) ---
elif menu_selection == "🧠 The Coding Nets (Simulator)":
    str_layout.title("🧠 The Interactive Logic Playground")
    str_layout.write("Refining your data logic structures without worrying about spelling or syntax bugs.")
    
    str_layout.markdown("""
    ### 🛠️ Problem Solving Strategy: The 'DRS' Engine
    *   **D (Define Inputs):** Isolate the variables you hold inside your program's memory banks.
    *   **R (Refine Conditions):** Define the exact rules of the match scenario (e.g. tracking boundaries).
    *   **S (Solve Sequentially):** Plan out the tracking steps in clean words before writing functional lines.
    """)
    
    str_layout.subheader("🏟️ Match Scenario: The Net Run Rate Threshold Optimizer")
    str_layout.write("Scenario: A team finishes their chasing innings. We hold their calculated **Net Run Rate (NRR)** inside a memory bucket.")
    str_layout.write("If their final NRR value is strictly higher than `+1.50`, our script needs to flag them as `'Qualifiers'`. If it is lower, it flags them as `'Knocked Out'`.")
    
    str_layout.code("""
# Let's inspect the conceptual code logic:
team_nrr = 1.85

if team_nrr > 1.50:
    print("Qualifiers")
else:
    print("Knocked Out")
    """, language="python")
    
    str_layout.subheader("🕹️ Live Execution Simulator")
    sim_answer = str_layout.text_input("Look closely at the script above. What word will print on the screen when Python executes this code block? (Type it exactly):")
    
    if str_layout.button("Submit Decision Review (DRS)"):
        if sim_answer.strip() == "Qualifiers":
            str_layout.balloons()
            str_layout.success("🎯 BOUNDARY! Splendid reading. Because 1.85 is greater than 1.50, the condition resolves true and outputs 'Qualifiers'. You earned 10 Runs!")
            str_layout.session_state.stadium_runs += 10
        elif sim_answer.strip() == "":
            str_layout.warning("Type your target solution into the input slot first.")
        else:
            st_layout.error("❌ Clean bowled! Let's re-read line 4: Is 1.85 greater than 1.50? Yes. So Python bypasses the 'else' block and targets the first print statement. Type the correct word to retry!")

# --- 9. SECTOR: OPEN-ENDED CHAT WITH DEADPOOL (LIVE API MODEL) ---
elif menu_selection == "💬 Chat with Deadpool (API Mode)":
    str_layout.title("💬 Open-Ended Chat Workspace with Deadpool")
    str_layout.write("No pre-baked dropdowns. Ask anything you want—coding logic, data architecture, general knowledge, or cricket stats. It is an open arena.")
    
    # User inputs their API Key securely right inside the interface
    custom_gemini_key = str_layout.text_input("🗝️ Optional: Paste your Google Gemini API Key below to unlock live data processing power:", type="password")
    
    str_layout.markdown("---")
    str_layout.write("💬 **Conversation Arena**")
    
    user_prompt_input = str_layout.chat_input("Ask Deadpool anything (e.g., 'Explain array index values using cricket field settings'...)")
    
    if user_prompt_input:
        str_layout.session_state.live_chat_history.append(f"Vamshi: {user_prompt_input}")
        
        if custom_gemini_key:
            try:
                gemini_ai.configure(api_key=custom_gemini_key)
                text_generation_engine = gemini_ai.GenerativeModel('gemini-pro')
                ai_query_payload = (
                    "You are Deadpool, the hilarious, fast-talking, sarcastic mercenary who is also a deeply supportive and brilliant AI coding mentor. "
                    "You are coaching Vamshi, an absolute beginner from an EEE background who balances a 12-hour customer care shift while mastering Python and AI. "
                    "Always reply in Deadpool's voice, address him as Vamshi, keep motivation extremely high, and use cricket analogies whenever explaining complex ideas. "
                    f"User prompt: {user_prompt_input}"
                )
                computed_response = text_generation_engine.generate_content(ai_query_payload)
                deadpool_reply = computed_response.text
            except Exception as system_fault:
                deadpool_reply = f"Chimichangas! I tried hitting that ball out of the stadium, but the API network thrown an error: {str(system_fault)}. Double-check your key configuration, kid!"
        else:
            # High-fidelity offline fallback persona response
            deadpool_reply = (
                "Hey Vamshi! I am currently running in Offline Mode because you haven't plugged in your secure Google API key at the top of the tab yet! "
                "But let me give you a quick Deadpool baseline advice anyway: whatever question you just typed, break it down like a T20 chase. "
                "If it's about python logic, isolate the variables first. If you are feeling exhausted after your shift, go rest! "
                "Grab a free key from Google AI Studio, paste it above, and my full mouthy brain will answer your prompt live!"
            )
            
        str_layout.session_state.live_chat_history.append(f"Deadpool ⚔️: {deadpool_reply}")
        
    for statement in str_layout.session_state.live_chat_history:
        if statement.startswith("Vamshi:"):
            str_layout.markdown(f"🧑 **{statement}**")
        else:
            str_layout.markdown(f"<div class='stadium-card' style='border-left: 4px solid #e23636;'>🔴 <b>{statement}</b></div>", unsafe_allow_html=True)

# --- 10. SECTOR: PROFESSIONAL ENGLISH TUNER ---
elif menu_selection == "🗣️ Professional English Tuner":
    str_layout.title("🗣️ The Technical Interview Communication Tuner")
    str_layout.write("Transforming your verbal structure from a 5/10 baseline up to an elite **8/10 interview standard** through simple daily routines.")
    
    str_layout.markdown("""
    <div class='stadium-card'>
        <h3 style='color: #3b82f6;'>🎤 The 2-Minute Vocal Performance Routine</h3>
        <p>1. Open your smartphone's built-in voice recorder application right now.</p>
        <p>2. Hit record, and explain out loud in English exactly <b>what a For Loop does</b> as if you are speaking directly to a senior recruiter.</p>
        <p>3. Play back your voice recording. Track your hesitations. Identify where you lose clarity, correct one word choice, and record it a second time. This technique eliminates voice anxiety twice as fast as a textbook.</p>
    </div>
    """, unsafe_allow_html=True)
    
    str_layout.subheader("📋 Executive Technical Transformation Matrix")
    str_layout.write("Review this table before interviews to replace casual explanations with elite engineering language:")
    
    transformation_matrix = {
        "Casual Phrase (What you want to avoid)": [
            "I want to make an app code that can find standard scores...",
            "I have a lot of problems making my logic work inside variables...",
            "I missed a lot of time before and now I want to start fresh..."
        ],
        "Enterprise Engineering Phrase (What to speak aloud)": [
            "My target is to implement a modular processing architecture to isolate data metrics...",
            "I am programmatically refining my logical processing design and variable handling paradigms...",
            "I am strategically re-aligning my data modeling timeline from Day 1 onward..."
        ]
    }
    str_layout.table(pd.DataFrame(transformation_matrix))
