import pandas as pd

# Loads the raw data into a pandas dataframe
interaction = pd.read_csv("RAW_interactions.csv")
recipes = pd.read_csv("RAW_recipes.csv")

# Removes unwated columns
interaction.drop(["review","user_id","date"], axis=1, inplace=True)
recipes.drop(["contributor_id","submitted","tags","n_steps","n_ingredients"], axis=1, inplace=True)

ratings = interaction.groupby("recipe_id").sum() / interaction.groupby("recipe_id").count()
ratings["n_reviews"] = interaction.groupby("recipe_id").count()
print(ratings.head())

preprocessed_data = pd.merge(left=recipes, right=ratings, how='left', left_on='id', right_on='recipe_id')
preprocessed_data.drop(["id"], axis=1, inplace=True)
print(preprocessed_data.head())

# Creates new csv and saves cleaned data to it
preprocessed_data.to_csv("CLEANED_JOINED_data.csv", index=False)