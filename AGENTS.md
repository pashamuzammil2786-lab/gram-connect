# AGENTS.md

This file provides guidance for developers and AI agents working on Gram Connect.

## Project Overview

Gram Connect is a Streamlit-based government scheme eligibility finder. It compares citizen profile information with scheme rules stored in a CSV dataset.

The main goal is to help rural citizens discover welfare schemes that may apply to them.
This guidance file is also used for AI agent support during development.

## Current Architecture

```text
User enters details
→ Streamlit stores profile
→ eligibility.py checks rules
→ schemes.csv provides scheme data
→ matching schemes are displayed
```

## Current Technology

- Python
- Streamlit
- SQLite
- CSV
- Rule-based matching

The README may describe a future React, FastAPI, or AI/RAG system, but the current implemented project is Streamlit.

## Important Files

```text
app.py
```

Main Streamlit entry page.

```text
pages/1_Register.py
```

Collects citizen profile details.

```text
pages/2_Eligible_Schemes.py
```

Displays eligible schemes.

```text
pages/3_About.py
```

Shows project objective and team information.

```text
backend/eligibility.py
```

Contains rule-based eligibility checking.

```text
database/db.py
```

Handles SQLite user database functions.

```text
data/schemes.csv
```

Stores scheme data and eligibility rules.

```text
data/source_notes.md
```

Stores source references for scheme data.

## Known Current Gaps

- `backend/eligibility.py` imports `get_schemes()` from `database.db`.
- `get_schemes()` may still need to be implemented.
- The eligible schemes page may still use hardcoded sample schemes.
- The registration form may not collect all fields required by the eligibility logic, especially `caste`.
- The README describes a larger future architecture, but the real app is currently Streamlit.

## Recommended Development Tasks

1. Add `get_schemes()` in `database/db.py`.
2. Load schemes from `data/schemes.csv` using `csv.DictReader`.
3. Add missing form fields such as caste.
4. Connect `pages/2_Eligible_Schemes.py` to `check_eligibility()`.
5. Show scheme name, description, benefits, application process, and official link.
6. Add graceful handling when no schemes match.
7. Add `.gitignore` for Python cache files.

## Eligibility Rule Notes

The eligibility engine checks:

- Age range
- Income limit
- Gender
- Occupation
- State
- Caste
- Disability
- Education

Use `Any` when a scheme accepts all values for a field.

Expected scheme fields:

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

## Development Commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Run app:

```bash
streamlit run app.py
```

Compile check:

```bash
python3 -m py_compile app.py pages/1_Register.py pages/2_Eligible_Schemes.py pages/3_About.py database/db.py backend/eligibility.py test_db.py
```

## Agent Instructions

- Work with the current Streamlit implementation.
- Do not assume React, FastAPI, LangChain, or RAG files exist.
- Keep changes simple and useful for an academic project demo.
- Do not remove team information without permission.
- Keep scheme data backed by official or reliable sources.
- Avoid unrelated refactoring.
- Do not commit generated folders such as `__pycache__/`.

## Documentation Update Rules

When functionality changes, update:

- `README.md` for project overview.
- `USER_MANUAL.md` for user instructions.
- `CONTRIBUTING.md` for contributor workflow.
- `data/source_notes.md` when scheme data changes.

