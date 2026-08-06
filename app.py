import pandas as pd
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from models.recommender import recommend
from database.db import cursor, db

app = Flask(__name__)

app.secret_key = "CookSmart@AI_Recipe_2026_Secure_Key"

print("✅ Connected to MySQL Successfully!")


@app.route("/")
def home():

    return render_template(
        "index.html",
        username=session.get("user_name")
    )



@app.route("/login", methods=["GET", "POST"])
def login():

    

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cursor.fetchone()

        if user:

            if check_password_hash(
                user["password"],
                password
            ):

                session["user_id"] = user["id"]
                session["user_name"] = user["name"]

                flash("Login Successful!")

                return redirect("/")

        flash("Invalid Email or Password")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:

            flash("Passwords do not match!")

            return redirect("/register")

        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        existing_user = cursor.fetchone()

        if existing_user:

            flash("Email already registered!")

            return redirect("/register")

        hashed_password = generate_password_hash(password)

        cursor.execute(
            """
            INSERT INTO users(name,email,password)
            VALUES(%s,%s,%s)
            """,
            (
                name,
                email,
                hashed_password
            )
        )

        db.commit()

        flash("Registration Successful! Please Login.")

        return redirect("/login")

    return render_template("register.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@app.route("/predict", methods=["POST"])
def predict():

    ingredients = request.form["ingredients"].lower()

    user_ingredients = [

        item.strip()

        for item in ingredients.split(",")

        if item.strip()

    ]

    cursor.execute(
        "SELECT * FROM recipes"
    )

    recipes = cursor.fetchall()

    matched_recipes = recommend(

        recipes,

        user_ingredients

    )
    if "user_id" in session:

      cursor.execute(
        """
        INSERT INTO search_history
        (user_id, ingredients)
        VALUES (%s, %s)
        """,
        (
            session["user_id"],
            ", ".join(user_ingredients)
        )
    )

    db.commit()

    return render_template(

        "results.html",

        recipes=matched_recipes,

        ingredients=user_ingredients

    )


@app.route("/recipe/<int:id>")
def recipe(id):

    cursor.execute(

        "SELECT * FROM recipes WHERE id=%s",

        (id,)

    )

    recipe = cursor.fetchone()

    return render_template(

        "recipe.html",

        recipe=recipe

    )


@app.route("/history")
def history():

    if "user_id" not in session:

        return redirect("/login")

    cursor.execute(
        """
        SELECT ingredients,
               searched_at
        FROM search_history
        WHERE user_id=%s
        ORDER BY searched_at DESC
        """,
        (session["user_id"],)
    )

    history = cursor.fetchall()

    return render_template(
        "history.html",
        history=history
    )




if __name__ == "__main__":

    app.run(debug=True)