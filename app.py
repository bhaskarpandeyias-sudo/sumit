import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Player Performance Analysis")

# Dataset
data = {
    'Player': ['A', 'B', 'C', 'D'],
    'Team': ['Team A', 'Team B', 'Team C', 'Team D'],
    'Matches': [10, 12, 8, 15],
    'Runs': [490, 540, 290, 590]
}

df = pd.DataFrame(data)

# Average
df['Average'] = np.round(df['Runs'] / df['Matches'], 2)

st.subheader("Player Statistics")
st.dataframe(df)

st.subheader("Team Rankings")
team_stats = df.groupby('Team')['Runs'].sum().sort_values(ascending=False)
st.write(team_stats)

st.subheader("Player Runs Chart")
fig, ax = plt.subplots()
ax.bar(df['Player'], df['Runs'])
ax.set_xlabel("Players")
ax.set_ylabel("Runs")
st.pyplot(fig)
