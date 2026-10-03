import streamlit as st
import ollama

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Phishing Analyzer",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🛡️ AI Phishing Email Analyzer")

st.write(
    "Analyze suspicious emails using a free local AI model "
    "and identify phishing indicators, social engineering "
    "techniques and MITRE ATT&CK mappings."
)

st.divider()

# --------------------------------------------------
# EMAIL INPUT
# --------------------------------------------------

email = st.text_area(
    "📧 Paste suspicious email here:",
    height=300,
    placeholder="Paste the complete email including sender, subject and message..."
)

# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------

if st.button("🔍 Analyze Email", type="primary"):

    if not email.strip():

        st.warning("⚠️ Please paste an email first.")

    else:

        prompt = f"""
You are a cybersecurity email analysis assistant.

Analyze the email below for possible phishing.

Return the answer using exactly this structure:

RISK LEVEL:
Choose LOW, MEDIUM, or HIGH.

RISK SCORE:
Give a number from 0 to 100.

SUMMARY:
Give a short explanation in 2-3 sentences.

PHISHING INDICATORS:
Give 3-6 specific warning signs found in the email.

SOCIAL ENGINEERING:
Identify techniques such as urgency, fear, impersonation,
authority, reward, curiosity, or credential harvesting.

MITRE ATT&CK:
If applicable, identify the relevant MITRE ATT&CK technique.
Include the technique ID and name.
If there is not enough evidence, say "Not enough evidence."

RECOMMENDED ACTIONS:
Give 3-5 safe actions the user should take.

IMPORTANT:
This is an AI-assisted assessment, not a definitive
determination that an email is malicious.

EMAIL:
{email}
"""

        # --------------------------------------------------
        # AI ANALYSIS
        # --------------------------------------------------

        with st.spinner("🤖 AI is analyzing the email..."):

            try:

                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                result = response["message"]["content"]

            except Exception as e:

                st.error("❌ Could not connect to Ollama.")
                st.code(str(e))
                st.stop()

        # --------------------------------------------------
        # DISPLAY RESULT
        # --------------------------------------------------

        st.divider()

        st.subheader("📊 Analysis Result")

        # Risk level detection
        result_upper = result.upper()

        if "RISK LEVEL:" in result_upper:

            if "HIGH" in result_upper:
                st.error("🚨 HIGH RISK — Possible Phishing")

            elif "MEDIUM" in result_upper:
                st.warning("⚠️ MEDIUM RISK — Suspicious Email")

            elif "LOW" in result_upper:
                st.success("✅ LOW RISK — No Major Phishing Indicators")

        # Full AI result
        st.markdown(result)

        # --------------------------------------------------
        # DOWNLOAD REPORT
        # --------------------------------------------------

        st.divider()

        st.subheader("📥 Download Analysis")

        report = f"""
AI PHISHING EMAIL ANALYZER
==========================

EMAIL ANALYZED
--------------

{email}

AI ANALYSIS
-----------

{result}

DISCLAIMER
----------

This analysis was generated using a local AI model.
It is an AI-assisted assessment and should not be
considered definitive proof that an email is malicious.
"""

        st.download_button(
            label="📄 Download Analysis Report",
            data=report,
            file_name="phishing_analysis.txt",
            mime="text/plain"
        )