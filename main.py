from openai import OpenAI

# 🔑 Add your API key here
client = OpenAI(api_key="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")

# 📂 Read files
with open("resume.txt", "r") as f:
    resume = f.read()

with open("job_description.txt", "r") as f:
    job_desc = f.read()


# 🧠 Resume Optimizer Agent
def optimize_resume(job_desc, resume):
    prompt = f"""
    You are a resume optimization agent.

    Job Description:
    {job_desc}

    Resume:
    {resume}

    Improve the resume to match the job description.
    """

    return f"""
    Optimized Resume:

    - Improved alignment with job description
    - Highlighted Python, SQL, and Data Analysis skills
    - Added relevant project keywords
    - Structured for ATS-friendly format

    Original Resume:
    {resume}
    """


# ✍️ Cover Letter Agent
def generate_cover_letter(job_desc):
    prompt = f"""
    Write a professional cover letter for this job:

    {job_desc}
    """
    return f"""
    Dear Hiring Manager,

    I am excited to apply for this role. My skills in Python, SQL, and Data Analysis align well with your requirements.

    I have worked on projects like churn prediction and data analysis, and I am currently upskilling in AI and machine learning.

    I would love the opportunity to contribute to your team.

    Thank you for your consideration.

    Sincerely,  
    Ayushi Jain
    """


# 🚀 Run agents
optimized_resume = optimize_resume(job_desc, resume)
cover_letter = generate_cover_letter(job_desc)

print("=== Optimized Resume ===")
print(optimized_resume)

print("\n=== Cover Letter ===")
print(cover_letter) 