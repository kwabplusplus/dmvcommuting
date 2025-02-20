# Read Me for Python Scripts

## Overview

This Read Me file provides guidance and explanations for three Python scripts: `Heatmap`, `Merge`, and `Scatter`. These scripts are designed for data analysis, specifically for analyzing correlations between weather conditions and commuting patterns, merging multiple datasets, and creating an interactive scatter plot. Each script utilizes Pandas for data handling and Plotly for visualization.

---

## 1. Heatmap Script

### Description
This script generates a correlation heatmap between various commuting metrics and weather conditions. It uses the Plotly library to create an interactive heatmap visualization.

### Key Steps
- Data loading from a CSV file.
- Selecting relevant columns for commuting and weather metrics.
- Calculating the correlation matrix of these metrics.
- Creating and displaying an interactive heatmap using Plotly.

### Usage
- **Data File:** `/Users/daasebre/Desktop/final_merged_dataset.csv` (Change this path to the location of your dataset.)
- **Columns:** Customize the `commuting_columns` and `weather_columns` lists as per your dataset's columns.

---

## 2. Merge Script

### Description
This script is used for merging multiple datasets into a single dataset. It ensures that date columns are in a consistent format before merging.

### Key Steps
- Loading multiple datasets from CSV files.
- Converting date columns into a standard datetime format.
- Merging datasets based on date columns.
- Saving the merged dataset to a new CSV file.

### Usage
- **Data Files:** Replace paths (`/Users/daasebre/Desktop/p4_combined_data.csv`, etc.) with the correct file paths.
- **Date Columns:** Ensure the date column names in your datasets match those in the script (`Start_Date`, `DATE`, `Date`).

---

## 3. Scatter Script

### Description
This script creates an interactive scatter plot visualizing the relationship between total rides and dates, color-coded by weather categories.

### Key Steps
- Data loading from a CSV file.
- Creating an interactive scatter plot with various data points (Total Rides, Date, Weather Category, etc.).
- Customizing hover data to display additional information.

### Usage
- **Data File:** `/Users/daasebre/Desktop/final_merged_dataset.csv` (Change this path to your dataset location.)
- **Columns and Parameters:** Adapt the x, y, color, and hover_data parameters based on your dataset's columns.

---

## General Notes
- **File Paths:** All scripts have hardcoded file paths. Change these paths to the locations of your datasets.
- **Environment Setup:** Ensure you have Pandas and Plotly installed in your Python environment.
- **Customization:** Modify column names and parameters as needed to suit your specific data analysis requirements.

Please follow the instructions in each section to adapt the scripts to your specific use case.
