# CNN Weather Predictor

This repository contains the `CNN.py` script, which utilizes a Convolutional Neural Network (CNN) to predict extreme weather events based on public total entries and exits data.

## Overview

The script performs the following key functions:

### Data Preprocessing

- **Function**: `preprocess_data_nn`
- **Steps**:
  1. Loads the dataset and converts the 'Date' column to datetime format.
  2. Filters the data based on the year (e.g., data before 2020).
  3. Creates a binary 'ExtremeWeather' label based on thresholds for maximum temperature, minimum temperature, and snowfall/ice pellets/hail.
  4. Splits the dataset into features (Total Entries and Total Exits) and labels ('ExtremeWeather'), and further into training and testing sets.

### Neural Network Model Training

- **Function**: `train_and_evaluate_nn`
- **Steps**:
  1. Scales the features using StandardScaler.
  2. Constructs a neural network with three layers (two dense layers with 64 and 32 neurons, respectively, and an output layer) using ReLU and sigmoid activation functions.
  3. Compiles the model with the Adam optimizer and binary cross-entropy loss function.
  4. Trains the model over 200 epochs with a batch size of 10.

### Model Evaluation

- After training, the model shows a progressive decrease in loss and a stable increase in accuracy, as evident from the output of the final epochs. For instance, at epoch 200, the training accuracy is approximately 70.19%.
- The model is then evaluated on the test set, demonstrating a slightly higher accuracy of 70.42%, with a loss of 0.5727.

## Usage

To run the `CNN.py` script and perform the analysis:

```bash
python CNN.py
