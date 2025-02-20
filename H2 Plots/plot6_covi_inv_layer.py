import pandas as pd
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py

# Load your data
data = pd.read_csv('all_data.csv')  

# Convert the 'Start_Date' column to datetime format
data['Start_Date'] = pd.to_datetime(data['Start_Date'])

# Filter data for the year 2020
data_2020 = data[data['Start_Date'].dt.year == 2020]

# Calculate 14-day moving averages for Total_Rides, Average Temperature, and Daily Cases
data_2020['Moving_Avg_Rides'] = data_2020['Total_Rides'].rolling(window=14).mean()
data_2020['Moving_Avg_Temperature'] = data_2020['Max Temperature (F)'].rolling(window=14).mean()
data_2020['Moving_Avg_Cases'] = data_2020['Daily_Cases'].rolling(window=14).mean()

# Invert the COVID-19 cases graph
data_2020['Inverted_Moving_Avg_Cases'] = -data_2020['Moving_Avg_Cases']

# Create a single plot with the updated data
fig = go.Figure()

# Adding Moving_Avg_Rides to the plot with the primary y-axis
fig.add_trace(go.Scatter(x=data_2020['Start_Date'], y=data_2020['Moving_Avg_Rides'], name='14-Day Moving Avg Total Rides', mode='lines'))

# Adding Moving_Avg_Temperature to the plot with the secondary y-axis
fig.add_trace(go.Scatter(x=data_2020['Start_Date'], y=data_2020['Moving_Avg_Temperature'], name='14-Day Moving Avg Temperature (F)', mode='lines', line=dict(color='red'), yaxis='y2'))

# Adding Inverted_Moving_Avg_Cases to the plot with the tertiary y-axis
fig.add_trace(go.Scatter(x=data_2020['Start_Date'], y=data_2020['Inverted_Moving_Avg_Cases'], name='-14-Day Moving Avg Daily Cases (Inverted)', mode='lines', line=dict(color='green'), yaxis='y3'))

# Adding titles and labels
fig.update_layout(
    title='14-Day Moving Averages with Inverted COVID-19 Cases (Year 2020)',
    xaxis_title='Date',
    yaxis_title='14-Day Moving Avg Total Rides',
    yaxis2=dict(title='14-Day Moving Avg Temperature (F)', overlaying='y', side='right'),
    yaxis3=dict(title='-14-Day Moving Avg Daily Cases (Inverted)', overlaying='y', side='right', position=0.85)
)

# Show the figure
fig.show()
