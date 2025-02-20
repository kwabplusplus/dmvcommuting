import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('/Users/daasebre/Desktop/final_merged_dataset.csv')

# Selecting relevant columns for the correlation heatmap
# Assuming 'Total_Rides', 'Average_Duration', 'Total Entries', 'Total Exits' are commuting metrics
# And 'Average Temperature (F)', 'Total Precipitation (in)', etc., are weather metrics
commuting_columns = ['Total_Rides', 'Average_Duration', 'Total Entries', 'Total Exits']
weather_columns = ['Average Temperature (F)', 'Total Precipitation (in)', 'Min Temperature (F)',
                   'Max Temperature (F)', 'Rain, Melted Snow, Etc. (in)', 'Snow, Ice Pellets, Hail (in)']

# Filtering the dataset for these columns
selected_data = data[commuting_columns + weather_columns]

# Calculating correlation
correlation_matrix = selected_data.corr()

# Creating a heatmap using Plotly
heatmap = px.imshow(correlation_matrix,
                    labels=dict(x="Metric", y="Metric", color="Correlation"),
                    x=correlation_matrix.columns,
                    y=correlation_matrix.columns,
                    color_continuous_scale='RdBu_r')

# Updating layout for better readability
heatmap.update_layout(title='Correlation Heatmap between Weather Conditions and Commuting Patterns',
                      xaxis_nticks=len(commuting_columns + weather_columns),
                      yaxis_nticks=len(commuting_columns + weather_columns))

heatmap.show()


