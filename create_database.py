import sqlite3

db = sqlite3.connect("recipes.db")
cursor = db.cursor()

# Users table
cursor.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Recipes table
cursor.execute("""
CREATE TABLE recipes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe TEXT,
    ingredients TEXT,
    description TEXT,
    instructions TEXT,
    image TEXT,
    time TEXT,
    difficulty TEXT
)
""")

# Search History table
cursor.execute("""
CREATE TABLE search_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    ingredients TEXT,
    searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

db.commit()

print("Database Created Successfully!")