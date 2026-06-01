import streamlit as st
import datetime
import pandas as pd
import google.generativeai as genai

# --- 1. STADIUM & PERSONA CONFIG ---
st.set_page_config(page_title="DEADPOOL AI MENTOR", page_icon="⚔️", layout="wide")

# --- 2. THE "MERC WITH A MOUTH" THEME ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 100%);
        color: #ffffff;
    }
    section[data-testid="stSidebar"] {
        background-color: #2b0000 !important;
        border-right: 3px solid #e23636;
    }
    .stadium-card {
        background: rgba(43, 0, 0, 0.6);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #e23636;
        box-shadow: 0 0 20px rgba(226, 54, 54, 0.4);
        margin-bottom: 25px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #e23636 0%, #000000 100%);
        color: white;
        border: 1px solid #ffffff;
        border-radius: 10px;
        font-weight: 800;
        text-transform: uppercase;
    }
    h1, h2, h3 { color: #e23636; text-transform: uppercase; letter-spacing: 2px; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: white; border: 1px solid #e23636; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PERSISTENT STATE ---
if 'chat_history' not in st.session_state: st.session_state.chat_history = []
if 'streak' not in st.session_state: st.session_state.streak = 1

# --- 4. DATES ---
today = datetime.date(2026, 6, 1)
interview_day = datetime.date(2026, 10, 1)

# --- 5. SIDEBAR: THE DUGOUT ---
st.sidebar.markdown("<h1 style='text-align: center; color: #e23636;'>⚔️ DEADPOOL</h1>", unsafe_allow_html=True)
st.sidebar.write(f"🔥 **Win Streak:** {st.session_state.streak} Matches")
if st.sidebar.button("LOG MATCH DAY"):
    st.session_state.streak += 1
    st.sidebar.success("Match logged. Maximum Effort!")

nav = st.sidebar.radio("CHOOSE SECTOR:", [
    "🏟️ THE ARENA (Dashboard)",
    "📊 MASTER SCORECARD (Checkboxes)",
    "🧠 LOGIC NETS (Simulator)",
    "💬 CHAT WITH DEADPOOL (AI)",
    "🗣️ ENGLISH TUNER"
])

# --- 6. ARENA DASHBOARD ---
if nav == "🏟️ THE ARENA (Dashboard)":
    st.title("🏟️ Welcome to the Merc's Arena")
    col1, col2 = st.columns(2)
    col1.metric("Days to Oct 1st Finals", (interview_day - today).days)
    col2.metric("Target Level", "AI Overlord")

    st.markdown("""
    <div class='stadium-card'>
        <h3>🔥 Deadpool's Message</h3>
        <p>"Listen up, Vamshi. You worked 12 hours? Cute. I once regrew my whole body from a thumb. 
        Starting from zero coding knowledge is just like being at 0/9 in a T20—you have nowhere to go but <b>Up</b>. 
        Focus for 20 minutes tonight. No excuses. I'm watching."</p>
    </div>
    """, unsafe_allow_html=True)
    
    energy = st.select_slider("Energy Level:", options=["Broken", "Tired", "Steady", "Superhuman"])
    if energy == "Broken":
        st.error("Go to sleep, ya dummy. Read one flashcard and hit the sack.")
    elif energy == "Superhuman":
        st.success("MAXIMUM EFFORT! Go to the Logic Nets and crush some code.")

# --- 7. MASTER SCORECARD (ALL MONTHS) ---
elif nav == "📊 MASTER SCORECARD (Checkboxes)":
    st.title("📊 The Complete 7-Month Scorecard")
    st.write("Track every single milestone. No skipping.")

    with st.expander("✅ JUNE: Python Core (Nets Practice)"):
        st.checkbox("Variables & Memory Buckets")
        st.checkbox("If/Else Logic (Umpire Decisions)")
        st.checkbox("For/While Loops (The Over Counter)")
        st.checkbox("Lists & Dictionaries (Team Roster)")
        st.markdown("[Watch: Python Masterclass](https://www.youtube.com/results?search_query=python+tutorial+for+beginners)")

    with st.expander("✅ JULY: SQL & Data (Fielding)"):
        st.checkbox("SQL Joins & Filters")
        st.checkbox("Pandas Analytics")

    with st.expander("✅ AUGUST: Machine Learning (Bowling)"):
        st.checkbox("Linear/Logistic Regression")
        st.checkbox("Model Accuracy & Metrics")

    with st.expander("✅ SEPTEMBER: GenAI (The Magic)"):
        st.checkbox("LLM APIs & Prompt Engineering")
        st.checkbox("Sentiment Capstone Finalization")

    with st.expander("✅ OCTOBER-DECEMBER: The Finals"):
        st.checkbox("Resume: Deadpool Style")
        st.checkbox("Interview Smasher")

# --- 8. LOGIC NETS (SIMULATOR) ---
elif nav == "🧠 LOGIC NETS (Simulator)":
    st.title("🧠 The Logic Simulator")
    st.subheader("Scenario: The DRS Review")
    st.code("""
# Logic: If ball hits stumps and no bat involved, it is OUT.
ball_hits_stumps = True
bat_involved = False

if ball_hits_stumps == True and bat_involved == False:
    print("☝️ OUT! BACK TO THE PAVILION!")
else:
    print("🏏 NOT OUT! KEEP BATTING!")
    """, language="python")
    
    ans = st.text_input("What is the result of this code?")
    if st.button("Submit Decision"):
        if "OUT" in ans.upper():
            st.success("Correct! You have the eye of an Umpire!")
        else:
            st.error("Wrong! Re-read the logic. Maximum Effort!")

# --- 9. CHAT WITH DEADPOOL (REAL AI INTERFACE) ---
elif nav == "💬 CHAT WITH DEADPOOL (AI)":
    st.title("💬 Talk to Deadpool")
    st.write("Ask me anything—Coding, Cricket, Life, or how to regrow a limb.")
    
    # User can input their own API Key in the sidebar or use a placeholder
    user_key = st.text_input("Enter your Google API Key (optional to save your own quota):", type="password")
    
    user_query = st.chat_input("Ask Deadpool anything...")
    
    if user_query:
        st.session_state.chat_history.append(f"Vamshi: {user_query}")
        
        # Persona Logic
        if user_key:
            try:
                genai.configure(api_key=user_key)
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(f"Answer this as Deadpool, the sarcastic but helpful AI mentor. Be funny and use cricket analogies. User question: {user_query}")
                reply = response.text
            except:
                reply = "Chimichangas! Your API key is acting up. Let's just say I agree with you."
        else:
            reply = "I'm in Offline Mode (Enter API Key for full brain power). But basically: Focus on your code, don't be a hero, and keep your head in the game!"

        st.session_state.chat_history.append(f"Deadpool: {reply}")

    for msg in st.session_state.chat_history:
        st.write(msg)

# --- 10. ENGLISH TUNER ---
elif nav == "🗣️ ENGLISH TUNER":
    st.title("🗣️ The Communication Tuner")
    st.markdown("""
    <div class='stadium-card'>
        <h3>🎤 2-Minute Voice Drill</h3>
        <p>1. Open your phone recorder.<br>2. Explain 'What is a Variable' like you're talking to a cricket fan.<br>3. Check for confidence. 8/10 or nothing!</p>
    </div>
    """, unsafe_allow_html=True)
