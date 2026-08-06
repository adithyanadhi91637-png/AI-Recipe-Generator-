def recommend(recipes, user_ingredients):

    matched_recipes = []

    for row in recipes:

        recipe_ingredients = [
            item.strip()
            for item in row["ingredients"].lower().split(",")
        ]

        match_count = 0

        for ingredient in user_ingredients:

            if ingredient in recipe_ingredients:
                match_count += 1

        if match_count > 0:

            matched_recipes.append({

    "recipe": row["recipe_name"],

    "matches": match_count,

    "description": row["description"],

    "time": row["cooking_time"],

    "difficulty": row["difficulty"],

    "image": row["image"]

})

    matched_recipes.sort(
        key=lambda x: x["matches"],
        reverse=True
    )

    return matched_recipes