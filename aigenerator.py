# ==================================================
# AI CV SCREENING SYSTEM - PRODUCT VERSION (NO LOGIN)
# Author: Arian Syahputra (Koyan)
# ==================================================

import streamlit as st
import pdfplumber
import requests
import json
import pandas as pd
import re
from io import BytesIO
from datetime import datetime

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="AI CV Screening Platform",
    page_icon="🤖",
    layout="wide"
)

# ==================================================
# API KEY
# ==================================================
OPENROUTER_API_KEY = "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"
MODEL_NAME = "liquid/lfm-2.5-1.2b-thinking:free"

# ==================================================
# HELPER FUNCTIONS
# ==================================================

def extract_text_from_pdf(uploaded_file):
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text[:4000]


def analyze_cv_with_ai(cv_text, user_prompt, role):
    system_prompt = {
        "HR": "You are a professional HR recruiter evaluating CV suitability objectively.",
        "Tech": "You are a senior technical interviewer focusing on technical depth.",
        "Manager": "You are a hiring manager focusing on impact, leadership, and ownership."
    }[role]

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": system_prompt + " Respond ONLY with valid JSON."
            },
            {
                "role": "user",
                "content": f"""
JOB REQUIREMENT:
{user_prompt}

CANDIDATE CV:
{cv_text}

Return JSON:
{{
  \"score\": number,
  \"summary\": string,
  \"strengths\": string,
  \"weaknesses\": string
}}
"""
            }
        ],
        "temperature": 0.2
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://portfolio.local",
            "X-Title": "AI CV Screening Platform",
        },
        data=json.dumps(payload),
        timeout=60
    )

    return response.json()


# ==================================================
# UI HEADER
# ==================================================
st.markdown(
    """
    <h1 style='text-align:center;'>🤖 AI CV Screening Platform</h1>
    <p style='text-align:center;color:gray;'>Fast • Objective • Recruiter-Friendly</p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ==================================================
# SIDEBAR (PRODUCT-LIKE)
# ==================================================
st.sidebar.title("🧭 Screening Setup")
role = st.sidebar.radio("Evaluation Perspective", ["HR", "Tech", "Manager"])
max_cv = st.sidebar.slider("Max CV per run", 1, 20, 10)
st.sidebar.markdown("---")
st.sidebar.caption("No login required • Session-based analysis")

# ==================================================
# MAIN INPUT
# ==================================================
st.subheader("📝 Job Requirement")
user_prompt = st.text_area(
    "Describe the role",
    placeholder="Example: BI Specialist with 3+ years experience, SQL, Power BI, Python"
)

st.subheader("📄 Candidate CVs (PDF)")
files = st.file_uploader(
    "Upload multiple CVs",
    type=["pdf"],
    accept_multiple_files=True
)

# ==================================================
# ACTION
# ==================================================
if st.button("🚀 Run Screening"):
    if not user_prompt or not files:
        st.warning("Please upload CVs and provide job requirement")
    else:
        results = []

        with st.spinner("🔍 AI is analyzing candidate CVs..."):
            for file in files[:max_cv]:
                cv_text = extract_text_from_pdf(file)
                ai_response = analyze_cv_with_ai(cv_text, user_prompt, role)

                if "choices" not in ai_response:
                    score, summary, strengths, weaknesses = 0, "AI Error", "-", "-"
                else:
                    content = ai_response["choices"][0]["message"]["content"]
                    match = re.search(r"\{.*\}", content, re.DOTALL)
                    if match:
                        parsed = json.loads(match.group())
                        score = parsed.get("score", 0)
                        summary = parsed.get("summary", "-")
                        strengths = parsed.get("strengths", "-")
                        weaknesses = parsed.get("weaknesses", "-")
                    else:
                        score, summary, strengths, weaknesses = 0, "Invalid AI output", "-", "-"

                results.append({
                    "Candidate": file.name,
                    "Score": score,
                    "Summary": summary,
                    "Strengths": strengths,
                    "Weaknesses": weaknesses
                })

        df = pd.DataFrame(results).sort_values("Score", ascending=False)

        # ==================================================
        # RESULTS (SIMPLIFIED & CLEAR)
        # ==================================================
        st.success("Screening completed")

        st.subheader("🏆 Recommended Candidates")

        for idx, row in df.iterrows():
            if row["Score"] >= 75:
                label = "Highly Recommended"
                emoji = "🟢"
            elif row["Score"] >= 50:
                label = "Consider"
                emoji = "🟡"
            else:
                label = "Not Recommended"
                emoji = "🔴"

            st.markdown(f"""
### {emoji} {row['Candidate']}
**Overall Match:** {row['Score']} / 100 — **{label}**

**Summary**  
{row['Summary']}

**Key Strengths**  
{row['Strengths']}

**Key Gaps**  
{row['Weaknesses']}
---
""")

        # ==================================================
        # EXPORT
        # ==================================================
        buffer = BytesIO()
        df.insert(0, "Screening Date", datetime.now().strftime("%Y-%m-%d %H:%M"))
        df.to_excel(buffer, index=False)
        buffer.seek(0)

        st.download_button(
            "📥 Export Result (Excel)",
            buffer,
            file_name="ai_cv_screening_result.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# ==================================================
# FOOTER
# ==================================================
st.markdown(
    """
    <hr>
    <center>
        <small>
            AI CV Screening Platform • Product Demo<br>
            Built by Arian Syahputra<br>
            <a href="https://wa.me/6285156343296" target="_blank">WhatsApp</a> | 
            <a href="https://www.linkedin.com/in/ariansyahputra/" target="_blank">LinkedIn</a>
        </small>
    </center>
    """,
    unsafe_allow_html=True
)
