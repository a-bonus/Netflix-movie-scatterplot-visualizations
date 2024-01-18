# Netflix Movies Duration Analysis

## Project Overview

This project explores a dataset containing information about movies and series available on Netflix. The primary focus is to investigate if the average duration of movies on Netflix has been declining and to identify any contributing factors.

## Dataset Description

The `netflix_data.csv` file is used for this analysis. It includes the following columns:

- `show_id`: The ID of the show.
- `type`: Type of the show (Movie/Series).
- `title`: Title of the show.
- `director`: Director of the show.
- `cast`: Cast of the show.
- `country`: Country of origin.
- `date_added`: Date added to Netflix.
- `release_year`: Year of Netflix release.
- `duration`: Duration of the show in minutes.
- `description`: Description of the show.
- `genre`: Show genre.

## Tools and Libraries Used

- **Python:** Programming language for scripting the analysis.
- **Pandas:** Python library for data manipulation and analysis.
- **Matplotlib:** Python library for creating static, animated, and interactive visualizations.

## Analysis Workflow

1. **Data Loading and Cleaning:**
   - Load the data from the CSV file.
   - Inspect and clean the data as necessary.

2. **Data Filtering:**
   - Subset the data to focus on movies.
   - Select relevant columns for further analysis.

3. **Exploratory Analysis:**
   - Examine short-duration movies.
   - Investigate the distribution of movie genres.

4. **Visualization:**
   - Plot a scatter graph to display movie durations against their release years.
   - Use different colors to represent various movie genres.

5. **Insights:**
   - Analyze the trend of movie durations over the years.
   - Discuss any observable patterns with respect to movie genres.

## Results

The scatter plot visualizes the relationship between the duration of movies and their release years, with different colors indicating various genres. This helps in identifying any trends in movie durations over time and assessing if there has been a decline in average durations.

## Running the Analysis

To execute this analysis:

1. Ensure Python, Pandas, and Matplotlib are installed on your system.
2. Clone the repository containing the script and dataset.
3. Run the Python script `netflix_movie_duration_analysis.py` to perform the analysis and generate visualizations.

## From DataCamp Portfolio
https://app.datacamp.com/workspace/w/3b9f64e2-3fb2-48a4-b797-8459a7a2b3f4/edit


