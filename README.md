# Agentic AI Resume Screening & Hiring Evaluation System

An AI-powered, multi-agent resume screening system that automates candidate evaluation by analyzing job descriptions and matching them with resumes to generate clear, explainable hiring insights.

---

## Overview

Recruiters often spend hours manually screening resumes, which is time-consuming and inconsistent.  
This project solves that problem by using an **Agentic AI architecture** to automate resume screening while maintaining transparency and human-readable outputs.

The system allows HR teams to upload a job description and screen **1 to 100 resumes in a single click**, generating suitability scores, strengths, gaps, and recommendations for each candidate.

---

## Key Features

- Multi-agent AI architecture for intelligent decision-making
- Automated extraction of job requirements
- Resume-to-job matching with skill gap analysis
- Hiring suitability score (25%–100%)
- Human-readable evaluation (not black-box AI)
- Streamlit-based simple web interface
- Reduces manual screening time by **8X–10X**

---

## System Architecture

The system is built using three coordinated AI agents:

1. **Planner Agent**
   - Analyzes the job description
   - Extracts required skills, experience, and criteria

2. **Resume Analyzer Agent**
   - Parses and evaluates candidate resumes
   - Identifies skills, experience, and qualifications

3. **Evaluator Agent**
   - Compares resumes with job requirements
   - Generates a suitability score with insights and recommendations

---

## Tech Stack

- Python
- Streamlit
- LLM-based AI Agents
- Natural Language Processing (NLP)

---

## How It Works

1. User uploads a job description
2. User uploads one or multiple resumes (PDF)
3. Planner Agent extracts hiring criteria
4. Resume Analyzer evaluates candidate profiles
5. Evaluator Agent generates:
   - Suitability score
   - Strengths
   - Skill gaps
   - Hiring recommendation

---

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sujal-kadam/Resume-Ai-Agent
   .\.venv\Scripts\python.exe -m streamlit run app.py

---

## Author

**Sujal Kadam**  
B.Sc. IT | AI & Automation 
LinkedIn: https://www.linkedin.com/in/sujal-kadam-b824a7398/  
GitHub: https://github.com/sujal-kadam/Resume-Ai-Agent
