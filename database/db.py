import sqlite3
import pandas as pd


def create_database():
    conn = sqlite3.connect("gram_ai.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        occupation TEXT,
        income REAL
    )
    """)

    conn.commit()
    conn.close()


def save_user(name, age, gender, occupation, income):
    conn = sqlite3.connect("gram_ai.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users
    (name, age, gender, occupation, income)
    VALUES (?, ?, ?, ?, ?)
    """, (name, age, gender, occupation, income))

    conn.commit()
    conn.close()


def get_schemes():
    try:
        df = pd.read_csv("data/schemes.csv")
        return df.to_dict(orient="records")
    except Exception as e:
        print("Error loading schemes:", e)
        return []


create_database()