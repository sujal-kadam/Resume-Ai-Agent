from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)

def evaluate_candidate(job_analysis: str, resume_analysis: str):
    """
    Compares job requirements with candidate profile
    and returns a hiring decision in human-readable text.
    """

    prompt = f"""
You are an AI Hiring Evaluation Agent assisting HR managers.

Your task is to compare:
1. The job requirements
2. The candidate's resume analysis

Then provide a clear hiring evaluation.

IMPORTANT INSTRUCTIONS:
- Do NOT return JSON
- Do NOT use code blocks
- Use bullet points and short sections
- Be concise, professional, and business-focused

Your output MUST include:
1. Overall Match Percentage (0–100%)
2. Fit Category (Poor / Average / Good / Strong / Excellent)
3. Key Strengths (bullet points)
4. Gaps or Concerns (bullet points)
5. Final Hiring Recommendation (short paragraph)
6. Interview Focus Areas (if shortlisted)

Job Requirements Summary:
{job_analysis}

Candidate Resume Summary:
{resume_analysis}
"""

    response = llm.invoke(prompt)
    return response.content.strip()


# ✅ Optional local test (won't run in Streamlit)
if __name__ == "__main__":
    sample_job = """
    Junior Data Analyst role requiring SQL, Excel, Python basics,
    and dashboard creation skills.
    """

    sample_resume = """
    B.Sc IT graduate with Python, SQL, Excel skills,
    internship experience, and Power BI projects.
    """

    output = evaluate_candidate(sample_job, sample_resume)
    print("\n🧠 Hiring Evaluation Output:\n")
    print(output)
