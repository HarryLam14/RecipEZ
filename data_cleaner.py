import pandas as pd
import ast

# Loads the raw data into a pandas dataframe
interaction = pd.read_csv("RAW_interactions.csv")
recipes = pd.read_csv("RAW_recipes.csv")

# Removes unwanted columns
interaction.drop(["review","user_id","date"], axis=1, inplace=True)
recipes.drop(["contributor_id","submitted","tags","n_steps","n_ingredients"], axis=1, inplace=True)

# Strip quotes from ingredients, nutrition and steps lists; finally lists are recognised as list types and not string types;
# Strips unwanted whitespaces and \n characters from name and description
recipes['ingredients'] = recipes['ingredients'].map(lambda x: ast.literal_eval(x))
recipes['nutrition'] = recipes['nutrition'].map(lambda x: ast.literal_eval(x))
recipes['steps'] = recipes['steps'].map(lambda x: ast.literal_eval(x))
recipes['name'] = recipes['name'].map(lambda x: ' '.join(str(x).split()))
recipes['description'] = recipes['description'].map(lambda x: ' '.join(str(x).split()))


# Find average rating of each recipe
ratings = interaction.groupby("recipe_id").sum() / interaction.groupby("recipe_id").count()
# Count number of reviews
ratings["n_reviews"] = interaction.groupby("recipe_id").count()

# Left join tables to preserve all rows of recipe table and provide ratings info where applicable
preprocessed_data = pd.merge(left=recipes, right=ratings, how='left', left_on='id', right_on='recipe_id')
preprocessed_data.drop(["id"], axis=1, inplace=True)

# Creates new json and saves cleaned data to it;
# indent prettifies the data, orient changes the notation of the data
# (values for orient='split', 'records', 'index', 'columns', 'values', 'table')
preprocessed_data.to_json("CLEANED_JOINED_data.json", orient='index', indent=4)