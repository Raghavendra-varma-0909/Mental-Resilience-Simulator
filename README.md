Mental Resilience Simulator
===========================

🌱 What’s This All About?
--------------------------
Mental Resilience Simulator is a simple, interactive journaling app designed to help people track their thoughts and emotions.
By combining the power of journaling with sentiment analysis and visual feedback, it encourages self-reflection and supports mental well-being in a private and tech-friendly way.

🚀 What You Can Do with It
---------------------------
- 🧠 Understand Your Mood – Each journal entry is analyzed using NLP to detect emotional tone.
- 📝 Keep a Daily Journal – Write, save, and revisit your thoughts anytime.
- 📊 See Your Progress – Get visual insights into how your emotional state changes over time.
- 🔐 Keep It Private – Includes simple user authentication so your data stays yours.
- 💬 Get Subtle Insights – Helps you spot patterns and emotional triggers over time.

🌍 Why It Matters
------------------
Mental health is just as important as physical health—but it's often overlooked.
This project gives people a private space to:
- Reflect regularly
- Recognize emotional ups and downs
- Track their resilience journey
- Understand their thoughts—without needing a therapist or app subscription

It’s a small step that can lead to better self-awareness and emotional strength.

🛠️ Built With
--------------
- streamlit – To build the interactive web app
- textblob – For analyzing sentiment in journal entries
- datetime – To timestamp each entry
- json – To manage and store data
- auth.py, db.py, dashboard.py, nlp_utils.py – Custom modules to handle login, data, visuals, and NLP

📁 How It’s Organized
----------------------
resilience_journal/
├── main.py           # Runs the app
├── auth.py           # Manages login
├── journal.py        # Handles writing and saving entries
├── nlp_utils.py      # Analyzes the text with NLP
├── db.py             # Deals with data storage
├── dashboard.py      # Builds charts and graphs

💡 Getting Started
-------------------
1. Clone the project:
   git clone https://github.com/Raghavendra-varma-0909/Mental-Resilience-Simulator.git
   cd Mental-Resilience-Simulator

2. Install the required libraries:
   pip install streamlit textblob

3. Launch the app:
   streamlit run main.py

👨‍💻 Made by
-------------
Raghavendra Varma  
GitHub: https://github.com/Raghavendra-varma-0909
