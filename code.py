import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Player': ['A', 'B', 'C', 'D'],
    'Team': ['Team A', 'Team B', 'Team C', 'Team D'],
    'Matches': [10, 12, 8, 15],
    'Runs': [490, 540, 290, 590]
}

df = pd.DataFrame(data)

# Calculate batting average using NumPy
df['Average'] = np.round(df['Runs'] / df['Matches'], 2)

# Display data
print("Player Statistics:")
print(df)

# Team performance
team_stats = df.groupby('Team')['Runs'].sum().sort_values(ascending=False)
print("\nTeam Rankings:")
print(team_stats)

# Visualization: Player Runs
plt.figure(figsize=(8,5))
plt.bar(df['Player'], df['Runs'], color='skyblue')
plt.xlabel('Players')
plt.ylabel('Runs Scored')
plt.title('Player Performance Analysis')
plt.show()