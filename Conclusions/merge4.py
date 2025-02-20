#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:31:14 2023

@author: daasebre
"""

import pandas as pd

# Load the datasets
df1 = pd.read_csv('/Users/daasebre/Desktop/p4_combined_data.csv')
df2 = pd.read_csv('/Users/daasebre/Desktop/xx.csv')
df3 = pd.read_csv('/Users/daasebre/Desktop/ttlentexit1.csv')  # Replace with the correct path and encoding

# Ensure the date columns are in the correct format
df1['Start_Date'] = pd.to_datetime(df1['Start_Date'])
df2['DATE'] = pd.to_datetime(df2['DATE'])
df3['Date'] = pd.to_datetime(df3['Date'])

# Merge all datasets in one step
final_merged_df = df1.merge(df2, left_on='Start_Date', right_on='DATE', how='inner') \
                    .merge(df3, left_on='Start_Date', right_on='Date', how='inner')

# Save the final merged dataset to a new file, if needed
final_merged_df.to_csv('/Users/daasebre/Desktop/final_merged_dataset.csv', index=False)

# Display the first few rows of the final merged dataset
print(final_merged_df.head())