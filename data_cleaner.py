import pandas as pd
from ast import literal_eval

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

# Make ingredients column into list type
preprocessed_data.ingredients = preprocessed_data.ingredients.apply(literal_eval)

# Make list of all ingredients
ingredients = pd.DataFrame(preprocessed_data.ingredients.explode().unique()).reset_index()

# Split ingredients up and drop ingredients column (list type is messy and difficult to use)
ing_split = pd.DataFrame(preprocessed_data.ingredients.values.tolist()).add_prefix('ingredient_')

# Create mapping of ingredients to recipes
i = 0
while 'ingredient_' + str(i) in ing_split:
    if i == 0:
        ingredients_map = pd.concat([ing_split['ingredient_' + str(i)], preprocessed_data['name']], axis=1)
    else:
        pd.concat([ingredients_map, pd.concat([ing_split['ingredient_' + str(i)], preprocessed_data['name']], axis=1)], axis=0 )
    i += 1
ingredients_map.reset_index()
ingredients_map.columns = ['ingredient', 'recipe']

# Creates new json and saves cleaned data to it;
# indent prettifies the data, orient changes the notation of the data
# (values for orient='split', 'records', 'index', 'columns', 'values', 'table')
preprocessed_data.to_json("CLEANED_JOINED_data.json", orient='index', indent=4)
ingredients.to_json("all_ingredients.json", orient='index', indent=4)
ingredients_map.to_json("ingredients_map.json", orient='index', indent=4)