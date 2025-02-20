```markdown
# Interactive Data Visualizations with Plotly

This repository contains a collection of Python scripts that generate interactive visualizations using Plotly. The scripts are designed to visualize trends and patterns in public health and transportation data, specifically focusing on bike rides and COVID-19 case data.

## Installation

To get started, clone this repository to your local machine.

Install the required Python packages:

```bash
pip install pandas plotly
```

## Repository Overview

### Visualization Features

- **Time Series Analysis**: Visualizes trends in data over time, such as total bike rides and COVID-19 case counts.
- **Interactive Elements**: Includes range sliders and selectors for dynamic data exploration.
- **Multi-Axis Plots**: Combines different data types on a single plot with dual y-axes for comparative analysis.

### Scripts

Each script in the repository generates a specific type of interactive chart using data from `p4_combined_data.csv` or 'all_data.csv'. Key elements include:
- Rolling averages for smoothing time series data.
- Dynamic range selectors for focusing on specific time periods.
- Secondary y-axis for comparing different scales of data.

## Usage

Run the scripts individually to view and interact with the visualizations.

Ensure you have the `p4_combined_data.csv` and 'all_data.csv' files in your working directory, as the scripts read this file to generate the charts.

