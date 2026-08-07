import sqlite3
import pandas as pd

db = sqlite3.connect("recipes.db")

recipes = pd.read_csv("dataset/recipes.csv")

recipes.to_sql(
    "recipes",
    db,
    if_exists="append",
    index=False
)

db.commit()

print("✅ Recipes Imported Successfully!")