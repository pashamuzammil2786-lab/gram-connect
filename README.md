# Gram Connect

Gram Connect is a Streamlit-based government scheme eligibility finder. It helps citizens discover welfare schemes by comparing their profile details with scheme rules stored in a CSV dataset.

The project is designed mainly for rural citizens who may not know which government schemes they are eligible for or where to apply.

## Project Overview

Many citizens miss government benefits because information about schemes, eligibility rules, benefits, and application processes is difficult to find in one place.

Gram Connect provides a simple web interface where users can enter their basic details and view possible schemes that may match their profile.

## Current Features

- Citizen registration form
- Simple Streamlit web interface
- Government scheme dataset in CSV format
- Rule-based eligibility checking logic
- SQLite helper for saving basic user details
- Source notes for scheme data
- Project documentation for users, contributors, and developers

## Current Technology Stack

- Python
- Streamlit
- SQLite
- CSV
- Rule-based matching

## Project Structure

```text
gram-connect/
├── app.py
├── pages/
│   ├── 1_Register.py
│   ├── 2_Eligible_Schemes.py
│   └── 3_About.py
├── backend/
│   └── eligibility.py
├── database/
│   └── db.py
├── data/
│   ├── schemes.csv
│   └── source_notes.md
├── CONTRIBUTING.md
├── USER_MANUAL.md
├── AGENTS.md
├── requirements.txt
├── test_db.py
└── README.md
```

## Important Files

- `app.py`: Main Streamlit home page.
- `pages/1_Register.py`: Citizen registration form.
- `pages/2_Eligible_Schemes.py`: Eligible schemes display page.
- `pages/3_About.py`: About page for the project.
- `backend/eligibility.py`: Rule-based eligibility logic.
- `database/db.py`: SQLite database helper functions.
- `data/schemes.csv`: Main government scheme dataset.
- `data/source_notes.md`: Source references for scheme data.
- `CONTRIBUTING.md`: Contribution guide.
- `USER_MANUAL.md`: User guide for running and using the app.
- `AGENTS.md`: Developer and AI-agent guidance.

## How to Run the Project

1. Clone the repository:

```bash
git clone https://code.swecha.org/sweety28/gram-connect.git
cd gram-connect
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the Streamlit app:

```bash
streamlit run app.py
```

4. Open the local URL shown in the terminal.

It usually looks like:

```text
http://localhost:8501
```

## How the App Works

```text
User enters profile details
→ Streamlit stores the profile
→ Eligibility logic compares profile with scheme rules
→ Scheme data is read from data/schemes.csv
→ Matching schemes are shown to the user
```

## Scheme Dataset

Scheme information is stored in:

```text
data/schemes.csv
```

Each scheme record includes:

- Scheme name
- Description
- Minimum and maximum age
- Gender rule
- Occupation rule
- Income limit
- State
- Caste
- Disability status
- Education rule
- Benefits
- Application process
- Official application link

Use `Any` when a scheme does not restrict a field.

## Example Schemes in the Dataset

- PM Kisan Samman Nidhi
- Ayushman Bharat PM-JAY
- PM Awas Yojana Gramin
- Telangana Rythu Bandhu
- Telangana Aasara Pension
- Telangana Kalyana Lakshmi Shaadi Mubarak
- PM Ujjwala Yojana
- PM Vishwakarma
- AP NTR Bharosa Pension
- AP Deepam 2.0

## Current Status

Gram Connect is currently an academic project MVP.

The current implemented version is based on Streamlit, CSV data, SQLite, and rule-based eligibility checking.

Some features mentioned as future goals, such as AI chatbot support, Telugu voice assistant, React frontend, FastAPI backend, and RAG-based search, are not part of the current implemented version yet.

## Known Gaps

- The eligible schemes page may still need to be fully connected to the eligibility engine.
- `backend/eligibility.py` expects a `get_schemes()` function for loading scheme data.
- The registration form may need additional fields such as caste.
- Some government scheme rules are simplified for CSV-based matching.
- Official scheme rules should be verified before final submission or real-world use.

## Future Enhancements

- Connect the eligible schemes page to the real CSV-based eligibility engine.
- Add `get_schemes()` to load schemes from `data/schemes.csv`.
- Add missing citizen profile fields.
- Show full scheme details, benefits, application process, and links.
- Add Telugu language support.
- Add document guidance for each scheme.
- Add search and filter options.
- Add AI chatbot or RAG-based question answering.
- Add voice assistant support.
- Improve mobile-friendly UI.

## Team Members

- Mounika Patnaik 1 - Project Lead & Frontend Developer
- MUZAMIL 2 - Backend Developer
- JAITI 3 - Database & Data Collection
- BHAVANI 4 - AI/RAG Developer
- SUSHMITHA 5 - Testing, Documentation & Deployment

## Disclaimer

Gram Connect is a helper tool for awareness and initial guidance. It should not be treated as the final official decision for government scheme eligibility.

Users should verify eligibility through official government portals, MeeSeva centers, Gram Panchayat offices, welfare department offices, or scheme-specific websites.

