import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame. This file contains information about various shows on Netflix.
netflix_df = pd.read_csv("netflix_data.csv")
print(netflix_df.iloc[0, 5])  # Printing the country of the first show for a quick data check

# Subset the DataFrame to include only movies, as we are interested in analyzing movie durations.
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Select only relevant columns for our analysis: title, country, genre, release year, and duration.
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

# Filter for movies with durations shorter than 60 minutes to analyze short movies.
short_movies = netflix_movies[netflix_movies.duration < 60]
print(short_movies)  # Printing short movies for a quick overview

# Initialize an empty list to store color values for different genres.
colors = []

# Iterate over each row in the netflix_movies DataFrame.
for label, row in netflix_movies.iterrows():
    # Assign colors based on the genre of the movie.
    if row['genre'] == "Children":
        colors.append('red')
    elif row['genre'] == "Documentaries":
        colors.append('blue')
    elif row['genre'] == "Stand-Up":
        colors.append('green')
    else:
        colors.append('black')

# Inspect the first 10 values of the colors list to verify color assignments.
colors[:10]

# Set up the figure for plotting.
fig = plt.figure(figsize=(12, 8))

# Create a scatter plot of movie duration versus release year.
# Colors represent different genres.
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)

# Adding a title and axis labels to the scatter plot.
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Display the plot.
plt.show()

# Placeholder response variable
answer = "maybe"
