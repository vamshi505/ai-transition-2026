import streamlit as st
import datetime
import pandas as pd
import time
import io
import asyncio
import edge_tts

# --- 1. STADIUM ARCHITECTURE & INTEL CONFIGURATION ---
st.set_page_config(
    page_title="Vamshi's Jarvis-Deadpool AI Core",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED PREMIUM CYBER-DARK HUD THEME (NEON CRIMSON & COBALT) ---
st.markdown("""
    <style>
    /* Full Holographic Dark Canvas */
    .stApp {
        background: radial-gradient(circle at center, #140202 0%, #020205 70%, #000000 100%);
        color: #f8fafc;
    }
    
    /* Tactical Sidebar Frame */
    section[data-testid="stSidebar"] {
        background-color: #050000 !important;
        border-right: 3px solid #e23636;
        box-shadow: 5px 0 25px rgba(226, 54, 54, 0.2);
    }
    
    /* Deadpool Crimson HUD Cards */
    .deadpool-card {
        background: linear-gradient(135deg, #2b0808 0%, #0c0101 100%);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #e23636;
        box-shadow: 0 0 25px rgba(226, 54, 54, 0.3);
        margin-bottom: 25px;
    }
    
    /* Jarvis Cobalt Tech Cards */
    .jarvis-card {
        background: linear-gradient(135deg, #07162c 0%, #020710 100%);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #00d2ff;
        box-shadow: 0 0 25px rgba(0, 210, 255, 0.3);
        margin-bottom: 25px;
    }

    .video-box {
        background-color: #070d19;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #1e40af;
        margin-top: 10px;
    }

    /* Kinetic Interface Action Controls */
    .stButton>button {
        background: linear-gradient(90deg, #e23636 0%, #00d2ff 100%);
        color: #ffffff !important;
        border: 1px solid #ffffff !important;
        border-radius: 30px !important;
        padding: 14px 28px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        transition: 0.4s all ease-in-out !important;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.01);
        box-shadow: 0 0 35px rgba(0, 210, 255, 0.6);
    }
    
    h1, h2, h3, h4 {
        font-family: 'Impact', 'Arial Black', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .crimson-txt { color: #e23636; text-shadow: 0 0 10px rgba(226, 54, 54, 0.5); }
    .cobalt-txt { color: #00d2ff; text-shadow: 0 0 10px rgba(0, 210, 255, 0.5); }
    .gold-glow { color: #fbbf24; text-shadow: 0 0 15px rgba(251, 191, 36, 0.7); font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. STATE PARSING ENGINE & LOGIC PERSISTENCE ---
if 'streak' not in st.session_state: st.session_state.streak = 1
if 'runs' not in st.session_state: st.session_state.runs = 0
if 'chat_log' not in st.session_state: st.session_state.chat_log = []

# Initialize interactive checklist variables in state storage
for key_idx in range(1, 38):
    state_key = f"chk_{key_idx}"
    if state_key not in st.session_state:
        st.session_state[state_key] = False

# --- 4. TOURNAMENT SCHEDULE SYSTEM CLOCK ---
today = datetime.date(2026, 6, 1)
interview_season = datetime.date(2026, 10, 1)
goal_deadline = datetime.date(2026, 12, 31)

# --- 5. SIDEBAR: FLIGHT DOCK CONTROL ---
st.sidebar.markdown("<h1 style='text-align: center; color: #e23636;'>⚔️ CORE HUD</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'><b>AGENT MATRIX OVERRIDE: ACTIVE</b></p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown(f"🔥 **Win Streak:** `{st.session_state.streak} Matches`")
if st.sidebar.button("🏏 LOG DAILY PRACTICE INNINGS"):
    st.session_state.streak += 1
    st.sidebar.success("Innings committed to mainframe telemetry!")

nav_choice = st.sidebar.radio("NAVIGATE VECTOR SECTORS:", [
    "🏟️ The Pavilion (Dashboard)",
    "📅 Complete 7-Month Roadmap",
    "📊 Master Progress Scorecard",
    "🧠 The Coding Nets (Logic Lab)",
    "💬 Chat Engine (Dual Agent Voice Mode)",
    "🗣️ Professional English Tuner"
])

# Asynchronous Neural Voice Generator Function
async def generate_neural_audio(text_payload, voice_id):
    communicate = edge_tts.Communicate(text_payload, voice_id)
    audio_buffer = io.BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_buffer.write(chunk["data"])
    audio_buffer.seek(0)
    return audio_buffer

# --- 6. SECTOR: THE PAVILION (DASHBOARD) ---
if nav_choice == "🏟️ The Pavilion (Dashboard)":
    st.title("🏟️ Main Command Pavilion")
    st.write("System Diagnostic Status: Normal. Current date sequence initialized to June 1, 2026.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='deadpool-card'><h5>Days to Selection Trials (Oct 1)</h5><h2 class='gold-glow'>{(interview_season - today).days} Days</h2></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='jarvis-card'><h5>Tactical Combat Tier</h5><h2 class='cobalt-txt'>Pace All-Rounder ⚡</h2></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='deadpool-card'><h5>Accumulated Runs Score</h5><h2 style='color: #10b981;'>{st.session_state.runs} Runs</h2></div>", unsafe_allow_html=True)

    st.subheader("🔋 Post-Shift Fatigue Strategy Matrix")
    energy = st.select_slider("Assess structural human remaining runtime power:", options=["0% (Exhausted)", "25% (Fatigued)", "50% (Steady)", "100% (Match Ready)"])
    
    if "0%" in energy:
        st.error("🚨 CRITICAL FATIGUE LIMIT: Switch to Voice Arena, run a concept summary audit, and engage recovery sleep patterns immediately.")
    elif "25%" in energy:
        st.warning("⚡ LOW POWER: Restrict operations to checking milestones in the Master Scorecard and tracking pre-linked masterclass video logs.")
    else:
        st.success("🔥 POWERPLAY SELECTION: Algorithmic parameters operating at peak capacity. Open 'The Coding Nets' and execute logic models.")

    col_dp, col_jv = st.columns(2)
    with col_dp:
        st.markdown("""
        <div class='deadpool-card'>
            <h3 class='crimson-txt'>⚔️ Deadpool's Corner</h3>
            <p><i>"Vamshi, listen up buddy! You run live chat escalation networks for 12 hours straight under maximum client panic. That means your cognitive circuits are already bulletproof! AI infrastructure isn't magic; it's just sorting metrics step-by-step. Let's step up to the crease and crush this innings. Maximum Effort!"</i></p>
        </div>
        """, unsafe_allow_html=True)
    with col_jv:
        st.markdown("""
        <div class='jarvis-card'>
            <h3 class='cobalt-txt'>🤖 JARVIS Diagnostic</h3>
            <p><i>"Systems are fully prepared, sir. Your background in electrical evaluation gives you a natural understanding of logical conditions and circuit states. We will isolate each algorithm incrementally. Do not permit minor compiler warnings to dilute your trajectory. Standing by to generate audio telemetry."</i></p>
        </div>
        """, unsafe_allow_html=True)

# --- 7. SECTOR: 7-MONTH CHAMPIONSHIP ROADMAP ---
elif nav_choice == "📅 Complete 7-Month Roadmap":
    st.title("📅 The 2026 Professional Career Transition Roadmap")
    st.write("Chronological engineering targets structured for enterprise transition deployment.")
    
    st.markdown("""
    <div class='deadpool-card'>
        <h3 class='crimson-txt'>🏏 PHASE 1: THE TRAINING NETS CLINIC (June — July)</h3>
        <p><b>Objective:</b> Master foundational algorithmic mechanics, systematic looping paths, and query optimization paradigms.</p>
        <ul>
            <li><b>June:</b> Variable mapping thresholds, conditional selection blocks, iterative tracking, sequences, and reusable modular frameworks.</li>
            <li><b>July:</b> Relational schema mechanics, cross-table matrix joining criteria, complex group aggregations, and Pandas dataframe analytics.</li>
        </ul>
    </div>
    
    <div class='jarvis-card'>
        <h3 class='cobalt-txt'>🎯 PHASE 2: ACCELERATED MODEL EXPLOSION (August — September)</h3>
        <p><b>Objective:</b> Build, scale, and validate end-to-end mathematical prediction models and transformer pipelines.</p>
        <ul>
            <li><b>August:</b> Linear continuous parameters, logistic classification boundaries, decision tree structures, and feature normalization metrics.</li>
            <li><b>September:</b> Neural deep networks, tokenization masks, attention layer tracking, and final staging of the Sentiment Product Recommendation System.</li>
        </ul>
    </div>
    
    <div class='deadpool-card'>
        <h3 class='crimson-txt'>🏆 PHASE 3: THE WORLD CUP PLACEMENT BLITZ (October — December)</h3>
        <p><b>Objective:</b> Production rollout of enterprise portfolios, resume optimization, and interview matching execution.</p>
        <ul>
            <li><b>October 1st:</b> Launch production pipelines. Algorithmic sorting optimization and advanced structural data layouts review.</li>
            <li><b>Nov - Dec:</b> Real-time technical board simulations, clearing target panels, and executing junior AI engineer contract signatures.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- 8. SECTOR: THE MASTER PROGRESS SCORECARD ---
elif nav_choice == "📊 Master Progress Scorecard":
    st.title("📊 Complete 37-Point Interactive Progress Scorecard")
    st.write("Verify every technical requirement across the 2026 development schedule.")

    st.markdown("<h3 class='crimson-txt'>📅 JUNE: Python Core Foundations & Logic Gates</h3>", unsafe_allow_html=True)
    st.session_state.chk_1 = st.checkbox("Checkpoint 01: Variable Naming Layouts & Memory Allocation Rules", value=st.session_state.chk_1)
    st.session_state.chk_2 = st.checkbox("Checkpoint 02: Core Data Classes (Integers, Floats, Strings, Booleans)", value=st.session_state.chk_2)
    st.session_state.chk_3 = st.checkbox("Checkpoint 03: Direct Comparison Mechanics (Evaluation of Truth Values)", value=st.session_state.chk_3)
    st.session_state.chk_4 = st.checkbox("Checkpoint 04: Chained Logical Operators (AND, OR, NOT Logic Verification)", value=st.session_state.chk_4)
    st.session_state.chk_5 = st.checkbox("Checkpoint 05: Conditional Branch Structures (Nested If, Elif, Else Pipelines)", value=st.session_state.chk_5)
    st.session_state.chk_6 = st.checkbox("Checkpoint 06: Definite Iteration Blocks (Processing Explicit For Sequences)", value=st.session_state.chk_6)
    st.session_state.chk_7 = st.checkbox("Checkpoint 07: Indefinite Iteration Blocks (Processing While Loop Constraints)", value=st.session_state.chk_7)
    st.session_state.chk_8 = st.checkbox("Checkpoint 08: Sequence Matrices (Python List Slicing, Appending, and Indexing)", value=st.session_state.chk_8)
    st.session_state.chk_9 = st.checkbox("Checkpoint 09: Mapping Arrays (Python Dictionary Structuring & Traversal)", value=st.session_state.chk_9)
    st.session_state.chk_10 = st.checkbox("Checkpoint 10: Functional Blueprints (Defining Parameters, Scopes, and Return Variables)", value=st.session_state.chk_10)
    st.markdown("<div class='video-box'>📺 <b>June Masterclass Blueprint Video Logs:</b><br>"
                "• <a href='https://www.youtube.com/results?search_query=freecodecamp+python+full+course' target='_blank'>FreeCodeCamp: Core Python Deep Dive Training</a></div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("<h3 class='cobalt-txt'>📅 JULY: Relational Infrastructure & SQL Engine Operations</h3>", unsafe_allow_html=True)
    st.session_state.chk_11 = st.checkbox("Checkpoint 11: Schema Design Principles (Primary/Foreign Constraint Architectures)", value=st.session_state.chk_11)
    st.session_state.chk_12 = st.checkbox("Checkpoint 12: Data Extraction Syntax (SELECT, WHERE, LIKE, IN Statements)", value=st.session_state.chk_12)
    st.session_state.chk_13 = st.checkbox("Checkpoint 13: Core Relational Joins (INNER JOIN and LEFT JOIN Implementations)", value=st.session_state.chk_13)
    st.session_state.chk_14 = st.checkbox("Checkpoint 14: Complex Relational Joins (RIGHT JOIN and FULL OUTER JOIN Matrices)", value=st.session_state.chk_14)
    st.session_state.chk_15 = st.checkbox("Checkpoint 15: Structural Groupings (GROUP BY, HAVING Constraints, and Sum/Count Aggregations)", value=st.session_state.chk_15)
    st.session_state.chk_16 = st.checkbox("Checkpoint 16: Pandas Matrix Processing (Converting Tables into High-Speed DataFrames)", value=st.session_state.chk_16)
    st.session_state.chk_17 = st.checkbox("Checkpoint 17: Quality Assurance Cleansing (Null Mapping, dropna, and fillna Routines)", value=st.session_state.chk_17)
    
    st.markdown("---")
    st.markdown("<h3 class='crimson-txt'>📅 AUGUST: Supervised Machine Learning Pipelines</h3>", unsafe_allow_html=True)
    st.session_state.chk_18 = st.checkbox("Checkpoint 18: Continuous Prediction Models (Linear Regression Weight Optimization)", value=st.session_state.chk_18)
    st.session_state.chk_19 = st.checkbox("Checkpoint 19: Classification Boundaries (Logistic Regression Log-Odds & Sigmoid Curves)", value=st.session_state.chk_19)
    st.session_state.chk_20 = st.checkbox("Checkpoint 20: Hierarchical Classifiers (Building and Pruning Decision Tree Nodes)", value=st.session_state.chk_20)
    st.session_state.chk_21 = st.checkbox("Checkpoint 21: Ensemble Architectures (Aggregating Output Paths via Random Forests)", value=st.session_state.chk_21)
    st.session_state.chk_22 = st.checkbox("Checkpoint 22: Feature Scaling Matrices (Mathematical Standardization & Normalization Tasks)", value=st.session_state.chk_22)
    st.session_state.chk_23 = st.checkbox("Checkpoint 23: Validation Set Separation (Implementing Stratified Train-Test Splitting)", value=st.session_state.chk_23)
    st.session_state.chk_24 = st.checkbox("Checkpoint 24: Model Score Calculations (Precision, Recall, and Unified F1 Mechanics)", value=st.session_state.chk_24)

    st.markdown("---")
    st.markdown("<h3 class='cobalt-txt'>📅 SEPTEMBER: Deep Learning & Generative AI Systems</h3>", unsafe_allow_html=True)
    st.session_state.chk_25 = st.checkbox("Checkpoint 25: Neural Network Mechanics (Backpropagation & Activation Functions)", value=st.session_state.chk_25)
    st.session_state.chk_26 = st.checkbox("Checkpoint 26: Transformer Systems (Text Tokenization Modeling & Scaled Attention)", value=st.session_state.chk_26)
    st.session_state.chk_27 = st.checkbox("Checkpoint 27: Endpoint Ingestion (Integrating Payloads into Google Gemini API)", value=st.session_state.chk_27)
    st.session_state.chk_28 = st.checkbox("Checkpoint 28: Context Prompt Engineering (Few-Shot Conditioning & Structure Labels)", value=st.session_state.chk_28)
    st.session_state.chk_29 = st.checkbox("Checkpoint 29: Capstone Design (Data Parsing Blueprint for Sentiment Recommender Foundations)", value=st.session_state.chk_29)
    st.session_state.chk_30 = st.checkbox("Checkpoint 30: Capstone Execution (Constructing Sentiment Vector Transformers to Parse Text)", value=st.session_state.chk_30)
    st.session_state.chk_31 = st.checkbox("Checkpoint 31: Capstone Hosting (Packing Project Infrastructure onto Streamlit Cloud Backend)", value=st.session_state.chk_31)

    st.markdown("---")
    st.markdown("<h3 class='crimson-txt'>📅 OCTOBER - DECEMBER: Whiteboard Algorithms & Placement Operations</h3>", unsafe_allow_html=True)
    st.session_state.chk_32 = st.checkbox("Checkpoint 32: Algorithmic Searching (Coding Iterative Linear & High-Speed Binary Search Loops)", value=st.session_state.chk_32)
    st.session_state.chk_33 = st.checkbox("Checkpoint 33: Sorting Routines (Implementing Custom Bubble Sort & Split Merge Sort Scripts)", value=st.session_state.chk_33)
    st.session_state.chk_34 = st.checkbox("Checkpoint 34: Data Structure Matrix Challenges (Array, String, and HashMap Optimization Paths)", value=st.session_state.chk_34)
    st.session_state.chk_35 = st.checkbox("Checkpoint 35: Resume Optimization (Reframing Support Ticket Metrics into Operations Data Engineering)", value=st.session_state.chk_35)
    st.session_state.chk_36 = st.checkbox("Checkpoint 36: GitHub Repository Presentation (Polishing Readme Blueprints & Structural Code Documentation)", value=st.session_state.chk_36)
    st.session_state.chk_37 = st.checkbox("Checkpoint 37: Interview Execution Strategy (Whiteboard Reasoning Drills & Architectural Explanations)", value=st.session_state.chk_37)

    # MASTER REAL-TIME METRIC CALCULATION
    st.markdown("---")
    st.subheader("📊 Tournament Achievement Completion Metrics")
    total_ticked = sum([st.session_state[f"chk_{i}"] for i in range(1, 38)])
    score_ratio = total_ticked / 37
    st.write(f"Championship Milestones Settled: **{total_ticked} / 37 Total Checkpoints** ({int(score_ratio * 100)}% Complete)")
    st.progress(score_ratio)

# --- 9. SECTOR: THE CODING NETS (LOGIC LAB) ---
elif nav_choice == "🧠 The Coding Nets (Logic Lab)":
    st.title("🧠 The Interactive Programmatic Logic Nets")
    st.write("Deconstruct computer science conditional parameters using explicit cricket match scenarios.")
    
    st.subheader("🏟️ Match Scenario: The Tactical Strike Rate Strategy Calculator")
    st.write("Scenario: A batsman reaches a milestone run metric. Calculate their performance rating using the equation:")
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
    
    st.subheader("🕹️ Live Execution Simulator Panel")
    sim_guess = st.text_input("Analyze the script module above. What exact string keyword will output on screen when Python executes the pipeline?")
    
    if st.button("Submit Decision Review (DRS)"):
        if sim_guess.strip() == "Explosive":
            st.balloons()
            st.success("🎯 BOUNDARY OVER THE FENCE! +10 Runs committed to your dashboard score!")
            st.session_state.runs += 10
        else:
            st.error("❌ CLEAN BOWLED STUMPS VIBRATING! Correct syntax spelling and submit again.")

# --- 10. SECTOR: DUAL-AGENT INTELLIGENCE CORE (PREMIUM NEURAL AUDIO ADDED) ---
elif nav_choice == "💬 Chat Engine (Dual Agent Voice Mode)":
    st.title("💬 Talk to Deadpool & JARVIS (Premium Voice Mode)")
    st.write("Toggle profiles to experience realistic, high-fidelity male voice simulation models.")
    st.markdown("---")
    
    agent_selector = st.radio("SELECT ACTIVE CORE INTELLIGENCE PROFILE:", ["🔴 Deadpool (Sarcastic Male AI Coach)", "🤖 JARVIS (Elite British Tech Instructor)"])
    
    user_prompt_entry = st.chat_input("Transmit transmission payload instructions to active agent...")
    
    if user_prompt_entry:
        st.session_state.chat_log.append(f"Vamshi: {user_prompt_entry}")
        
        if "GEMINI_API_KEY" not in st.secrets:
            system_voice_response = "System configuration fault: GEMINI_API_KEY identifier is missing from server deployment secrets."
            st.session_state.chat_log.append(f"System Matrix: {system_voice_response}")
        else:
            try:
                import google.generativeai as live_genai
                live_genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                
                if 'active_model_str' not in st.session_state:
                    try:
                        valid_models = [m.name for m in live_genai.list_models() if 'generateContent' in m.supported_generation_methods]
                        if 'models/gemini-1.5-flash' in valid_models: st.session_state.active_model_str = 'gemini-1.5-flash'
                        elif 'models/gemini-pro' in valid_models: st.session_state.active_model_str = 'gemini-pro'
                        else: st.session_state.active_model_str = valid_models[0]
                    except:
                        st.session_state.active_model_str = 'gemini-pro'
                
                llm_engine_instance = live_genai.GenerativeModel(st.session_state.active_model_str)
                
                # CHOOSE THE PRECISE NEURAL GENDER ID & DIALECTS
                if agent_selector == "🔴 Deadpool (Sarcastic Male AI Coach)":
                    system_conditioning_directives = (
                        "You are Deadpool, the hilarious, fast-talking, highly sarcastic mercenary who is also a deeply supportive, expert AI coding mentor. "
                        "You are coaching Vamshi, an absolute beginner from an EEE background who balances an intense 12-hour customer care shift "
                        "at Tech Mahindra. Always reply using Deadpool's signature comic book voice, address him as Vamshi, keep motivation at absolute max, and frame explanations using clever cricket analogies. "
                        f"User instruction payload: {user_prompt_entry}"
                    )
                    neural_voice_id = 'en-US-GuyNeural'  # Gritty, robust, expressive American male voice
                    speaker_identity_label = "Deadpool ⚔️"
                else:
                    system_conditioning_directives = (
                        "You are JARVIS, an elite, highly sophisticated, formal British AI technical instructor. "
                        "You are assisting Vamshi, a brilliant Master's student specializing in Data Science and Artificial Intelligence. "
                        "Provide responses with immaculate professional engineering grammar, structured data breakdowns, clean enterprise coding logic architectures, and absolute clarity. "
                        f"Technical query payload: {user_prompt_entry}"
                    )
                    neural_voice_id = 'en-GB-OliverNeural'  # Crisp, flawless, sophisticated British male butler voice
                    speaker_identity_label = "JARVIS 🤖"
                
                # Run AI Inference
                inferred_response_data = llm_engine_instance.generate_content(system_conditioning_directives)
                agent_text_reply = inferred_response_data.text
                
                # --- ASYNC NEURAL VOICE PIPELINE FOR EXPERT AUDIO ---
                with st.spinner("⚡ Tuning audio frequencies..."):
                    audio_stream = asyncio.run(generate_neural_audio(agent_text_reply, neural_voice_id))
                    st.audio(audio_stream, format='audio/mp3', autoplay=True)
                
                st.session_state.chat_log.append(f"{speaker_identity_label}: {agent_text_reply}")
                
            except Exception as execution_fault_anomaly:
                st.session_state.chat_log.append(f"Fault Diagnostic: Network interface exception -> {str(execution_fault_anomaly)}")

    # Display beautifully grouped messaging components
    for historical_msg in st.session_state.chat_log:
        if historical_msg.startswith("Vamshi:"):
            st.markdown(f"🧑 **{historical_msg}**")
        elif historical_msg.startswith("JARVIS"):
            st.markdown(f"<div class='jarvis-card'>🔵 <b>{historical_msg}</b></div>", unsafe_allow_html=True)
        elif historical_msg.startswith("Deadpool"):
            st.markdown(f"<div class='deadpool-card'>🔴 <b>{historical_msg}</b></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='video-box'>⚠️ <b>{historical_msg}</b></div>", unsafe_allow_html=True)

# --- 11. SECTOR: PROFESSIONAL ENGLISH TUNER ---
elif nav_choice == "🗣️ Professional English Tuner":
    st.title("🗣️ Technical Interview Communication Coach")
    st.write("Refine communication protocols from casual baseline states up to professional presentation frameworks.")
    
    st.markdown("""
    <div class='jarvis-card'>
        <h3 class='cobalt-txt'>🎤 The Daily 2-Minute Vocal Performance Tuning Routine</h3>
        <p>1. Launch the native system audio tracking application on your mobile device terminal.</p>
        <p>2. Engage record, and provide an unscripted explanation in English of <b>how variable lists or conditional branches operate</b> as if addressing an engineering director.</p>
        <p>3. Review the captured telemetry. Identify hesitation intervals, correct phrasing pathways, and re-execute.</p>
    </div>
    """, unsafe_allow_html=True)
    
    phrase_translation_dictionary = {
        "Casual Conversational Baseline Phrases (Avoid in Technical Mocks)": [
            "I want to write an app script code that calculates tournament runs and scores...",
            "I make lots of errors and my logical loop thinking is messed up right now...",
            "I work a regular support shift queue logging and closing water customer service tickets..."
        ],
        "Enterprise Engineering Target Phrases (Deploy to Whiteboard Board Panels)": [
            "My strategic objective is to implement a robust processing architecture to isolate data metrics...",
            "I am systematically optimizing my logic handling layouts and computational structural paradigms...",
            "I manage real-time structural queue databases, resolving critical client data escalations..."
        ]
    }
    st.table(pd.DataFrame(phrase_translation_dictionary))
