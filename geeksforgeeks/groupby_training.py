import pandas as pd

df = pd.read_csv("data/nba.csv")
print(df.head())
print(df.info())
df.dropna(inplace=True)
# just some changes

perc = [0.20, 0.4, 0.8]
print(df.describe(percentiles=perc))

team = df.groupby("Team")
print(team.first())

for name, group in team:
    print(type(group))

print(team.get_group("Miami Heat"))

team_and_position = df.groupby(['Team', 'Position'])
print(team_and_position.first())

df.drop("Team", inplace=True, axis=1)
print(df)
print(df.index)
print(df.loc[0])
df = df.set_index('Name')

print(df.iloc[0])
print(df.loc["Avery Bradley"])
print(df.index)
print(df.head())
