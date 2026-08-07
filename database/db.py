import sqlite3

db = sqlite3.connect(
    "recipes.db",
    check_same_thread=False
)

db.row_factory = sqlite3.Row

cursor = db.cursor()

print("✅ SQLite Connected Successfully!")