import mysql.connector

try:

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="ai_recipe_generator_db"
    )

    cursor = db.cursor(dictionary=True)

    print("Database Connected!")

except mysql.connector.Error as err:

    print(err)