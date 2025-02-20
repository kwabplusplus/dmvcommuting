import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('/Users/daasebre/Desktop/final_merged_dataset.csv')  # Replace with your file path

# Preparing the data for the plot (you can use a subset if the dataset is very large)
df_subset = df.head(1000)  # Using the first 1000 rows as an example

# Creating an interactive scatter plot
fig = px.scatter(
    df_subset, 
    x="Start_Date", 
    y="Total_Rides", 
    color="Weather Category",  # Color coding based on weather category
    hover_data=["Average_Duration", "Total Exits", "Total Positives", "Average Temperature (F)"],
    title="Interactive Scatter Plot of Total Rides vs Date with Weather Categories"
)

# Show the figure
fig.show()
