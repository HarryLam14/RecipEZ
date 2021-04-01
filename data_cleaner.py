import pandas as pd

# Loads the raw data into a pandas dataframe
interaction = pd.read_csv("RAW_interactions.csv")
recipes = pd.read_csv("RAW_recipes.csv")

# Removes unwated columns
interaction.drop(["review","user_id","date"],axis=1,inplace=True)
recipes.drop(["contributor_id","submitted","tags","n_steps","n_ingredients"],axis=1,inplace=True)

# Creates new csv and saves cleaned data to it
interaction.to_csv("CLEANED_interactions.csv",index=False)
recipes.to_csv("CLEANED_recipes.csv",index=False)