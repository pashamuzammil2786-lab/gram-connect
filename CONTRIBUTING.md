# Contributing to Gram Connect

Thank you for contributing to Gram Connect. This project helps citizens discover government welfare schemes based on their personal profile.

## Project Goal

Gram Connect aims to reduce the information gap between rural citizens and government welfare schemes. Many citizens are unaware of available schemes, eligibility rules, required documents, benefits, and application links.

This project provides a simple digital platform where users can enter their details and find schemes that may match their profile.

## Current Technology Stack

- Python
- Streamlit
- SQLite
- CSV dataset
- Rule-based eligibility checking

## Setup Instructions

Clone the repository:

```bash
git clone https://code.swecha.org/sweety28/gram-connect.git
cd gram-connect
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

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
├── requirements.txt
├── README.md
└── test_db.py
```

## Important Files

- `app.py`: Main Streamlit home page.
- `pages/1_Register.py`: Citizen registration form.
- `pages/2_Eligible_Schemes.py`: Page for displaying eligible schemes.
- `pages/3_About.py`: About page for the project.
- `backend/eligibility.py`: Rule-based eligibility checking logic.
- `database/db.py`: SQLite database helper functions.
- `data/schemes.csv`: Main government scheme dataset.
- `data/source_notes.md`: Source notes for scheme information.

## How to Contribute

You can contribute by:

- Adding new government schemes to `data/schemes.csv`.
- Updating source references in `data/source_notes.md`.
- Improving the eligibility logic.
- Improving Streamlit page design.
- Fixing bugs.
- Adding missing form fields.
- Improving documentation.
- Testing the app and reporting issues.

## Scheme Data Guidelines

All scheme data should be added to:

```text
data/schemes.csv
```

Each scheme should include these fields:

```text
scheme_name
description
min_age
max_age
gender
occupation
income_limit
state
caste
disability
education
benefits
application_process
application_link
```

Use `Any` when a scheme does not restrict a field.

Example:

```csv
PM Kisan Samman Nidhi,Income support scheme for eligible farmer families,18,100,Any,Farmer,999999999,Any,Any,Any,Any,Direct income support,Apply through PM-Kisan portal,https://pmkisan.gov.in/
```

## Data Source Rules

- Prefer official government websites.
- Add every source to `data/source_notes.md`.
- Recheck links before final presentation or submission.
- Avoid adding schemes without a source.
- Avoid duplicate schemes.
- Keep scheme names clear and official.

## Coding Guidelines

- Keep code simple and readable.
- Use meaningful variable names.
- Avoid unnecessary complex logic.
- Keep functions small when possible.
- Do not remove existing work without checking.
- Do not commit generated files such as `__pycache__/`.
- Use comments only when they help explain non-obvious logic.

## Testing Checklist

Before submitting changes, check:

- The app starts with `streamlit run app.py`.
- The registration page opens correctly.
- The eligible schemes page does not crash.
- New CSV rows are formatted correctly.
- Scheme source links work.
- No generated cache files are committed.

## Suggested Next Improvements

- Connect the eligible schemes page to the real eligibility engine.
- Add `get_schemes()` to load data from `data/schemes.csv`.
- Add missing form fields such as caste.
- Save complete user profile data.
- Show scheme benefits, application process, and official links.
- Add Telugu language support.
- Add document guidance for each scheme.

