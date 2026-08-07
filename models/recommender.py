def recommend(recipes, user_ingredients):

    matched_recipes = []

    for row in recipes:

        recipe_ingredients = [
            item.strip().lower()
            for item in row["ingredients"].split(",")
        ]

        match_count = 0

        for ingredient in user_ingredients:

            if ingredient.lower() in recipe_ingredients:
                match_count += 1

        if match_count > 0:

            matched_recipes.append({

                "id": row["id"],

                "recipe": row["recipe"],

                "matches": match_count,

                "description": row["description"],

                "instructions": row["instructions"],

                "time": row["time"],

                "difficulty": row["difficulty"],

                "image": row["image"]

            })

    matched_recipes.sort(
        key=lambda x: x["matches"],
        reverse=True
    )

    return matched_recipes