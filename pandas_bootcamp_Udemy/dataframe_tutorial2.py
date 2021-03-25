# Skill Challenges for Udemy course: The Ultimate Pandas Bootcamp: Advanced Python Data Analysis
import pandas as pd

players = pd.read_csv("data//soccer.csv")
print(players.info())
english_players = players["nationality"] == "England"
print(english_players)
avg_market_value = players["market_value"].mean()

big_market_value_players = players["market_value"] > 2 * avg_market_value

page_views_4000 = players["page_views"] > 4000
new_signing_players = players["new_signing"] == 1

players_for_exercise = players[english_players & big_market_value_players & (page_views_4000 ^ new_signing_players)]
print("----------------Players for exercise---------------")
print(players_for_exercise)

players.sort_values(by="age", inplace=True)
print(players.head(1))

players.set_index("club", inplace=True)
print(players.head())
players.sort_index(inplace=True)
print(players.head(40))

players.sort_values(by=["club", "market_value"], ascending=[True, False], inplace=True)
print(players.head(10))

players = pd.read_csv("data//soccer.csv")
players_deleted = players.drop(index=[2, 10, 21])
players.drop(labels="market_value", axis=1)
# or in one row: players.drop(index=[2,10,21],columns="market_value")
print(players_deleted)
print(players["nationality"].isna().sum() > 0)

players_dup = players_deleted.drop_duplicates(subset=["club", "position"], keep="first")
print(players_dup["name"])


def get_popularity(x):
    if x < 220:
        return "Relativly unknown"
    elif x < 600:
        return "Kind of Popular"
    elif x < 2000:
        return "Popular"
    else:
        return "Super Popular"


popularity = players.page_views.apply(get_popularity)
players.insert(0, "popularity", popularity)
print(players.head())
print(players["popularity"].value_counts())

players = pd.read_csv("data//soccer.csv")
players_random = players.sample(4).sample(4, axis=1)
print(players_random)
players_random.append(players_random.iloc[0])
# players_random.insert(0,"new col",pd.Series(data=[1,2,3,9]))

players_random = players_random.assign(goals_per_year=[12, 3, 3, 1])
print(players_random)
