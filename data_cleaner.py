import pandas as pd

# Loads the raw data into a pandas dataframe
interaction = pd.read_csv("RAW_interactions.csv")
recipes = pd.read_csv("RAW_recipes.csv")

# Removes unwanted columns
interaction.drop(["review","user_id","date"], axis=1, inplace=True)
recipes.drop(["contributor_id","submitted","tags","n_steps","n_ingredients"], axis=1, inplace=True)

# Strip quotes from ingredient lists
recipes['ingredients'] = recipes['ingredients'].map(lambda x: x.strip('"'))


# Find average rating of each recipe
ratings = interaction.groupby("recipe_id").sum() / interaction.groupby("recipe_id").count()
# Count number of reviews
ratings["n_reviews"] = interaction.groupby("recipe_id").count()

# Left join tables to preserve all rows of recipe table and provide ratings info where applicable
preprocessed_data = pd.merge(left=recipes, right=ratings, how='left', left_on='id', right_on='recipe_id')
preprocessed_data.drop(["id"], axis=1, inplace=True)

# Creates new csv and saves cleaned data to it
preprocessed_data.to_csv("CLEANED_JOINED_data.csv", index=False)