# 🛡️ AI Phishing Email Analyzer

## Overview

AI Phishing Email Analyzer is a cybersecurity tool that
uses a local Large Language Model (LLM) to analyze emails
for potential phishing indicators.

The application provides a risk assessment, suspicious
indicators, social engineering analysis, MITRE ATT&CK
mapping and recommended defensive actions.

## Features

- 🔍 Phishing email analysis
- 📊 Risk level
- 📈 Risk score
- ⚠️ Phishing indicators
- 🎭 Social engineering detection
- 🎯 MITRE ATT&CK mapping
- 📄 Downloadable analysis
- 🔒 Local AI processing

## Technologies

- Python
- Streamlit
- Ollama
- Llama 3.2
- Prompt Engineering
- MITRE ATT&CK

## How It Works

User enters an email.

↓

Streamlit sends the email to Ollama.

↓

Llama 3.2 analyzes the email.

↓

The application displays the security assessment.

## Installation

Install the required packages:

```bash
pip install -r requirements.txt

Install Ollama and download the model:

ollama pull llama3.2

Run the application:

python -m streamlit run app.py

Example:
The tool can identify potential indicators such as:

Urgent language
Suspicious links
Credential requests
Impersonation
Fear-based language
Social engineering

Disclaimer:

This project provides an AI-assisted assessment.

It should not be treated as a definitive determination
that an email is malicious or safe.

Security professionals should perform additional
investigation before making a final decision.
