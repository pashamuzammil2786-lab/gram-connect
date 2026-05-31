# Gram Connect User Manual

## About Gram Connect

Gram Connect is a government scheme eligibility finder. It helps citizens discover welfare schemes based on profile details such as age, gender, occupation, annual income, state, education, and disability status.

The project is mainly designed to support rural citizens who may not know which government schemes they can apply for.The manual is kept up to date with the current Streamlit implementation.
## Purpose of the App

Many citizens miss government benefits because they do not know:

- Which schemes exist.
- Whether they are eligible.
- What benefits are provided.
- Where to apply.
- Which official links to use.

Gram Connect provides a simple interface to reduce this confusion.

## How to Run the App

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the Streamlit app:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal.

It usually looks like:

```text
http://localhost:8501
```

## How to Use Gram Connect

1. Open the app in your browser.
2. Go to the **Citizen Registration** page from the sidebar.
3. Enter the citizen details.
4. Click **Check Eligibility**.
5. Go to the **Eligible Schemes** page.
6. View the schemes displayed for the profile.

## Pages in the App

### Home Page

The home page introduces Gram Connect and explains that the app helps citizens find government welfare schemes.

### Citizen Registration Page

This page collects citizen details.

Current form fields include:

- Full name
- Age
- Gender
- Occupation
- Annual income
- State
- Education
- Disability status

After entering the details, click **Check Eligibility**.

### Eligible Schemes Page

This page is used to show schemes that match the citizen profile.

Current note: this page may still show sample hardcoded schemes until the full eligibility engine is connected.

### About Page

This page explains the objective of Gram Connect and the project team roles.

## Scheme Dataset

Scheme information is stored in:

```text
data/schemes.csv
```

The dataset includes:

- Scheme name
- Scheme description
- Eligibility rules
- Benefits
- Application process
- Official application link

Examples of schemes in the dataset:

- PM Kisan Samman Nidhi
- Ayushman Bharat PM-JAY
- PM Awas Yojana Gramin
- Telangana Rythu Bandhu
- Telangana Aasara Pension
- PM Ujjwala Yojana
- PM Vishwakarma
- AP NTR Bharosa Pension

## Troubleshooting

### App does not start

Run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Eligible schemes are not showing correctly

Check:

- Whether user details were entered on the registration page.
- Whether the eligible schemes page is connected to the eligibility logic.
- Whether `data/schemes.csv` contains valid data.

### Import error for `get_schemes`

This means the eligibility engine expects a function named `get_schemes()` in `database/db.py`, but that function still needs to be implemented.

### CSV formatting issue

Check that:

- The header row is present.
- Every row has the same number of columns.
- Text containing commas is properly quoted.
- Required fields are not empty.

## Important Disclaimer

Gram Connect is a helper tool. It should not be treated as the final official decision for government scheme eligibility.

Users should confirm final eligibility through:

- Official government portals
- MeeSeva centers
- Gram Panchayat offices
- Welfare department offices
- Scheme-specific official websites

Scheme rules can change, so official sources should always be verified.

