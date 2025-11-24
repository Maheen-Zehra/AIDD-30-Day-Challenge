import streamlit as st # pyright: ignore[reportMissingImports]
import json
from utils import extract_text_from_pdf
from agent import StudyBuddyAgent

# --- Page Configuration ---
st.set_page_config(
    page_title="Study Buddy",
    page_icon="📚",
    layout="centered"
)

# --- Agent Initialization ---
# Initialize the agent. In a real scenario, this might involve connecting to services.
agent = StudyBuddyAgent()

# --- Session State Management ---
# Initialize session state variables to None if they don't exist.
if 'pdf_text' not in st.session_state:
    st.session_state.pdf_text = None
if 'summary' not in st.session_state:
    st.session_state.summary = None
if 'quiz' not in st.session_state:
    st.session_state.quiz = None
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# --- UI Components ---
st.title("📚 Study Buddy Agent")
st.markdown("Upload a PDF document, and I'll help you summarize it and create a quiz to test your knowledge!")

# --- PDF Upload and Processing ---
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Use a button to trigger processing
    if st.button("Process PDF"):
        # Reset state if a new file is uploaded
        st.session_state.pdf_text = None
        st.session_state.summary = None
        st.session_state.quiz = None
        st.session_state.user_answers = {}

        with st.spinner("Reading your document..."):
            extracted_text = extract_text_from_pdf(uploaded_file)
            if "Error" in extracted_text:
                st.error(extracted_text)
            else:
                st.session_state.pdf_text = extracted_text
                st.success("PDF processed successfully! You can now generate a summary or a quiz.")

# --- Summarization Section ---
if st.session_state.pdf_text is not None:
    st.markdown("---")
    if st.button("✨ Generate Summary"):
        with st.spinner("Creating your summary... this may take a moment."):
            summary = agent.summarize(st.session_state.pdf_text)
            st.session_state.summary = summary

if st.session_state.summary is not None:
    st.subheader("Summary")
    st.info(st.session_state.summary)

# --- Quiz Generation Section ---
if st.session_state.pdf_text is not None:
    if st.button("📝 Create Quiz"):
        st.session_state.quiz = None # Reset previous quiz
        st.session_state.user_answers = {}
        with st.spinner("Crafting your quiz... this may take a moment."):
            quiz_data = agent.generate_quiz(st.session_state.pdf_text)
            st.session_state.quiz = quiz_data

if st.session_state.quiz is not None:
    st.markdown("---")
    st.subheader("Quiz Time!")
    
    show_results = st.button("Submit & See Results")
    
    for i, q in enumerate(st.session_state.quiz):
        st.markdown(f"**Question {i+1}:** {q['question']}")
        options = list(q['options'].values())
        user_choice = st.radio(
            label="Choose your answer:",
            options=options,
            key=f"q_{i}"
        )
        # Store the key of the chosen option
        for key, value in q['options'].items():
            if value == user_choice:
                st.session_state.user_answers[i] = key
                break

    if show_results:
        st.markdown("---")
        st.subheader("Quiz Results")
        score = 0
        for i, q in enumerate(st.session_state.quiz):
            correct_answer_key = q['answer']
            correct_answer_value = q['options'][correct_answer_key]
            user_answer_key = st.session_state.user_answers.get(i)

            if user_answer_key == correct_answer_key:
                score += 1
                st.success(f"**Question {i+1}: Correct!**")
            else:
                st.error(f"**Question {i+1}: Incorrect.**")
                st.info(f"The correct answer was: **{correct_answer_value}**")
        
        st.markdown(f"### Your final score: {score}/{len(st.session_state.quiz)}")

st.markdown("---")
st.markdown("_Powered by Gemini, Streamlit, and OpenAgents._")
