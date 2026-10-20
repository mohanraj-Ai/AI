import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / "company.db"


def create_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            role TEXT NOT NULL,
            salary INTEGER NOT NULL
        )
    """)

    employees = [
        (1, "Arun", "AI", "AI Engineer", 800000),
        (2, "Priya", "AI", "ML Engineer", 750000),
        (3, "Rahul", "Software", "Python Developer", 650000),
        (4, "Divya", "Software", "Backend Developer", 700000),
        (5, "Karthik", "Automotive", "Automotive Engineer", 600000),
        (6, "Meena", "AI", "Data Scientist", 850000),
        (7, "Vijay", "Automotive", "ADAS Engineer", 900000),
        (8, "Anitha", "HR", "HR Executive", 500000),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO employees
        (id, name, department, role, salary)
        VALUES (?, ?, ?, ?, ?)
    """, employees)

    connection.commit()
    connection.close()

    print(f"Database created successfully: {DB_PATH}")


if __name__ == "__main__":
    create_database()