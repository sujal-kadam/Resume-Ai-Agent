from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables (.env file)
load_dotenv()

# Initialize the LLM (Planner Agent brain)
llm = ChatOpenAI(
    model="gpt-4o-mini",   # cost-effective & strong
    temperature=0.3
)

def analyze_job_description(job_description: str):
    """
    Takes Job Description text from Streamlit
    and returns a human-readable hiring plan (NOT JSON).
    """

    planner_prompt = f"""
You are a Senior HR Planning Agent.

Analyze the following Job Description and explain the hiring requirements
in clear, professional, human-readable language.

Instructions:
- Do NOT return JSON
- Do NOT use code blocks
- Use bullet points and short headings
- Write as if explaining to an HR manager

Cover:
1. Job role summary
2. Required skills
3. Experience expectations
4. Nice-to-have skills
5. What the recruiter should focus on while screening

Job Description:
{job_description}
"""

    response = llm.invoke(planner_prompt)
    return response.content.strip()


# ✅ Optional local test (won't run in Streamlit)
if __name__ == "__main__":
    sample_jd = """
    We are hiring a Junior Data Analyst.
    Requirements:
    - Strong knowledge of SQL and Excel
    - Basic Python for data analysis
    - 0–2 years of experience
    - Ability to create dashboards and reports
    Good to have:
    - Tableau or Power BI
    - Internship or project experience
    """

    output = analyze_job_description(sample_jd)
    print("\n📌 Planner Agent Output:\n")
    print(output)
