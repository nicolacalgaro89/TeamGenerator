import pandas as pd
import numpy as np

# List to hold individual row DataFrames
rows = []

# Every person has a Team defined by a number:
# If Team != 0 team is fixed for that member. It is necessary to fix at least a capitain for every team.
# The number of teams depends only on the number of capitains.
# If Team = 0 let the software choose the teams for you with age optimization

data = [
    {'Person': 'Nome1',  'Age': 25, 'Team': 1},
    {'Person': 'Nome2',  'Age': 34, 'Team': 2},
    {'Person': 'Nome3',  'Age': 23, 'Team': 0},
    {'Person': 'Nome4',  'Age': 35, 'Team': 0},
    {'Person': 'Nome5',  'Age': 21, 'Team': 0},
    {'Person': 'Nome6',  'Age': 16, 'Team': 0},
    {'Person': 'Nome7',  'Age': 27, 'Team': 0},
    {'Person': 'Nome8',  'Age': 38, 'Team': 0},
    {'Person': 'Nome9',  'Age': 24, 'Team': 0},
    {'Person': 'Nome10', 'Age': 20, 'Team': 0},
    {'Person': 'Nome11', 'Age': 15, 'Team': 0},
    {'Person': 'Nome12', 'Age': 40, 'Team': 0},
    {'Person': 'Nome13', 'Age': 35, 'Team': 0},
    {'Person': 'Nome14', 'Age': 20, 'Team': 0},
    {'Person': 'Nome15', 'Age': 35, 'Team': 0},
    {'Person': 'Nome16', 'Age': 40, 'Team': 0},
    {'Person': 'Nome17', 'Age': 15, 'Team': 0},
    {'Person': 'Nome18', 'Age': 36, 'Team': 0},
    {'Person': 'Nome19', 'Age': 21, 'Team': 0},
    {'Person': 'Nome20', 'Age': 31, 'Team': 0},
    {'Person': 'Nome21', 'Age': 21, 'Team': 0},
    {'Person': 'Nome22', 'Age': 31, 'Team': 0},
    {'Person': 'Nome23', 'Age': 22, 'Team': 0},
    {'Person': 'Nome24', 'Age': 33, 'Team': 0},
    {'Person': 'Nome25', 'Age': 11, 'Team': 0},
    {'Person': 'Nome26', 'Age': 12, 'Team': 0},
    {'Person': 'Nome27', 'Age': 13, 'Team': 0},
    {'Person': 'Nome28', 'Age': 14, 'Team': 0},
    {'Person': 'Nome29', 'Age': 15, 'Team': 0},
    {'Person': 'Nome30', 'Age': 16, 'Team': 0},
]

# Create a DataFrame for each row and add it to the list
for row in data:
    row_df = pd.DataFrame([row])
    rows.append(row_df)

# Concatenate all the row DataFrames
df = pd.concat(rows, ignore_index=True)
    
df = df.sort_values('Age').reset_index(drop = True)

print("People data: ")
print(df)

for index, row in df.iterrows():
    count_df = df[df['Team'] > 0].groupby(['Team']).size().reset_index(name='Count')
    count_df = count_df.sort_values('Count').reset_index(drop = True)
    if row['Team'] == 0:
        df.at[index,'Team']=count_df.head()['Team'][0]

print(df)

# Group the DataFrame by 'Name'
grouped = df.groupby('Team')

# Iterate over the groups and print the group name and corresponding data
for team, group in grouped:
    print("Group Name:", team)
    print(group)
    print("Avg age:", group['Age'].mean())

#print(df.groupby(['Team']))


# # Calculate the number of people per cluster
# num_people = len(df)

# # Calculate the overall average age
# overall_avg_age = df['Age'].mean()



    # teamid = i+1
    # for index, row in df.iterrows():
    #     if teamid == row['team']:
    #         data['team'].append(te)
    #     if team == 0 :
    #         print("no team")

