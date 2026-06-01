import streamlit as st
import datetime
import pandas as pd

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Vamshi's AI Transition 2026", page_icon="🏏", layout="wide")

# --- CUSTOM INTERFACE THEME ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { background-color: #238636; color: white; border-radius: 10px; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #f59e0b; }
    h1, h2, h3 { color: #58a6ff; font-family: 'Helvetica'; }
    </style>
    """, unsafe_allow_html=True)

# --- SYSTEM DATES ---
today = datetime.date(2026, 6, 1)
interview_start = datetime.date(2026, 10, 1)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🏆 Match Center")
nav = st.sidebar.radio("Sectors:", [
    "🏠 Dashboard", 
    "📅 7-Month Roadmap", 
    "🏆 My Scorecard (Progress)",
    "🧠 Logic Lab (Cricket Ed.)",
    "💻 Coddy Interactive Hub",
    "🗣️ English Fluency Pro"
])

# --- 1. DASHBOARD ---
if nav == "🏠 Dashboard":
    st.title("🚀 Day 1: The First Ball")
    st.metric("Days to Interview Phase", (interview_start - today).days)
    st.info("🔥 **Tonight's Goal (19:00 Start):** Master Variables & If/Else logic.")

# --- 2. 7-MONTH ROADMAP ---
elif nav == "📅 7-Month Roadmap":
    st.title("📅 The Championship Roadmap")
    data = {
        "Month": ["June", "July", "August", "September", "October", "November", "December"],
        "Focus": ["Python Logic & English", "SQL & Stats", "Machine Learning", "GenAI & Projects", "Applications", "Mocks", "Offer"],
    }
    st.table(pd.DataFrame(data))

# --- 3. PROGRESS TRACKER (NEW) ---
elif nav == "🏆 My Scorecard (Progress)":
    st.title("🏆 My Progress Scorecard")
    st.write("Check off the 'overs' as you complete them. Don't move to the next month until June is green!")
    
    st.subheader("🏏 JUNE: The Opening Stand")
    c1 = st.checkbox("Day 1: Variables & Data Types")
    c2 = st.checkbox("Day 2-3: If/Else & Comparison Operators")
    c3 = st.checkbox("Week 2: For Loops & While Loops")
    c4 = st.checkbox("Week 3: Lists & Dictionaries")
    c5 = st.checkbox("Week 4: Functions & Modules")
    
    progress = (c1+c2+c3+c4+c5) / 5
    st.write(f"June Progress: {int(progress*100)}%")
    st.progress(progress)

# --- 4. LOGIC LAB ---
elif nav == "🧠 Logic Lab (Cricket Ed.)":
    st.title("🧠 Logic Lab")
    st.subheader("Day 1 Challenge: The Milestone Checker")
    st.code("""
runs = 72 # Change this number to test

if runs >= 100:
    print("Century!")
elif runs >= 50:
    print("Half-Century!")
else:
    print("Keep playing!")
    """)

# --- 5. CODDY HUB ---
elif nav == "💻 Coddy Interactive Hub":
    st.title("💻 Coddy Learning Links")
    st.markdown("- [June: Python Fundamentals](https://coddy.tech/landing/python)")

# --- 6. ENGLISH PRO ---
elif nav == "🗣️ English Fluency Pro":
    st.title("🗣️ Communication")
    st.write("Explain Day 1's 'If/Else' logic out loud for 2 minutes tonight.")
