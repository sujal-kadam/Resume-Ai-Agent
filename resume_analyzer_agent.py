from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)

def analyze_resume(resume_text: str):
    """
    Takes resume text from Streamlit (PDF → text)
    and returns a human-readable candidate summary (NOT JSON).
    """

    prompt = f"""
You are a Resume Analyzer Agent assisting HR and recruiters.

Analyze the resume below and summarize the candidate profile
in clear, professional, human-readable language.

Instructions:
- Do NOT return JSON
- Do NOT use code blocks
- Use bullet points and short headings
- Write as if explaining the candidate to an HR manager

Cover:
1. Candidate background summary
2. Key skills and tools
3. Education details
4. Experience / internships
5. Projects or practical exposure
6. Any risks, gaps, or caution areas (if applicable)

Resume:
{resume_text}
"""

    response = llm.invoke(prompt)
    return response.content.strip()


# ✅ Optional local test (won't run in Streamlit)
if __name__ == "__main__":
    sample_resume = """
    Name: Rahul Sharma
    Education: B.Sc IT, Mumbai University (2024)

    Skills:
    Python, SQL, Excel, Power BI

    Experience:
    6-month internship as Data Analyst Intern

    Projects:
    Sales dashboard using Power BI
    Customer churn analysis using Python
    """

    output = analyze_resume(sample_resume)

    print("\n📄 Resume Analyzer Output:\n")
    print(output)
