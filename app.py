import streamlit as st

st.title("🤖 AI Job Application Assistant")

st.write("Upload your resume and job description to generate optimized resume and cover letter.")

# Input fields
resume = st.text_area("Paste your Resume here")
job_desc = st.text_area("Paste Job Description here")

# Button
if st.button("Generate"):

    # Fake Resume Output
    optimized_resume = f"""
    Ayushi Jain

    Skills:
    - Python
    - SQL
    - Data Analysis
    - Machine Learning
    - Excel

    Projects:
    - Customer Churn Prediction using Machine Learning
    - TED Talk Data Analysis

    Experience:
    - 3 years experience
    - Currently upskilling in AI, LLMs, and RAG

    Enhancements:
    ✔ Added job-relevant keywords  
    ✔ Improved project descriptions  
    ✔ Structured for ATS optimization  
    """

    # Fake Cover Letter
    cover_letter = f"""
    Dear Hiring Manager,

    I am writing to express my interest in this role. With strong skills in Python, SQL, and Data Analysis, I am confident in my ability to contribute effectively to your team.

    I have worked on projects such as Customer Churn Prediction and TED Talk Analysis, which have strengthened my analytical and problem-solving abilities. I am also currently expanding my knowledge in AI, LLMs, and modern data technologies.

    I am highly motivated, quick to learn, and eager to apply my skills in a real-world environment.

    Thank you for your time and consideration.

    Sincerely,  
    Ayushi Jain
    """

    st.subheader("📄 Optimized Resume")
    st.write(optimized_resume)

    st.subheader("✉️ Cover Letter")
    st.write(cover_letter)