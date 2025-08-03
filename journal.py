import streamlit as st
from nlp_utils import score_reflection
from db import save_entry

def get_prompt(step):
    prompts = {
        1: "What's something that's been on your mind lately?",
        2: "That sounds difficult. Has anything helped, even a little?",
        3: "You're showing courage just by writing. What's something gentle you can do for yourself?",
        4: "What kind of support would feel good right now?"
    }
    return prompts.get(step, "Take your time. Write when you're ready.")

def journal_flow():
    st.title("📝 My Journal of Reflection")
    st.info("This journal is your private space. Be honest and kind to yourself.")

    topics = [
        "Feeling overwhelmed or stuck",
        "Losing someone I care about",
        "Worrying I'm not good enough",
        "Feeling lonely or distant",
        "Exam pressure or future stress"
    ]

    selected_topic = st.selectbox("Choose a topic:", topics)

    if "step" not in st.session_state:
        st.session_state.step = 1
        st.session_state.entries = []
        st.session_state.score = 0

    prompt = get_prompt(st.session_state.step)
    st.write(f"**Prompt:** {prompt}")

    reply = st.text_area("Write here:")

    if st.button("Next"):
        st.session_state.entries.append((prompt, reply))
        st.session_state.score += score_reflection(reply)

        if st.session_state.step < 4:
            st.session_state.step += 1
            st.rerun()
        else:
            save_entry(st.session_state.entries, st.session_state.score, selected_topic)
            st.success("You've completed your journal. Thank you.")
            st.metric("Reflection Score", st.session_state.score)
            st.balloons()
            for i, (q, a) in enumerate(st.session_state.entries):
                st.markdown(f"**Q{i+1}:** {q}")
                st.markdown(f"_A:_ {a}")
            st.session_state.step = 1
            st.session_state.entries = []
            st.session_state.score = 0