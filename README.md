# Gram Connect – Rural Telangana Government Scheme Assistant

## Project Overview

Gram Connect is an AI-powered platform designed to help rural citizens of Telangana access government welfare schemes easily. The application provides scheme recommendations, eligibility checking, document guidance, and AI-based assistance in Telugu and English.

## Problem Statement

Many rural citizens are unaware of government schemes, eligibility criteria, required documents, and application procedures. Gram Connect aims to bridge this information gap through a simple and user-friendly digital platform.

## Key Features

- Government Scheme Search
- Eligibility Checker
- AI Chatbot Assistant
- Telugu and English Language Support
- Document Guidance
- Complaint and Feedback Module
- Government Notifications and Updates


#Git
git clone https://code.swecha.org/sweety28/gram-connect.git

## Technology Stack

### Frontend
- React.js
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI

### Database
- SQLite / MongoDB

### AI Components
- RAG (Retrieval-Augmented Generation)
- LangChain
- Hugging Face / OpenAI APIs

### Deployment
- GitLab
- Vercel

## Project Architecture

User → Frontend → Backend API → Database + AI Engine → Response 

gram-connect/
│
├── frontend/
│   │
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.js
│   │   │   ├── Hero.js
│   │   │   ├── Chatbot.js
│   │   │   ├── SchemeCard.js
│   │   │   └── Footer.js
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.js
│   │   │   ├── Search.js
│   │   │   ├── Eligibility.js
│   │   │   └── ChatbotPage.js
│   │   │
│   │   ├── App.js
│   │   └── index.js
│   │
│   └── package.json
│
├── backend/
│   │
│   ├── app.py
│   ├── routes/
│   ├── models/
│   ├── services/
│   └── requirements.txt
│
├── database/
│   │
│   ├── schemes.db
│   ├── scheme_data.csv
│   └── schema.sql
│
├── ai-rag/
│   │
│   ├── documents/
│   ├── embeddings/
│   ├── vectorstore/
│   ├── chatbot.py
│   └── rag_pipeline.py
│
├── testing/
│   │
│   ├── test_cases.md
│   └── bug_reports.md
│
├── README.md
├── CONTRIBUTORS.md
├── USER_MANUAL.md
└── AGENTS.md

## Future Enhancements

- Voice Assistant in Telugu
- Mobile Application
- Real-time Government Updates
- Personalized Scheme Recommendations

## Team Members

- Mounika Patnaik 1 – Project Lead & Frontend Developer
- MUZAMIL 2 – Backend Developer
- JAITI 3 – Database & Data Collection
- BHAVANI 4 – AI/RAG Developer
- SUSHMITHA 5 – Testing, Documentation & Deployment

## Project Status

Currently under development as an academic group project.