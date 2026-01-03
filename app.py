import streamlit as st
from pypdf import PdfReader
from main import run_ai_screening

# ----------------------------------
# Page Config
# ----------------------------------
st.set_page_config(
    page_title="AI Resume Screening Agent",
    layout="wide"
)

st.title("🤖 AI Resume Screening Agent")
st.caption("AI-powered candidate screening & hiring recommendation")

# ----------------------------------
# Job Description Input
# ----------------------------------
jd_text = st.text_area(
    "📄 Paste Job Description",
    height=220,
    placeholder="Paste the job description here..."
)

# ----------------------------------
# Resume Upload (MULTIPLE PDFs)
# ----------------------------------
uploaded_files = st.file_uploader(
    "📎 Upload Resumes (PDF only – up to 100)",
    type=["pdf"],
    accept_multiple_files=True
)

# ----------------------------------
# PDF Text Extraction
# ----------------------------------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text.strip()

# ----------------------------------
# Run Screening
# ----------------------------------
if st.button("🚀 Run AI Screening"):
    if not jd_text:
        st.warning("Please paste the Job Description.")
    elif not uploaded_files:
        st.warning("Please upload at least one Resume PDF.")
    elif len(uploaded_files) > 100:
        st.warning("You can upload a maximum of 100 resumes at a time.")
    else:
        st.success(f"Processing {len(uploaded_files)} candidate(s)")
        
        with st.spinner("🤖 AI agents are evaluating candidates..."):
            results = []

            for resume_file in uploaded_files:
                resume_text = extract_text_from_pdf(resume_file)

                evaluation_output = run_ai_screening(
                    job_description=jd_text,
                    resume_text=resume_text
                )

                results.append({
                    "name": resume_file.name,
                    "output": evaluation_output
                })

        st.success("✅ All evaluations completed")

        st.divider()
        st.header("📊 Hiring Evaluation Results")

        # ----------------------------------
        # DISPLAY RESULTS (HR FRIENDLY)
        # ----------------------------------
        for idx, result in enumerate(results, start=1):
            with st.expander(f"👤 Candidate {idx}: {result['name']}", expanded=(idx == 1)):
                
                lines = [
                    line.strip()
                    for line in result["output"].split("\n")
                    if line.strip()
                ]

                for line in lines:
                    # Match percentage highlight
                    if "%" in line:
                        st.markdown(f"### 🎯 **{line}**")

                    # Fit category
                    elif "Fit Category" in line:
                        st.markdown(f"### 🧩 {line}")

                    # Strengths
                    elif "Strength" in line:
                        st.markdown(f"#### 💪 {line}")

                    # Gaps / Risks
                    elif "Gap" in line or "Concern" in line:
                        st.markdown(f"#### ⚠️ {line}")

                    # Final recommendation
                    elif "Recommendation" in line:
                        st.markdown(f"### ✅ **{line}**")

                    else:
                        st.markdown(f"- {line}")
