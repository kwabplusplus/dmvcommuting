import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import chart_studio
import chart_studio.plotly as py

# Load data
df_combined = pd.read_csv('p4_combined_data.csv')

# Convert 'Start_Date' to datetime format for proper plotting
df_combined['Start_Date'] = pd.to_datetime(df_combined['Start_Date'])

# Filter data for the year 2021
df_combined = df_combined[df_combined['Start_Date'].dt.year == 2021]

# Calculate 14-day rolling averages
df_combined['14_day_avg_rides'] = df_combined['Total_Rides'].rolling(window=14).mean()
df_combined['14_day_avg_cases'] = df_combined['Daily_Cases'].rolling(window=14).mean()

# Create a subplot with 2 rows
fig = make_subplots(rows=2, cols=1, subplot_titles=("14-Day Average Total Bike Rides in 2021", "14-Day Average COVID-19 Cases in 2021"))

# Add Total Bike Rides to the first subplot
fig.add_trace(
    go.Scatter(x=df_combined['Start_Date'], y=df_combined['14_day_avg_rides'], name='14-Day Avg Total Bike Rides'),
    row=1, col=1
)

# Add COVID-19 Cases to the second subplot
fig.add_trace(
    go.Scatter(x=df_combined['Start_Date'], y=df_combined['14_day_avg_cases'], name='14-Day Avg COVID-19 Cases', marker_color='red'),
    row=2, col=1
)

# Update layout
fig.update_layout(height=600, width=800, title_text="14-Day Rolling Averages for 2021: Bike Rides and COVID-19 Cases", showlegend=False)
fig.update_xaxes(title_text="Date", row=1, col=1)
fig.update_xaxes(title_text="Date", row=2, col=1)
fig.update_yaxes(title_text="Total Bike Rides", row=1, col=1)
fig.update_yaxes(title_text="COVID-19 Cases", row=2, col=1)

# Show the figure
fig.show()

# Set up your Chart Studio credentials (you need to replace with your actual username and API key)
chart_studio.tools.set_credentials_file(username='rebeccaansell', api_key='pDNZQz5cJ8cT0lp5K8F7')

# Upload the plot to Chart Studio
plot_url = py.plot(fig, filename='MyPlot', auto_open=True)
print(plot_url)
