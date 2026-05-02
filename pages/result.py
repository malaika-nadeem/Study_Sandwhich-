import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
import json


st.set_page_config(page_title="studysandwhich", page_icon="🥪")

st.markdown("""<style>
.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background-color: #FDF6EC !important;
}
</style>""", unsafe_allow_html=True)

# unpack from session state
text = st.session_state["text"]
num_mcq = st.session_state["num_mcq"]
num_short = st.session_state["num_short"]

st.subheader("*Your StudySandwich is ready!* 🥪")

with st.spinner("Generating your quiz..."):
    prompt = f"""
    You are a quiz generator. Based on the text below, generate:
    - {num_mcq} MCQs with 4 options each and the correct answer
    - {num_short} short questions with answers
    
    Return in JSON format only. No extra text. Use this structure:
    {{
      "mcqs": [
        {{"question": "...", "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}}, "correct": "A"}}
      ],
      "short_questions": [
        {{"question": "...", "answer": "..."}}
      ]
    }}
    
    Text: {text}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )                                              
    result = response.choices[0].message.content
    
   # clean backticks if present
    result = result.strip().replace("```json", "").replace("```", "").strip()
   # parse JSON
    quiz_data = json.loads(result)

for i, mcq in enumerate(quiz_data["mcqs"]):
    st.write(f"**Q{i+1}: {mcq['question']}**")
    answer = st.radio("Choose:", list(mcq["options"].values()), key=f"mcq_{i}")
for i, sq in enumerate(quiz_data["short_questions"]):
    st.write(f"**Q{i+1}: {sq['question']}**")  # display the question
    user_answer = st.text_input("Your answer:", key=f"short_{i}")  # text box for user
st.markdown("---")
if st.button("Submit Quiz 🥪"):
    score = 0
    total = len(quiz_data["mcqs"]) + len(quiz_data["short_questions"])
    
    # check MCQs
    st.subheader("MCQ Results:")
    for i, mcq in enumerate(quiz_data["mcqs"]):
        user_ans = st.session_state.get(f"mcq_{i}")
        correct_ans = mcq["options"][mcq["correct"]]
        if user_ans == correct_ans:
            st.success(f"Q{i+1}: ✅ Correct!")
            score += 1
        else:
            st.error(f"Q{i+1}: ❌ Wrong! Correct answer: {correct_ans}")
    
    # check short questions using AI
    st.subheader("Short Question Results:")
    for i, sq in enumerate(quiz_data["short_questions"]):
        user_ans = st.session_state.get(f"short_{i}", "")
        check_prompt = f"""
        Question: {sq['question']}
        Expected answer: {sq['answer']}
        User's answer: {user_ans}
        Reply only: CORRECT or INCORRECT and one sentence why.
        """
        check_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": check_prompt}]
        )
        feedback = check_response.choices[0].message.content
        if "CORRECT" in feedback.upper():
            st.success(f"Q{i+1}: ✅ {feedback}")
            score += 1
        else:
            st.error(f"Q{i+1}: ❌ {feedback}")
    
    # final score
    st.markdown("---")
    st.subheader(f"🥪 Your Score: {score}/{total}")
            
