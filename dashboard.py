import streamlit as st
import json

DB_FILE = "journal_entries.json"

def show_dashboard():
    st.title("📊 Journal Dashboard")

    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
    except:
        st.warning("No journal entries found.")
        return

    st.metric("Total Entries", len(data))
    scores = [d['score'] for d in data]
    if scores:
        st.metric("Average Score", sum(scores) / len(scores))

    for entry in data:
        st.markdown("---")
        st.write(f"**Date:** {entry['timestamp']}")
        st.write(f"**Topic:** {entry['topic']}")
        for i, (q, a) in enumerate(entry['entries']):
            st.markdown(f"**Q{i+1}:** {q}")
            st.markdown(f"_A:_ {a}")