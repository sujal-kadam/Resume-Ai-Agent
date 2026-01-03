from planner_agent import analyze_job_description
from resume_analyzer_agent import analyze_resume
from evaluator_agent import evaluate_candidate


def run_ai_screening(job_description: str, resume_text: str):
    """
    Orchestrates all three agents:
    1. Planner Agent (JD analysis)
    2. Resume Analyzer Agent (candidate analysis)
    3. Evaluator Agent (final decision)

    Returns ONLY the final hiring evaluation (text).
    """

    # Step 1: Analyze Job Description
    job_analysis = analyze_job_description(job_description)

    # Step 2: Analyze Resume
    resume_analysis = analyze_resume(resume_text)

    # Step 3: Evaluate Candidate (FINAL DECISION)
    evaluation_result = evaluate_candidate(
        job_analysis=job_analysis,
        resume_analysis=resume_analysis
    )

    return evaluation_result


# ✅ Optional local test (won't run in Streamlit)
if __name__ == "__main__":
    sample_jd = """
    We are hiring a Junior Data Analyst.
    Requirements:
    - Strong knowledge of SQL and Excel
    - Basic Python for data analysis
    - 0–2 years of experience
    """

    sample_resume = """
    B.Sc IT graduate with Python, SQL, Excel skills.
    Internship as Data Analyst Intern.
    """

    output = run_ai_screening(sample_jd, sample_resume)
    print("\n🧠 FINAL HIRING DECISION\n")
    print(output)
