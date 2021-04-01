import pandas as pd

interaction = pd.read_csv("RAW_interactions.csv")

interaction.drop(["review","user_id","date"],axis=1,inplace=True)

interaction.to_csv("CLEANED_interactions.csv",index=False)