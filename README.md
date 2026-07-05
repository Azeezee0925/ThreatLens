# 🛡️ ThreatLens AI – AI-Powered Threat Intelligence & OWASP Risk Analysis Platform

## Overview

ThreatLens AI is an intelligent cybersecurity platform developed to automate the investigation and analysis of Indicators of Compromise (IOCs) using multiple threat intelligence sources.

The platform checks IP addresses, domains, URLs, and file hashes using public threat intelligence APIs, performs AI-assisted threat analysis, maps threats to OWASP Top 10 and MITRE ATT&CK, correlates available CVEs, generates downloadable PDF reports, and provides dashboard analytics and real-time alerting.

---

## Features

### 🔍 IOC Investigation

Supports investigation of:

* IP Addresses
* Domains
* URLs
* MD5 Hashes
* SHA1 Hashes
* SHA256 Hashes

---

### 🌐 Threat Intelligence Sources

Integrated with:

* VirusTotal API
* AbuseIPDB API
* AlienVault OTX API

---

### 🤖 AI Threat Analysis

Automatically generates:

* Executive Summary
* Risk Assessment
* Key Findings
* AI Recommendation

---

### 🎯 Threat Scoring

ThreatLens Intelligence Engine combines multiple threat intelligence sources into a unified ThreatLens Score to classify IOCs as:

* Safe
* Suspicious
* Malicious

---

### 🛡️ OWASP Top 10 Mapping

Automatically maps detected threats to relevant OWASP Top 10 categories such as:

* Injection
* Broken Access Control
* Identification & Authentication Failures
* Security Misconfiguration
* Vulnerable Components
* Server-Side Request Forgery (SSRF)

---

### ⚔️ MITRE ATT&CK Mapping

Correlates detected threats with MITRE ATT&CK tactics and techniques to improve threat understanding.

Examples include:

* Initial Access
* Command and Control
* Defense Evasion
* Execution

---

### 🧩 CVE Correlation

Checks for known Common Vulnerabilities and Exposures (CVEs) associated with investigated IOCs.

Displays:

* CVE availability
* Related CVEs
* Number of CVEs

---

### 📊 Dashboard Analytics

Provides security monitoring statistics including:

* Total Investigations
* IOC Distribution
* Threat Distribution

---

### 🚨 Alerts

Displays high-risk investigations requiring immediate attention, supporting incident response workflows.

---

### 📄 PDF Report Generation

Generate downloadable investigation reports containing:

* IOC Details
* Threat Analysis
* Threat Scores
* AI Recommendations
* MITRE Mapping
* OWASP Mapping
* CVE Information

---

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript

### Backend

* FastAPI
* SQLAlchemy
* SQLite

### APIs

* VirusTotal
* AbuseIPDB
* AlienVault OTX
* NVD API

---

## System Architecture

User

↓

Next.js Frontend

↓

FastAPI Backend

↓

Threat Intelligence APIs

• VirusTotal

• AbuseIPDB

• AlienVault OTX

↓

ThreatLens Intelligence Engine

↓

AI Analysis

↓

Dashboard • Alerts • Reports

---

# Installation

## Clone the repository

```bash
git clone https://github.com/Azeezee0925/ThreatLens.git
cd ThreatLens
```

## Backend Setup

```bash
cd backend
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create environment file

Create a `.env` file and add your API keys:

```env
VIRUSTOTAL_API_KEY=YOUR_API_KEY
ABUSEIPDB_API_KEY=YOUR_API_KEY
ALIENVAULT_API_KEY=YOUR_API_KEY
```

### Start the backend

```bash
uvicorn app.main:app --reload
```

The backend will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Open a new terminal.

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at:

```
http://localhost:3000
```


## Key Capabilities

* IOC Enrichment
* Threat Intelligence Collection
* Threat Scoring
* AI-powered Threat Analysis
* OWASP Mapping
* MITRE ATT&CK Mapping
* CVE Correlation
* Dashboard Analytics
* Real-Time Alerts
* PDF Report Generation

---

## Future Enhancements

* Threat Feed Aggregation
* Email Alert Notifications
* Threat Trend Prediction
* User Authentication
* Role-Based Access Control
* SIEM Integration
* Cloud Deployment
* Docker Support

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Cyber Threat Intelligence
* Digital Forensics Concepts
* REST API Development
* FastAPI Backend Development
* Next.js Frontend Development
* Database Design using SQLAlchemy
* AI-assisted Threat Analysis
* OWASP Top 10
* MITRE ATT&CK Framework
* CVE Correlation
* Git & GitHub
* Full Stack Cybersecurity Application Development

---

## Author

**Azeeza Maalin M**

AI-Powered Threat Intelligence & OWASP Risk Analysis Platform

Internship Project – 2026
