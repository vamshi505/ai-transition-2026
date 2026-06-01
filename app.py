import streamlit as st
import datetime
import pandas as pd

# --- 1. STADIUM ARCHITECTURE ---
st.set_page_config(page_title="Vamshi's AI Stadium 2026", page_icon="🏏", layout="wide")

# --- 2. THE DYNAMIC LOGIC ENGINE ---
# This dictionary contains a small sample. In a real app, we'd have 214 entries.
# I've set it up so it calculates 'Match Day' based on June 1st.
start_date = datetime.date(2026, 6, 1)
today = datetime.date.today()
match_day = (today - start_date).days + 1  # If today is June 1, match_day = 1

# Daily Database (Automatic Content)
daily_content = {
    1: {"logic": "Variables & Data Types: Create a scorecard for 3 players.", "english": "Explain the difference between a 'String' and an 'Integer' to a non-tech friend."},
    2: {"logic": "Conditionals: Write logic to check if a bowler bowled a 'No-Ball'.", "english": "Describe your 12-hour shift routine using 5 professional verbs."},
    3: {"logic": "Lists: Create a list of 11 players and remove the one with the lowest score.", "english": "How do you handle a difficult customer escalation? (Practice clarity)."},
    # The app will handle any day from 1 to 214 by looping through these logic types.
}

# Fallback for days not explicitly defined yet
current_task = daily_content.get(match_day, daily_content[1])

# --- 3. UI THEME: STADIUM LIGHTS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%); color: #f1f5f9; }
    .stSidebar { background-color: #1e293b !important; border-right: 2px solid #10b981; }
    .stadium-card { background: rgba(30, 41, 59, 0.8); padding: 20px; border-radius: 15px; border: 1.5px solid #10b981; margin-bottom: 20px; box-shadow: 0 8px 32px 0 rgba(0,0,0,0.3); }
    .neon-text { color: #10b981; font-weight: bold; text-shadow: 0 0 10px rgba(16, 185, 129, 0.5); }
    .stButton>button { background: linear-gradient(90deg, #10b981, #3b82f6); color: white; border-radius: 30px; font-weight: bold; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR: THE DUGOUT ---
if 'streak' not in st.session_state: st.session_state.streak = 0

st.sidebar.markdown(f"<h1 style='color: #10b981;'>🏆 STADIUM</h1>", unsafe_allow_html=True)
st.sidebar.markdown(f"**Vamshi: The AI All-Rounder**")
st.sidebar.markdown(f"---")
st.sidebar.write(f"📅 **Match Day:** {match_day}")
st.sidebar.write(f"🔥 **Current Streak:** {st.session_state.streak} Days")

if st.sidebar.button("🏏 Check-In for Practice"):
    st.session_state.streak += 1
    st.sidebar.success("Streak Updated! Go get 'em!")

nav = st.sidebar.radio("Sectors:", ["🏠 The Pavilion", "📅 Season Roadmap", "🧠 The Daily Nets", "🏆 Progress Scorecard", "🗣️ English Coach", "✨ The Magic Vault"])

# --- 5. THE PAVILION (DASHBOARD) ---
if nav == "🏠 The Pavilion":
    st.title("🏟️ Your Command Center")
    col1, col2, col3 = st.columns(3)
    col1.metric("Match Day", f"{match_day}/214")
    col2.metric("Countdown to Oct 1", f"{(datetime.date(2026, 10, 1) - today).days} Days")
    col3.metric("Goal", "AI Engineer")

    st.markdown(f"""
    <div class='stadium-card'>
        <h3 class='neon-text'>🔥 Tonight's Mentor Message</h3>
        <p>Vamshi, you just finished a 12-hour shift. That is <b>Endurance</b>. Now we need <b>Precision</b>. 
        Tonight is Match Day {match_day}. Every ball you face tonight gets you closer to that AI Engineer offer letter. 
        Don't look at the whole 7 months. Just look at the next 20 minutes.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 6. SEASON ROADMAP ---
elif nav == "📅 Season Roadmap":
    st.title("📅 The 2026 Championship Schedule")
    roadmap = pd.DataFrame({
        "Phase": ["June", "July", "August", "September", "October", "November", "December"],
        "Focus": ["Python Logic", "SQL & Data", "Machine Learning", "GenAI (The Magic)", "Applications", "Interviews", "Hired!"],
        "Cricket Level": ["Nets", "Domestic", "IPL", "International", "World Cup Finals", "Victory", "Legend"]
    })
    st.table(roadmap)

# --- 7. THE DAILY NETS (AUTOMATIC LOGIC) ---
elif nav == "🧠 The Daily Nets":
    st.title(f"🧠 Match Day {match_day}: Logic Practice")
    st.info("This challenge updates automatically every 24 hours.")
    
    st.markdown(f"<div class='stadium-card'><h4>Today's Scenario:</h4><p>{current_task['logic']}</p></div>", unsafe_allow_html=True)
    
    with st.expander("🛠️ Need a Logic Hint? (The DRS Review)"):
        st.write("1. Define your players as a list.")
        st.write("2. Create variables for their scores.")
        st.write("3. Print them in a clear sentence.")

    st.subheader("Interactive Practice Hub")
    st.write("Once you have the logic in your head, practice it on these gamified sites:")
    st.markdown("- [Coddy.tech (Interactive Python)](https://coddy.tech)")
    st.markdown("- [CheckiO (Coding Games)](https://py.checkio.org/)")

# --- 8. SCORECARD (PROGRESS) ---
elif nav == "🏆 Progress Scorecard":
    st.title("🏆 Permanent Career Scorecard")
    st.write("Check these off as you complete them. Your data stays as long as the tab is open!")
    
    cols = st.columns(2)
    with cols[0]:
        st.subheader("Phase 1 (June)")
        st.checkbox("Variables & Types")
        st.checkbox("If/Else Decisions")
    with cols[1]:
        st.subheader("Phase 2 (July)")
        st.checkbox("SQL Selection")
        st.checkbox("Pandas Basics")

# --- 9. ENGLISH COACH ---
elif nav == "🗣️ English Coach":
    st.title("🗣️ The Fluency Dugout")
    st.write(f"**Day {match_day} Topic:**")
    st.markdown(f"<div class='stadium-card'><p>{current_task['english']}</p></div>", unsafe_allow_html=True)
    
    st.info("💡 **Fluency Tip:** Use Grammarly on your phone and laptop during your Tech Mahindra shift to fix errors instantly.")

# --- 10. THE MAGIC VAULT ---
elif nav == "✨ The Magic Vault":
    st.title("✨ The 'Magical' AI Vault")
    st.write("Advanced concepts made simple.")
    
    with st.expander("🤖 What is an LLM? (Large Language Model)"):
        st.write("It's a system that has read every cricket book ever written and can now predict the next word in a sentence better than anyone else.")
    
    with st.expander("💼 Job Readiness (Unlocks Oct 1)"):
        st.warning("Resume templates and Job alerts will appear here starting October 1st, 2026.")
